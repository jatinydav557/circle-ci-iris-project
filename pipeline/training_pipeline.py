import sys
import os
from src.data_processing import DataProcessing
from src.model_training import ModelTraining
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
if __name__ == "__main__":
    data_processor = DataProcessing("artifacts/raw/data.csv")
    data_processor.run()

    trainer =  ModelTraining()
    trainer.run()

