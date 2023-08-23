import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import pandas as pd
import numpy as np
import re
import os

from utilities import custom_logging

logger = custom_logging.CustomLogging(__name__)

class DataRetriever:
    """
    A class for retrieving data from a given A data path and processing it for further analysis.

    Parameters:
        data_path (str): The file path from which the data will be loaded.

    Attributes:
        data_path (str): The file path from which the data will be loaded.
        """
    

    RETRIEVED_DATA = 'heart_2020_cleaned.csv' # File name for the retrieved data.

    def __init__(self, url, data_path):
        self.url = url
        self.DATASETS_DIR = data_path

    def retrieve_data(self):
        """
        Retrieves data from the specified path, processes it, and stores it in a CSV file.

        Returns:
            str: A message indicating the location of the stored data.
        """    
        # Loading data from specific path
        data = pd.read_csv(self.url) 

        # Create directory if it does not exist
        if not os.path.exists(self.DATASETS_DIR):
            os.makedirs(self.DATASETS_DIR)
            print(f"Directory '{self.DATASETS_DIR}' created successfully.")
        else:
            print(f"Directory '{self.DATASETS_DIR}' already exists.")

        # Save data to CSV file
        data.to_csv(self.DATASETS_DIR + self.RETRIEVED_DATA, index=False)
        logger.info("Stored data")
        return f'Data stored in {self.DATASETS_DIR + self.RETRIEVED_DATA}'
       