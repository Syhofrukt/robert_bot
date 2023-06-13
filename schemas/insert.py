from pydantic import BaseModel

class InsertDataModel(BaseModel):
    key: str
    name: str
    day: int
    month: int
    year: int
    hour: int
    minute: int
