#This is the entry point for the project
import numpy as np
import pandas as pd
from loadDataset import load_dataset 
from preprocessing import Preprocessing
from splitting import Split
from training import Train
import configparser#declared fro reading the file
import os
debug=True

def main():
    #Here only initialize the configparser
    config=configparser.ConfigParser()
    config.read("config.ini")
    if not os.path.exists("../output/preprocessed_df.csv"):
        print("IN MAIN")
        train_dataset_path=config['DATASET']["train_dataset_path"]
        df=load_dataset(train_dataset_path)
        print("LOADING OF DATA COMPLETED")

        print("STARTING OF PREPROCESSING IN MAIN")
        preprocess1=Preprocessing(df)
        preprocess1.description_info_head_dataframe()
        print("target column has been taken")
        target_column=str(config["MAIN"]["target_column"])

        preprocess1.handle_missing_values(target_column) 
        preprocess1.encoding_columns()
        preprocess1.scale_numerical_features()#Here i got the final df after preprocessing
        preprocess1.saving_preprocessed_data()
        print("END OF PREPROCESSING IN MAIN")
        print("-------------------------------------------")
        print("SPLITTING OF DATASET IN MAIN")
    # Created one new dataframe
    preprocessed_df=pd.read_csv("../output/preprocessed_df.csv")
    split1=Split(preprocessed_df)
    splitted_data=split1.split_data()#It's a list which contain x_train,x_test,y_train,y_test
    print("SPLITTING COMPLETED IN MAIN")
    print("-------------------------------------------")
    print("TRAINING STARTED IN MAIN")
    train1=Train(splitted_data)

if __name__=="__main__":
    main()
