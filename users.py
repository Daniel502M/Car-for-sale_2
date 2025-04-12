from fastapi import APIRouter, Depends
from dbconn import DbConn
from users_schemas import UserSchema, UserUpdateSchema
from auth_schemas import UserSignUpSchema
from pydantic import EmailStr
from security import hash_password

import auth


user_crud_router = APIRouter(tags=['User CRUD'])


# @_GET

@user_crud_router.get("/users/get/all")
def get_all_users():
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM users""")

    users = dbconn.cursor.fetchall()

    return users


user_get_router = APIRouter(tags=['User Get'])


@user_get_router.get("/user/get/by_id/{user_id}")
def get_user_by_id(user_id: int):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM users WHERE id=%s""",
                          (user_id,))
    user = dbconn.cursor.fetchone()

    return user


@user_get_router.get("/user/get/by_name/{user_name}")
def get_users_by_name(user_name: str):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM users WHERE name=%s""",
                          (user_name,))

    user = dbconn.cursor.fetchone()

    return user


@user_get_router.get("/user/get/by_email/{user_email}")
def get_user_by_email(user_email: EmailStr):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM users WHERE email=%s""",
                          (user_email,))

    user = dbconn.cursor.fetchone()

    return user


# @_UPDATE

@user_crud_router.put("/update/user-by-id/{user_id}")
def update_user_by_id(user_update_data: UserUpdateSchema, user_id: int,
                      current_user=Depends(auth.get_current_user)):

    user_id = current_user.get("user_id")  # Извлекаем user_id из словаря

    dbconn = DbConn()
    try:
        hashed_password = hash_password(user_update_data.password)
    except Exception as err:
        raise err

    try:
        dbconn.cursor.execute("""UPDATE users SET name=%s, password=%s WHERE user_id=%s""",
                              (user_update_data.name, hashed_password, user_id))

        dbconn.conn.commit()
    except Exception as err:
        raise err

    return "User updated"


# @_DELETE

@user_crud_router.delete("/users/delete/by-user-id/{user_id}")
def delete_user_by_id(user_id: int, user_create_data: UserSignUpSchema,
                      current_user=Depends(auth.get_current_user)):

    user_id = current_user.get("user_id")  # Извлекаем user_id из словаря

    dbconn = DbConn()

    dbconn.cursor.execute("""DELETE FROM users WHERE id=%s""",
                          (user_id,))

    dbconn.conn.commit()

    return "User deleted"
