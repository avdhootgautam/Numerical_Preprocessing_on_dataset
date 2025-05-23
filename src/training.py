import configparser
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
class Train:
    def __init__(self,splitted_data):
        self.splitted_data=splitted_data
        self.config=configparser.ConfigParser()
        self.config.read("config.ini")
    def chose_algorithm(self):
        pass