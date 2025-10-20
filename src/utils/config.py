import os
from dotenv import load_dotenv
from typing import Optional


# Load the environment variables from .env file
load_dotenv()

class Config:
    """Configuration class to handle the environment variables"""

    # Data paths
    TRAINING_PATH = os.getenv('TRAINING_PATH')
    TEST_PATH = os.getenv('TEST_PATH')


    @classmethod
    def get_data_path(cls, data_type:str) -> str:
        """Get data path by type"""

        path_mapping = {
            'training': cls.TRAINING_PATH,
            'test': cls.TEST_PATH,
        }

        path = path_mapping.get(data_type.lower())
        if path is None:
            raise ValueError(f'Uknowrn data type {data_type}')
        
        return path

    def get_env_var(cls, var_name: str, default: Optional[str]= None) -> str:
        
        value = os.getenv(var_name, default)
        if value is None:
            raise ValueError("Environment variable not found")