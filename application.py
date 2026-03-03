#.py file for deployement purpose
from flask import Flask, request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
application=Flask(__name__) #gives entry point in creating
app = application

print("App starting")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html') #this has simple input data fields that we need to give to the model
    else:
        #post req?
        #predict pipeline class will be created over here
        data = CustomData(
         gender=request.form.get('gender'), 
         race_ethnicity=request.form.get('ethnicity'),
         parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            writing_score=float(request.form.get('writing_score')),
            reading_score=float(request.form.get('reading_score'))

        )
        pred_df = data.get_data_as_dataframe() #this will convert the input data into dataframe
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df) #this will give the prediction result
        return render_template('home.html', results=results[0]) #this will show the result in the home.html page list format
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
    #while deploying well remove debug = true