# from fastapi import APIRouter, FastAPI, File, UploadFile, Form
# import os
# import shutil
#
# app = FastAPI()
# upload_router = APIRouter()
#
# # Папка для хранения загруженных файлов
# UPLOAD_DIR = "uploads/"
# os.makedirs(UPLOAD_DIR, exist_ok=True)
#
# @upload_router.post("/upload-photo")
# async def upload_photo(
#     username: str = Form(...),  # Имя пользователя
#     photo: UploadFile = File(...)  # Загрузка файла
# ):
#     # Путь для сохранения файла
#     file_path = os.path.join(UPLOAD_DIR, photo.filename)
#
#     # Сохранение файла на сервере
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(photo.file, buffer)
#
#     return {
#         "message": "Фото успешно загружено",
#         "username": username,
#         "photo_url": f"/static/{photo.filename}"  # Ссылка на фото
#     }
#
# # # Подключаем маршруты к основному приложению
# # app.include_router(upload_router)
#
# # Настройка для предоставления доступа к загруженным файлам
# from fastapi.staticfiles import StaticFiles
# app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")
