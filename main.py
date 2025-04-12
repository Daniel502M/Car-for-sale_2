from fastapi import FastAPI
import uvicorn
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from models import Base
from database import engine
from auth import auth_router
from cars import cars_crud_router, cars_get_router
from users import user_crud_router, user_get_router
from favorites import user_favorites_router
from messages import message_crud_router

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
app.include_router(cars_crud_router)
app.include_router(cars_get_router)
# users
app.include_router(user_crud_router)
app.include_router(user_get_router)
# favorites
app.include_router(user_favorites_router)
# messages
app.include_router(message_crud_router)


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
