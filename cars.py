from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Header, status
from fastapi.exceptions import HTTPException
from dbconn import DbConn


from auth_schemas import UserSignUpSchema, UserLoginSchema
from security import hash_password, verify_password
from cars_schemas import CarsCreateSchema
# from buy_courses_schemas import BuyCoursesSchemas
from typing import Optional
from auth import verify_token
import auth

cars_router = APIRouter(tags=['Cars Create'])


# @_CREATE:

@cars_router.post("/create/cars")
def add_cars(data: CarsCreateSchema,
             current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""INSERT INTO cars (tipe, brand, model, year, mileage, color,
        price, engine, engine_capacity, gearbox, drive, steering_wheel, region, description, user_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                          (data.tipe, data.brand, data.model, data.year, data.mileage, data.color, data.price, data.engine,
                           data.engine_capacity, data.gearbox, data.drive, data.steering_wheel, data.region, data.description, data.user_id))

    dbconn.conn.commit()

    return "OK"


# @_GET:
cars_router1 = APIRouter(tags=['Cars Get'])

@cars_router1.get("/cars/by-id/{id}")
def get_cars_by_id(id: int,
                   current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE id=%s""",
                          (id,))

    cars = dbconn.cursor.fetchone()

    return cars


@cars_router1.get("/cars/by-type/{type}")
def get_cars_by_type(type,
                     current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE tipe=%s""",
                          (type,))

    cars = dbconn.cursor.fetchall()

    return cars


@cars_router1.get("/cars/by-brand/{brand}")
def get_cars_by_brand(brand,
                      current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE brand=%s""",
                          (brand,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/cars/by-model/{model}")
def get_cars_by_model(model,
                      current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE model=%s""",
                          (model,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/cars/by-year/{year}")
def get_cars_by_year(year,
                     current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE year=%s""",
                          (year,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/cars/by-mileage/{mileage}")
def get_cars_by_mileage(mileage,
                        current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE mileage=%s""",
                          (mileage,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/cars/by-color/{color}")
def get_cars_by_color(color,
                      current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE color=%s""",
                          (color,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/cars/by-price/{start_price}-{end_price}")
def get_cars_by_price(start_price, end_price,
                      current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE price>=%s and price<=%s""",
                          (start_price, end_price))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/cars/by-engine/{engine}")
def get_cars_by_engine(engine,
                       current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE engine=%s""",
                          (engine,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/cars/by_engine_capacity/{engine_capacity}")
def get_cars_by_engine_capacity(engine_capacity,
                                current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE engine_capacity=%s""",
                          (engine_capacity,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/cars/by-gearbox/{gearbox}")
def get_cars_by_gearbox(gearbox,
                        current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE gearbox=%s""",
                          (gearbox,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/cars/by-drive/{drive}")
def get_cars_by_drive(drive,
                      current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE drive=%s""",
                          (drive,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/cars/by_steering_wheel/{steering_wheel}")
def get_cars_by_steering_wheel(steering_wheel,
                               current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE steering_wheel=%s""",
                          (steering_wheel,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/cars/by_region/{region}")
def get_cars_by_region(region,
                       current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE region=%s""",
                          (region,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/cars/by_user_id/{user_id}")
def get_cars_by_user_id(user_id,
                        current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE user_id=%s""",
                          (user_id,))

    cars = dbconn.cursor.fetchall()

    return cars


# @_UPDATE:
cars_router2 = APIRouter(tags=['Cars Update'])

@cars_router2.put("/cars/update/by-id/{id}")
def update_cars_by_id(data: CarsCreateSchema, id,
                      current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""UPDATE cars SET tipe=%s, brand=%s, model=%s, year=%s, mileage=%s, color=%s, price=%s,
                        engine=%s, engine_capacity=%s, gearbox=%s, drive=%s, steering_wheel=%s, region=%s, description=%s WHERE user_id=%s""",
                          (data.tipe, data.brand, data.model, data.year, data.mileage, data.color, data.price,
                           data.engine, data.engine_capacity, data.gearbox, data.drive, data.steering_wheel, data.region,
                           data.description, data.user_id))

    dbconn.conn.commit()

    return "OK"


# DELETE:
cars_router3 = APIRouter(tags=['Cars Delete'])

@cars_router3.delete("/cars/delete/by-id/{id}")
def delete_cars_by_id(id,
                      current_user = Depends(auth.get_current_user)):
    dbconn = DbConn()

    dbconn.cursor.execute("""DELETE FROM cars WHERE id=%s""",
                          (id,))

    dbconn.conn.commit()

    return "OK"




# .get("/users/{id}")
# .get("/users/{name}")
# .get("/users/{email}")
#
# /users/Vaxo


# .get("/users/by-id/{id}")
# .get("/users/by-name/{name}")
# .get("/users/by-email{email}")
#
# /users/by-name/Vaxo

