import pandas as pd
from .config import Config
from loguru import logger

class CSVReader:
    def __init__(self, path: str = None, data_type: str = None):
        if path is not None:
            self.path = path
        elif data_type is not None:
            self.data_type = Config.get_data_path(data_type)
            logger.info(f'Training path fetched here {self.data_type}')

        else:
            raise ValueError("Data type or path nor provided")

    def read_csv(self) -> pd.DataFrame:
        return pd.read_csv(self.data_type)


class ExcelReader:
    def __init__(self, path: str):
        self.path = path

    def read_excel(self) -> pd.DataFrame:
        return pd.read_excel(self.path)


class JSONReader:
    def __init__(self, path: str):
        self.path = path

    def read_json(self) -> pd.DataFrame:
        return pd.read_json(self.path)
