import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype #To check for the column whether it has numeric datatype or not
from sklearn.preprocessing import LabelEncoder,StandardScaler,MinMaxScaler,RobustScaler,MaxAbsScaler
from preprocessingScaling import preprocessing_scaling
debug= False
encode_debug=True
scale_debug=True
class Preprocessing:
    def __init__(self,df):
        self.df=df
        self.label_encoder=LabelEncoder()
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
        list_one_hot_encoded_columns=[]
        list_of_label_encoder_columns=[]
        dictionary_of_the_column_with_index={index:col for index,col in enumerate(self.df.columns) if self.df[col].dtype==object}
        #Below i  have displayed the values of the column with their index which are in a dataframe
        print(f"These are the columns in a dataframe :: {dictionary_of_the_column_with_index}")

        if encode_debug:
            for index,column in dictionary_of_the_column_with_index.items():
                print(f"At index {index} ,the column is:: {column}")

        for i in range(len(self.df.columns)-1):
            choose_encoding=int(input("Enter 1 for one hot encoding , 2 for label encoding and 3 for exiting :: "))
            if choose_encoding==3:
                break
            column_index=int(input("Enter the index of the column for encoding:: "))
            if choose_encoding==1:
                list_one_hot_encoded_columns.append(dictionary_of_the_column_with_index[column_index])
            elif choose_encoding==2:
                list_of_label_encoder_columns.append(dictionary_of_the_column_with_index[column_index])

        if encode_debug:
            print(f"This is the list of the one hot encoded columns :: {list_one_hot_encoded_columns}")
            print(f"This is the list of label encoded columns {list_of_label_encoder_columns}")
        #Now apply encoding  to the columns
        #Applied LabelEncoder 
        for val in list_of_label_encoder_columns:
            self.df[val]=self.label_encoder.fit_transform(self.df[val])
        #Applied OneHotEncoding
        self.df=pd.get_dummies(self.df,columns=list_one_hot_encoded_columns)
        print(f"top five values of the df :: \n {self.df.head()}")
        print("COMPLETED 3rd PREPROCESSING")
    
    def scale_numerical_features(self):
        #To remove the outliers we use scaling features
        #Four features will be provided
        print(f"ENTERED 4th PREPROCESSING")
        set_of_standard_scaling_column=set()
        set_of_min_max_scaling_column=set()
        set_of_robust_scaling_columns=set()
        set_of_max_absolute_scaling_columns=set()
        dict_of_column_with_their_index={index: col for index,col in enumerate(self.df.columns)}
        print(f"Below i have shown the column:: \n{dict_of_column_with_their_index}")
        for i in range(len(self.df.columns)-1):
            choose_scaling=int(input("Enter 1 for standard_scaling,2 for min_max_scaling,3 for robust_scaling ,4 for max_absolute_scaling and 5 for exiting :: "))
            if choose_scaling==5:
                break
            column_index=int(input("Enter the index of the column:: "))
            if choose_scaling==1:
                set_of_standard_scaling_column.add(dict_of_column_with_their_index[column_index])
            elif choose_scaling==2:
                set_of_min_max_scaling_column.add(dict_of_column_with_their_index[column_index])
            elif choose_scaling==3:
                set_of_robust_scaling_columns.add(dict_of_column_with_their_index[column_index])
            elif choose_scaling==4:
                set_of_max_absolute_scaling_columns.add(dict_of_column_with_their_index[column_index])
            #For each step i will display the list for all the scaling features

            if set_of_standard_scaling_column:
                print(f"set of column choosen for the Standatrd Scaling:: {set_of_standard_scaling_column}")
            if set_of_min_max_scaling_column:
                print(f"set of column choosen for the Min Max Scaling:: {set_of_min_max_scaling_column}")
            if set_of_robust_scaling_columns:
                print(f"set of column choosen for the Robust Scaling:: {set_of_robust_scaling_columns}")
            if set_of_max_absolute_scaling_columns: 
                print(f"set of column choosen for the Max Absolute Scaling:: {set_of_max_absolute_scaling_columns}")
        self.df=preprocessing_scaling(self.df,set_of_standard_scaling_column,set_of_min_max_scaling_column,set_of_robust_scaling_columns,set_of_max_absolute_scaling_columns)
        if scale_debug:
            print(f"First five values after scaling the features:: \n{self.df.head()}")

        print("COMPLETED 4th PREPROCESSING")
    