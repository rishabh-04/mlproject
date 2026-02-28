# any functnality written in common way , used in entire application ... save my model in cloud etc

import os
import sys
import dill
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
# convert this object into pickle file at file location
def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)  
            
    except Exception as e:
        raise CustomException(e, sys)      
#reports of all the models
def evaluate_models(X_train,y_train,X_test,y_test,models,params):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            para = params[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train) #training the model


            y_train_pred = model.predict(X_train) #predicting the train data
            y_test_pred = model.predict(X_test) #predicting the test data
            train_model_score = r2_score(y_train,y_train_pred) #calculating r2 score for train data
            test_model_score = r2_score(y_test,y_test_pred) #calculating r2 score for test data
            report[list(models.keys())[i]] = test_model_score #storing the r2 score in report dictionary
        return report
    
    except Exception as e:
        raise CustomException(e, sys)