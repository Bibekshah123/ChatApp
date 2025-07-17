from fastapi import FastAPI, Depends, HTTPException
from app import models, database, auth, schemas
from sqlalchemy.orm import Session
from fastapi import WebSocket
from app.chat import websocket_endpoint

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(auth.get_db)):
    hashed = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, password=hashed, role=user.role)
    db.add(db_user)
    db.commit()
    return {"msg": "User created"}

@app.post("/login", response_model=schemas.Token)
def login(user: schemas.UserLogin, db: Session = Depends(auth.get_db)):
    db_user = db.query(models.User).filter_by(username=user.username).first()
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = auth.create_access_token({"sub": db_user.username, "role": db_user.role})
    return {"access_token": token, "token_type": "bearer"}

@app.websocket("/ws/{room_id}")
async def chatroom(websocket: WebSocket, room_id: str, token: str):
    db = next(auth.get_db())
    await websocket_endpoint(websocket, room_id, token, db)