#This is the entry point for the project
import numpy as np
import pandas as pd
from loadDataset import load_dataset 
from preprocessing import Preprocessing
debug=True

def main():
    train_dataset_path="../dataset/train.csv"
    df=load_dataset(train_dataset_path)
    
    preprocess1=Preprocessing(df)
    preprocess1.description_info_head_dataframe()
    #target_column="income_>50K"
    target_column=input(f"Enter the target column(string)::")
    preprocess1.handle_missing_values(target_column)
    
if __name__=="__main__":
    main()
