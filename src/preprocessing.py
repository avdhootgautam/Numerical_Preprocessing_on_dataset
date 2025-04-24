import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype #To check for the column whether it has numeric datatype or not
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
debug= False
class Preprocessing:
    def __init__(self,df):
        self.df=df

    def description_info_head_dataframe(self):
        print(f"ENTERED 1ST PREPROCESSING")
        stats_df=int(input(f"Enter 1 for the [quick stats of the numerical column in a dataframe] else 0:: "))
        if stats_df==1:
            print(f"Stats for the numerical column of the dataframe is ::\n{self.df.describe()}")
        else:
            print(f"NO DESCRIPTION")
        summary_df=int(input(f"Enter 1 for the [concise summary of the dataframe ] else 0:: "))
        if summary_df==1:
            print(f"\n {self.df.info()}")
        else:
            print(f"NO SUMMARY")
        head_df=int(int(input("Enter 1 for the [head of the dataframe] else 0:: ")))
        if head_df==1:
            print(f"Top five values of the dataframe are ::\n {self.df.head()}")
        else:
            print(f"NO TOP VALUES")
        print(f"1st PREPROCESSING COMPLETED")
        
    def handle_missing_values(self,target_column):
        print(f"ENTERED 2nd PREPROCESSING")
        #Below , directly removed the rows having NA value
        if debug:
            print(f"TRUE if there is null value and FALSE if there is no null value ::{self.df["age"].isnull().any()}")
        remove_na=int(input("Enter 1 for removing all the rows with na values(recommnded 1 for more null values):: "))
        if remove_na==1:
            self.df.dropna(axis=0,inplace=True)
        else:
            print(f"NO ROWS REMOVED WITH NA VALUES")
        handle_missing_values_with_mean_median=int(input("Enter 1 if you want to handle the missing values with mean and median:: "))
        if handle_missing_values_with_mean_median==1:
            
            total_number_of_columns=len(self.df.columns)-1#I have decraesed one because i don't want to do any  change in result column
            list_of_total_number_of_columns={index:col for index,col in enumerate(self.df.columns) if col!=target_column and is_numeric_dtype(self.df[col])}
            for index,value in list_of_total_number_of_columns.items():
                    print(f"Column at index {index} is {value}")

            #Below made a list of dictionary for the columns in which i want to change the column
            list_of_dict_of_column_name_to_change=[]
            number_of_column=int(input("Enter the total number of column to change:: "))
            for i in range(number_of_column):
                index=int(input(f"Enter the index for the column you want to change:: "))
                mea_or_med=int(input("Enter 0 for [mean] and 1 for [median]:: "))
                list_of_dict_of_column_name_to_change.append({index:mea_or_med})
            print(f"dict is :: {list_of_dict_of_column_name_to_change}")

            for val in list_of_dict_of_column_name_to_change:
                for index,value in val.items():
                    column_name=self.df.columns[index]
                    if debug:
                        print(f"The column name is {column_name}")
                    if value == 0:
                        self.df[column_name] = self.df[column_name].fillna(self.df[column_name].mean())
                    elif value == 1:
                        self.df[column_name] = self.df[column_name].fillna(self.df[column_name].median())
        elif handle_missing_values_with_mean_median==0:
            print(f"MISSING VALUES HAS NOT BEEN HANDLED")
        print(f"Top five values of the DataFrame::\n{self.df.head()}")
        if debug:
             print(f"TRUE if there is null value and FALSE if there is no null value ::{self.df["age"].isnull().any()}")
        print(f"2nd PREPROCESSING COMPLETED ")
    
    def encoding_columns(self):
        print(f"ENTERED 3rd PREPROCESSING")

