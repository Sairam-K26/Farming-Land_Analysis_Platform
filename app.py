from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained Naive Bayes model
with open("NBClassifier.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load crop prices and input costs (you need to define these based on your data)
crop_prices = {
    "rice": 1000,
    "maize": 800,
    "chickpea": 1200,
    # Add more crops and prices as needed
}

input_costs_per_acre = {
    "rice": {
        "seed": 50,
        "fertilizer": 100,
        "pesticides": 80,
        # Add more input costs as needed
    },
    "maize": {
        "seed": 40,
        "fertilizer": 80,
        "pesticides": 70,
        # Add more input costs as needed
    },
    "chickpea": {
        "seed": 60,
        "fertilizer": 120,
        "pesticides": 90,
        # Add more input costs as needed
    },
    # Add more crops and input costs as needed
}


# Function to predict the crop
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
    predicted_labels = model.predict(input_data)

    # Get top three predicted labels
    top_predictions = []
    for label in np.argsort(-model.predict_proba(input_data))[0][:3]:
        top_predictions.append(model.classes_[label])

    return top_predictions


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Retrieve input values from the form
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # Round up the floating-point values
        N = round(N)
        P = round(P)
        K = round(K)
        temperature = round(temperature, 2)
        humidity = round(humidity, 2)
        ph = round(ph, 2)
        rainfall = round(rainfall, 2)

        # Predict the crop
        predicted_crops = predict_crop(N, P, K, temperature, humidity, ph, rainfall)

        # Create a list of tuples containing crops and their priorities
        predictions_with_priority = [
            (crop, i + 1) for i, crop in enumerate(predicted_crops)
        ]

        # Redirect to the crop selection page with the prediction results as URL parameters
        return redirect(
            url_for("select_crop", predictions_with_priority=predictions_with_priority)
        )


@app.route("/select_crop", methods=["GET", "POST"])
def select_crop():
    if request.method == "GET":
        # Retrieve prediction results from URL parameters
        predictions_with_priority = request.args.get("predictions_with_priority")
        return render_template(
            "select_crop.html", predictions_with_priority=predictions_with_priority
        )

    elif request.method == "POST":
        # Retrieve selected crop and acreage from the form
        selected_crop = request.form["crop"]
        acreage = float(request.form["acreage"])

        # Calculate total input costs based on acreage and input costs per acre for the selected crop
        total_input_costs = sum(input_costs_per_acre[selected_crop].values()) * acreage

        # Calculate total price for the land based on crop price and acreage
        total_price = crop_prices[selected_crop] * acreage

        # Calculate profit
        profit = total_price - total_input_costs

        # Render the price calculation result template
        return render_template(
            "price_calculation_result.html",
            selected_crop=selected_crop,
            acreage=acreage,
            total_input_costs=total_input_costs,
            total_price=total_price,
            profit=profit,
        )


if __name__ == "__main__":
    app.run(debug=True)
