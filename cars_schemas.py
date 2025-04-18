from pydantic import BaseModel


class CarsCreateSchema(BaseModel):
    type: str
    brand: str
    model: str
    year: int
    mileage: int
    color: str
    price: int
    engine: str
    engine_capacity: float
    gearbox: str
    drive: str
    steering_wheel: str
    region: str
    description: str
    phone_number: str
