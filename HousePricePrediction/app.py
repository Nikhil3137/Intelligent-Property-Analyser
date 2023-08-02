from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__, template_folder='template')

# Load the machine learning model
model = joblib.load("C:/Users/Nikhil/PycharmProjects/TCSProject/HousePricePrediction/template/linear1.joblib")

@app.route("/")
def home():
    return render_template("home.html", predicted_price=None)

@app.route("/predict_price", methods=["POST"])
def predict_price():
    # Get the input data from the form
    area = request.form.get("area")
    bedrooms = request.form.get("bedroom")
    bathrooms = request.form.get("bathroom")
    stories = request.form.get("stories")
    mainroad = request.form.get("mainroad")
    guestroom = request.form.get("guestroom")
    basement = request.form.get("basement")
    airconditioning = request.form.get("airconditioning")
    hotwaterheating = request.form.get("hotwaterheating")
    noparking = request.form.get("noparking")
    furnishingstatus = request.form.get("furnishingstatus")
    preferredarea = request.form.get("preferredarea")

    # Validate the form inputs
    if None in [area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, airconditioning,
                hotwaterheating, noparking, furnishingstatus, preferredarea]:
        return render_template("home.html", predicted_price=None, error="Please fill all the required fields.")

    # Create a DataFrame from the input data
    input_data = pd.DataFrame({
        "area": [float(area)],
        "bedrooms": [int(bedrooms)],
        "bathrooms": [int(bathrooms)],
        "stories": [int(stories)],
        "mainroad": [int(mainroad)],
        "guestroom": [int(guestroom)],
        "basement": [int(basement)],
        "airconditioning": [int(airconditioning)],
        "hotwaterheating": [int(hotwaterheating)],
        "noparking": [int(noparking)],


        "furnishingstatus": [furnishingstatus],
        "preferredarea": [preferredarea]
    })

    # Perform one-hot encoding for categorical variables
    input_data_encoded = pd.get_dummies(input_data, columns=["furnishingstatus", "preferredarea"])

    # Generate predictions using the model
    price_prediction = model.predict(input_data_encoded).tolist()[0]
    price_in_crore = abs(price_prediction) / 100

    # Round the value to two decimal places
    rounded_price_in_crore = round(price_in_crore, 2)

    # Print the converted value
    print(rounded_price_in_crore)

    # Render the template with the predicted price
    return render_template("home.html", predicted_price=rounded_price_in_crore)

if __name__ == "__main__":
    app.run(debug=True)
