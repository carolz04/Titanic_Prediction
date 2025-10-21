from pydantic import BaseModel, Field, field_validator
from enum import Enum
from typing import Optional, Annotated
import math
from loguru import logger
import processing


class Pclass(int, Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3

class Sex(str, Enum):
    MALE = 'male'
    FEMALE = 'female'

class Embarked(str, Enum):
    CHERBOURG = 'C'
    QUEENSTOWN = 'Q'
    SOUTHAMPTON = 'S'

class TitanicSchema(BaseModel):

    model_config = {
        "use_enum_values": True
    }  
    PassengerId: Optional[int] = None
    Survived: Optional[int] = Field(None, description="Survived or not")
    Pclass: Pclass
    Name: Optional[str] = None
    Sex: Sex
    Age: Optional[float] = Field(None, description="Age of the passenger", ge=0, lt=100) # Allow none for missing ages
    SibSp: int = Field(ge=0)
    Parch: int = Field(ge=0)
    Ticket: str
    Fare: float= Field(ge=0)
    Cabin: Optional[str] = None
    Embarked: Annotated[Optional[Embarked], Field(default=None)]

    @field_validator('Cabin', mode='before')
    def fill_cabin_with_most_frequent(cls,v):
        if v is None or (isinstance(v, float) and math.isnan(v)):
            return cls._most_frequent_cabin
        return v
    
    @classmethod
    def set_most_frequent_cabin(cls, cabin: str):
        return cls._most_frequent_cabin

    @field_validator('Cabin', 'Age','Embarked', mode='before')
    def nan_to_none(cls,v):
        if isinstance(v,float) and math.isnan(v):
            return None
        return v

    @field_validator('Embarked', mode='before')
    def coerce_embarked(cls,v):
        if isinstance(v, str):
            try:
                return Embarked(v)
            except ValueError as e:
                logger.error(f'Error in the embarked field {e}')
                return None
        return v
       

