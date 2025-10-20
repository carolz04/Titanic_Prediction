import pandas as pd
from utils.readers import CSVReader
import argparse
from loguru import logger
from processing import dataframe_to_pydantic
from ..processing.schemas import TitanicSchema

class Transform:
    def __init__(self, data: pd.DataFrame= None, data_type: str='training'):
        if data is not None: 
            self.data = data
        else:
            reader = CSVReader(data_type=data_type)
            self.data = reader.read_csv()

    def transform_data():
        parser = argparse.ArgumentParser(description="Transform titanic data")
        parser.add_argument('--data-type', required=True,
        choices=['training', 'test'],
        help="Type of data to process")
        args = parser.parse_args()

        transform = Transform(data_type=args.data_type)
        logger.info('Transform data completed')






