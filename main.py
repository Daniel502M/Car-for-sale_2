from fastapi import FastAPI
import uvicorn
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from models import Base
from database import engine
from auth import auth_router
from cars import cars_router, cars_router1
from users import user_router, user_router1, user_favorites

# from download_photo import upload_router


Base.metadata.create_all(bind=engine)

while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            database='car_for_sale',
            password='password',
            cursor_factory=RealDictCursor
        )

        cursor = conn.cursor()
        break
    except Exception as err:
        print(err)
        time.sleep(3)

app = FastAPI()


@app.get('/')
def main():
    return "Ok"


# auth
app.include_router(auth_router)
# cars
app.include_router(cars_router)
app.include_router(cars_router1)
# app.include_router(cars_router2)
# app.include_router(cars_router3)
# user
app.include_router(user_router)
app.include_router(user_router1)
app.include_router(user_favorites)

# app.include_router(upload_router)


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
