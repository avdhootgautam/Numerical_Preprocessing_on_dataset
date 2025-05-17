#This is the entry point for the project
import numpy as np
import pandas as pd
from loadDataset import load_dataset 
from preprocessing import Preprocessing
import configparser#declared fro reading the file
debug=True

def main():
    #Here only initialize the configparser
    config=configparser.ConfigParser()
    config.read("config.ini")

    print("IN MAIN")
    train_dataset_path=config['DATASET']["train_dataset_path"]
    df=load_dataset(train_dataset_path)
    print("LOADING OF DATA COMPLETED")

    print("STARTING OF PREPROCESSING IN MAIN")
    preprocess1=Preprocessing(df)
    preprocess1.description_info_head_dataframe()
    #target_column="income_>50K"
    target_column=input(f"Enter the target column(string)::")
    preprocess1.handle_missing_values(target_column) 
    preprocess1.encoding_columns()
    preprocess1.scale_numerical_features()
    print("END OF PREPROCESSING IN MAIN")
    
if __name__=="__main__":
    main()
