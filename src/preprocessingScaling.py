"""
Arguments:
"""
from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler,MaxAbsScaler
def preprocessing_scaling(df,set_of_standard_scaling_column,set_of_min_max_scaling_column,set_of_robust_scaling_columns,set_of_max_absolute_scaling_columns):
    #Now i will make the object of all the scaling features
        standard_scaler=StandardScaler()
        min_max_scaler=MinMaxScaler()
        robust_scaler=RobustScaler()
        max_abs_scaler=MaxAbsScaler()
        if set_of_standard_scaling_column:
            df[list(set_of_standard_scaling_column)]=standard_scaler.fit_transform(df[list(set_of_standard_scaling_column)])
        if set_of_min_max_scaling_column:
            df[list(set_of_min_max_scaling_column)]=standard_scaler.fit_transform(df[list(set_of_min_max_scaling_column)])
        if set_of_robust_scaling_columns:
            df[list(set_of_robust_scaling_columns)]=standard_scaler.fit_transform(df[list(set_of_robust_scaling_columns)])
        if set_of_max_absolute_scaling_columns:
            df[list(set_of_max_absolute_scaling_columns)]=standard_scaler.fit_transform(df[list(set_of_max_absolute_scaling_columns)])

        return df