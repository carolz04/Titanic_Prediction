from pydantic import BaseModel, Field
from typing import Optional
import pandas as pd

class TitanicSchema(BaseModel):
    PassengerId:int
    Survived: Optional[int] = None
    Pclass: int
    Name: str
    Age: Optional[int] = None
    SibSp: int 
    Parch: int
    Ticket: str
    Fare: Optional[float]= None
    Cabin: Optional[str] = None
    Embarked: Optional[str] = None
