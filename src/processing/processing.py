import pandas as pd
from .schemas import TitanicSchema
from pandantic import Pandantic
from utils.readers import CSVReader
from loguru import logger


def df_to_pydantic(data: pd.DataFrame= None, data_type: str='training'):
    if data is not None:
        df = data.copy()
    else:
        reader = CSVReader(data_type=data_type)
        df = reader.read_csv()

    try: 
        validator = Pandantic(schema=TitanicSchema)
        df_validated = validator.validate(dataframe=df, errors="raise")
       
        logger.info(f"Data validated successfully: {df_validated}")

        cabin_values = df['Cabin'].dropna()
        if len(cabin_values)>0:
            most_frequent_cabin = cabin_values.mode().iloc[0]
        return df_validated
    except Exception as e:
        logger.error(f"Validation error: {e}")
        return None


