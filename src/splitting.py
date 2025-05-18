from sklearn.model_selection import train_test_split
import configparser

class Split():
    def __init__(self,df):
        self.df=df
        self.config=configparser.ConfigParser()
        self.config.read("config.ini")
    def split_data(self):
        X=self.df.drop(str(self.config["MAIN"]["target_column"]),axis=1)
        Y=self.df[str(self.config["MAIN"]["target_column"])]
        x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=float(self.config["SPLITTING"]["test_size"]),random_state=int(self.config["SPLITTING"]["random_state"]))
        print(f"This is the x_train after splitting {x_train.shape}")
        print(f"This is the x_test after splitting {x_test.shape}")
        print(f"This is the y_train after splitting {y_train.shape}")
        print(f"This is the y_test after splitting {y_test.shape}")