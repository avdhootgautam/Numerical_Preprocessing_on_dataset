import pandas as pd
def load_dataset(train_dataset_path):
    df=pd.read_csv(train_dataset_path)
    return df