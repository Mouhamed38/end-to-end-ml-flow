import os
import pandas as pd
from mlProject import logger
from mlProject.entity.config_entity import DataTransformationConfig
from pathlib import Path
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config

        #ajouter du data cleaning ICI


    def train_test_split(self):
        data=pd.read_csv(self.config.data_path)

        train,test =train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)

        logger.info('Data splitted into train and test')
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
