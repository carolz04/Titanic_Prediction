import pandas as pd
from utils.readers import CSVReader
from loguru import logger
from src.processing.processing import df_to_pydantic
import argparse

class Transform:
    def __init__(self, data: pd.DataFrame= None, data_type: str='training'):
        if data is not None: 
            self.data = data
        else:
            reader = CSVReader(data_type=data_type)
            self.data = reader.read_csv()

    def transform_data(self):
        df_validated = df_to_pydantic(data=self.data, data_type=self.data)
        logger.info(f"Data transformed successfully")
        return df_validated

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-type", default="training")
    args = parser.parse_args()
    
    logger.info(f"Starting transformation for {args.data_type} data")
    transformer = Transform(data_type=args.data_type)
    result = transformer.transform_data()
    logger.info(f"Successfully transformed {len(result)} rows")

