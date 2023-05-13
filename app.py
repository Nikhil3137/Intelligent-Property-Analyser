from flask import Flask, render_template, request
import pickle
import joblib

import json
app = Flask(__name__)
# Load the machine learning model
model = joblib.load(open('C:/Users/Nikhil/PycharmProjects/TCSProject/HousePricePrediction/template/model1.joblib','rb'))

@app.route('/')
def home():
	return render_template('index.html')
@app.route('/predict', methods=['GET','POST'])
def predict():
    # Get the form data
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    parking = int(request.form['parking'])
    furnishingstatus = request.form['furnishingstatus']
    area = int(request.form['area'])

    # Convert furnishing status to numerical value
    if furnishingstatus == 'Unfurnished':
        furnishingstatus_num = 0
    elif furnishingstatus == 'Semi-Furnished':
        furnishingstatus_num = 1
    else:
        furnishingstatus_num = 2

    # Make a prediction using the model
    prediction = model.predict([[bedrooms, bathrooms, parking, furnishingstatus_num, area]])

    # Render the prediction on a new page
    return render_template('result.html', prediction=prediction[0])
