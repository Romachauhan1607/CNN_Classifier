import os                           
import urllib.request as request     # request to server
from zipfile import ZipFile                         # unzip file
from CNNClassifier import logger    #separate logger
from pathlib import Path            # 
from tqdm import tqdm
from CNNClassifier.entity import DataIngestionConfig
from CNNClassifier.utils import utils

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):           #init method
        

    def download_file(self):           # download the file method
        pass

    def get_updated_list_of_files(Self):
        pass

    def preprocess(self):
        pass

    def unzip_and_clean(self):
        pass