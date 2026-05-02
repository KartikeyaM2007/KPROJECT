import os
import sys
import pandas as pd

from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")


class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting data ingestion")

        try:
            df = pd.read_csv('notebook/data/stud.csv')

            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)

            df.to_csv(self.config.raw_data_path, index=False)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.config.train_data_path, index=False)
            test_set.to_csv(self.config.test_data_path, index=False)

            logging.info("Data ingestion completed")

            return (
                self.config.train_data_path,
                self.config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()

    from src.components.data_transformation import DataTransformation

    transformer = DataTransformation()
    transformer.initiate_data_transformation(train_path, test_path)