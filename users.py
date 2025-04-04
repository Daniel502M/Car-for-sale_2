from fastapi import APIRouter, Depends
from dbconn import DbConn
from users_schemas import UserSchema, UserUpdateSchema
from auth_schemas import UserSignUpSchema
from pydantic import EmailStr
from security import hash_password
import auth


user_router = APIRouter(tags=['User Get'])

# @_GET

# @user_router.get("/users")
# def get_all_users():
#     dbconn = DbConn()
#
#     dbconn.cursor.execute("""SELECT * FROM users""")
#
#     users = dbconn.cursor.fetchall()
#
#     return users
#
#
# @user_router.get("/{user_id}")
# def get_user_by_id(id):
#     dbconn = DbConn()
#
#     dbconn.cursor.execute("""SELECT * FROM users WHERE id=%s""",
#                           (id,))
#     user = dbconn.cursor.fetchone()
#
#     return user
#
#
# @user_router.get("/{user_name}")
# def get_users_by_name(data: UserSchema, name: str):
#     dbconn = DbConn()
#
#     dbconn.cursor.execute("""SELECT * FROM users WHERE name=%s""",
#                           (name,))
#
#     user = dbconn.cursor.fetchall()
#
#     return user
#
#
# @user_router.get("/user_email")
# def get_user_by_email(data: UserSchema, email: EmailStr):
#     dbconn = DbConn()
#
#     dbconn.cursor.execute("""SELECT *FROM users WHERE email=%s""",
#                           (email,))
#
#     user = dbconn.cursor.fetchall()
#
#     return user


user_router1 = APIRouter(tags=['User Update'])

# @_UPDATE

@user_router1.put("/update/user-by-id/{user_id}")
def update_user_by_id(user_create_data: UserUpdateSchema, user_id: int,
                      current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()
    try:
        hashed_password = hash_password(user_create_data.password)
    except Exception as err:
        raise err

    try:
        dbconn.cursor.execute("""UPDATE users SET name=%s, password=%s WHERE id=%s""",
                              (user_create_data.name, hashed_password, user_id))

        dbconn.conn.commit()
    except Exception as err:
        raise err

    return "User updated"


# @user_router1.put("/user_name")
# def update_user_by_name(user_create_data: UserSignUpSchema, name: str):
#     dbconn = DbConn()
#     try:
#         hashed_password = hash_password(user_create_data.password)
#     except Exception as err:
#         raise err
#
#     try:
#         dbconn.cursor.execute("""UPDATE users SET name=%s, email=%s, password=%s WHERE name=%s""",
#                               (user_create_data.name, user_create_data.email, hashed_password, name))
#
#         dbconn.conn.commit()
#     except Exception as err:
#         raise err
#
#     return "User updated"
#
#
# @user_router1.put("/user_email")
# def update_user_by_email(user_create_data: UserSignUpSchema, email: EmailStr):
#     dbconn = DbConn()
#     try:
#         hashed_password = hash_password(user_create_data.password)
#     except Exception as err:
#         raise err
#
#     try:
#         dbconn.cursor.execute("""UPDATE users SET name=%s, email=%s, password=%s WHERE email=%s""",
#                               (user_create_data.name, user_create_data.email, hashed_password, email))
#
#         dbconn.conn.commit()
#     except Exception as err:
#         raise err
#
#     return "User updated"


user_router2 = APIRouter(tags=['User Delete'])

# @_DELETE

@user_router2.delete("/users/delete/by-user-id/{user_id}")
def delete_user_by_id(user_id: int,
                      current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""DELETE FROM users WHERE id=%s""",
                          (user_id,))

    dbconn.conn.commit()

    return "User deleted"