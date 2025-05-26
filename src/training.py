import configparser
import pickle
import os
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
class Train:
    def __init__(self,splitted_data):
        self.splitted_data=splitted_data
        self.config=configparser.ConfigParser()
        self.config.read("config.ini")
    def chose_algorithm(self):
        dict_chose_algorithm={}
        dict_chose_algorithm[0]=LogisticRegression()
        dict_chose_algorithm[1]=RandomForestClassifier()
        dict_chose_algorithm[2]=GradientBoostingClassifier()
        dict_chose_algorithm[3]=DecisionTreeClassifier()
        print(f"These are the model we are using:: {dict_chose_algorithm}")
        model_dir="../output/model"
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)

        for name,model in dict_chose_algorithm.items():
            model.fit(self.splitted_data[0],self.splitted_data[2])
            model_path=os.path.join(model_dir,f"trained_model_{name}.pkl")
            with open(model_path,"wb") as file:
                pickle.dump(model,file)
            y_pred=model.predict(self.splitted_data[1])
            acc=accuracy_score(self.splitted_data[3],y_pred)
            print(f"{name}: Accuracy = {acc:.2f}")
            