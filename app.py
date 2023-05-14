from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the machine learning model
model = joblib.load("C:/Users/Nikhil/PycharmProjects/TCSProject/HousePricePrediction/template/rid.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict_price", methods=["POST"])
def predict_price(inputs):
    # Get the input data from the form
    area = request.form.get("area")
    bedrooms = request.form.get("bedrooms")
    bathrooms = request.form.get("bathrooms")
    mainroad = request.form.get("mainroad")
    guestroom = request.form.get("guestroom")
    airconditioning = request.form.get("airconditioning")
    hotwaterheating = request.form.get("hotwaterheating")
    parking = request.form.get("parking")
    furnishingstatus = request.form.get("furnishingstatus")
    preferredarea = request.form.get("preferredarea")

    # Put the input data into a dictionary
    inputs = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "airconditioning": airconditioning,
        "hotwaterheating": hotwaterheating,
        "parking": parking,
        "furnishingstatus": furnishingstatus,
        "preferredarea": preferredarea
    }

    # Generate predictions using the model
    predictions = predict_price(inputs)

    # Return the predictions as a JSON object
    return jsonify(predictions)