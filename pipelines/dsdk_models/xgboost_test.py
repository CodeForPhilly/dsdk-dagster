from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import _pickle as cPickle

with open(f'xgboost', 'rb') as f:
    model_r = cPickle.load(f)
        
data = loadtxt('test_data.csv', delimiter=",")

def diabetes_predict(params):
    pred = model_r.predict(params)
    predictions = [round(value) for value in pred]
    return predictions
    
predict = diabetes_predict(data)    