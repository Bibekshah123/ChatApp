from fastapi import WebSocket, Depends, WebSocketDisconnect
from sqlalchemy.orm import Session
from app.auth import decode_token, get_db
from app import models
from app.websocket_manager import ConnectionManager
import json

manager = ConnectionManager()

async def websocket_endpoint(websocket: WebSocket, room_id: str, token: str, db: Session = Depends(get_db)):
    payload = decode_token(token)
    username = payload.get("sub")
    await manager.connect(room_id, websocket)

    # Send last 10 messages
    messages = db.query(models.Message).filter_by(room_id=room_id).order_by(models.Message.id.desc()).limit(10).all()
    for msg in reversed(messages):
        await websocket.send_text(f"{msg.sender}: {msg.content}")

    try:
        while True:
            data = await websocket.receive_text()
            msg_obj = models.Message(room_id=room_id, sender=username, content=data)
            db.add(msg_obj)
            db.commit()
            await manager.broadcast(room_id, f"{username}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
