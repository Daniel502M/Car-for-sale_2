from fastapi import APIRouter, Depends, HTTPException
from dbconn import DbConn
from favorites_schemas import UserFavoriteCars

import auth


user_favorites_router = APIRouter(tags=['Favorite Cars CRUD'])


@user_favorites_router.post("/user/favorite/cars")
def create_favorite_car(data: UserFavoriteCars,
                        current_user=Depends(auth.get_current_user)):

    user_id = current_user.get("user_id")  # Извлекаем user_id из словаря

    dbconn = DbConn()

    dbconn.cursor.execute("""INSERT INTO favorite_cars (user_id, post_id) VALUES (%s, %s)""",
                          (user_id, data.post_id))

    dbconn.conn.commit()

    return "OK"


@user_favorites_router.get("/user/favorite/cars/all")
def get_all_cars():
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM favorite_cars""")

    cars = dbconn.cursor.fetchall()

    return cars


@user_favorites_router.delete("/user/favorite/delete/{post_id}")
def delete_favorite_car_by_id(post_id: int,
                              current_user=Depends(auth.get_current_user)):

    user_id = current_user.get("user_id")  # Извлекаем user_id из словаря

    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM favorite_cars WHERE user_id=%s""",
                          (user_id,))

    user = dbconn.cursor.fetchone()

    if dict(user).get("user_id") != user_id:
        raise HTTPException(status_code=403, detail="user != user_id")
    else:
        dbconn.cursor.execute("""DELETE FROM favorite_cars WHERE post_id=%s""",
                              (post_id,))

        dbconn.conn.commit()

    return "Favorite car deleted"
