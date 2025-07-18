#  FastAPI Chat App

A real-time chat application built using **FastAPI**, **WebSockets**, **JWT Authentication**, and **PostgreSQL**.

## Features

- User Registration & Login (with JWT)
- Role-based Access Control (Admin/User)
- Room-based chat system
- Real-time messaging using WebSockets
- PostgreSQL + SQLAlchemy ORM for persistence
- Cursor-based pagination for chat history

---

##  Tech Stack

- **Backend**: FastAPI, WebSockets, SQLAlchemy
- **Database**: PostgreSQL
- **Authentication**: JWT (PyJWT or similar)
- **WebSocket Server**: Uvicorn
- **Others**: Pydantic, Alembic (optional for migrations)

---

##  Setup Instructions

### 1. Clone the Repository

    ```bash
    git clone https://github.com/YourUsername/ChatApp.git
    cd ChatApp

### 2. Create & Activate a Virtual Environment

    ```bash
    python -m venv venv
    venv\Scripts\activate

### 3. Install Dependencies
    ```bash
    pip install -r requirements.txt

### 4. Run the App
    ```bash
    uvicorn main:app --reload

    The app will be running at:
    http://127.0.0.1:8000


##  WebSocket Usage

Endpoint: ws://localhost:8000/ws/{room_id}?token=your_jwt_token

Use tools like Postman WebSocket or frontend clients.

example:
 ``bash
 ws://localhost:8000/ws/1?token=eyJhbGciOi...

## API Testing in Postman
-> Register: POST /signup

-> Login: POST /login

-> Authenticated endpoints require Bearer token in headers:
    Authorization: Bearer <your_token>










