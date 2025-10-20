import pandas as pd
from typing import List
from pydantic import BaseModel
from .schemas import TitanicPassenger

def dataframe_to_pydantic(df: pd.DataFrame, model_class) -> List[BaseModel]:
    """Convert DataFrame rows to list of Pydantic models"""
    models = []
    for _, row in df.iterrows():
        # Convert NaN values to None for Pydantic compatibility
        row_dict = row.to_dict()
        row_dict = {k: (v if pd.notna(v) else None) for k, v in row_dict.items()}
        
        model = model_class(**row_dict)
        models.append(model)
    
    return models


