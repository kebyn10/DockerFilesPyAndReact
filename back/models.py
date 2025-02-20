from pydantic import BaseModel ,Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls,v):
        if not ObjectId.is_valid(v):
            raise ValueError("invalid")
        return str(v)

class Task(BaseModel):
    id:Optional[PyObjectId]= Field(alias="_id")
    title:str
    description:str
    completed:bool=False

    class Config:
        orm_mode=True
        allow_population_by_field_name=True
        json_encoders={ObjectId:str}