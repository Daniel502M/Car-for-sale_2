from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Header, status
from fastapi.exceptions import HTTPException
from dbconn import DbConn

from auth_schemas import UserSignUpSchema, UserLoginSchema
from security import hash_password, verify_password
from cars_schemas import CarsCreateSchema
from typing import Optional
from auth import verify_token
from messages_schemas import MessageSchema, MessageUpdateSchema

import auth


message_crud_router = APIRouter(tags=['Messages CRUD'])


@message_crud_router.post("/massage/create")
def create_message(data: MessageSchema,
                   current_user=Depends(auth.get_current_user)):

    user_id = current_user.get("user_id")  # Извлекаем user_id из словаря

    dbconn = DbConn()

    dbconn.cursor.execute("""INSERT INTO messages (user_id, post_id, message) VALUES (%s, %s, %s)""",
                          (user_id, data.post_id, data.message))

    dbconn.conn.commit()

    return "Message delivered successfully"


@message_crud_router.get("/message/get/all")
def get_all_messages():

    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM messages""")

    messages = dbconn.cursor.fetchall()

    return messages


@message_crud_router.put("/message/update/{id}")
def update_message_by_id(id: int, data: MessageUpdateSchema,
                         current_user=Depends(auth.get_current_user)):

    user_id = current_user.get("user_id")  # Извлекаем user_id из словаря

    dbconn = DbConn()

    dbconn.cursor.execute("""UPDATE messages SET message=%s WHERE id=%s AND user_id=%s""",
                          (data.message, id, user_id))

    dbconn.conn.commit()

    return "Message updated successfully"


@message_crud_router.delete("/message/delete/{id}")
def delete_message_by_id(id: int,
                         current_user=Depends(auth.get_current_user)):

    user_id = current_user.get("user_id")  # Извлекаем user_id из словаря

    dbconn = DbConn()

    dbconn.cursor.execute("""DELETE FROM messages WHERE id=%s AND user_id=%s""",
                          (id, user_id))

    dbconn.conn.commit()

    return "Message deleted successfully"
