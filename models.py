from sqlalchemy import Column, Integer, String, TIMESTAMP, text, Float

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))


class Cars(Base):
    __tablename__ = "cars"

    id = Column(Integer, nullable=False, primary_key=True)
    type = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    mileage = Column(Integer, nullable=False)
    color = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    engine = Column(String, nullable=False)
    engine_capacity = Column(Float, nullable=False)
    gearbox = Column(String, nullable=False)
    drive = Column(String, nullable=False)
    steering_wheel = Column(String, nullable=False)
    region = Column(String, nullable=False)
    description = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))


# class BayedCourses(Base):
#     __tablename__ = "bayed_courses"
#
#     id = Column(Integer, nullable=False, primary_key=True)
#     user_id = Column(Integer, nullable=False)
#     curs_id = Column(Integer, nullable=False)
#     # name = Column(String, nullable=False)
#     # duration = Column(Integer, nullable=False)
#     # price = Column(Float, nullable=False)
#     created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))


class Favorite(Base):
    __tablename__ = "favorite_cars"

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, nullable=False)
    post_id = Column(Integer, nullable=False)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, nullable=False)
    post_id = Column(Integer, nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
