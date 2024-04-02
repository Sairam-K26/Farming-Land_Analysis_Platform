
# **Crop Yield Prediction**

This project aims to predict crop yields based on various agricultural factors using machine learning techniques. The prediction is made using a Python script (`main.py`) that utilizes the scikit-learn library for machine learning tasks. The user interface for interacting with the prediction model is built using Streamlit, a popular Python library for creating web applications.

## **Project Description**

Predicting crop yields is crucial for agricultural planning, resource allocation, and decision-making. This project provides a solution for predicting crop yields based on factors such as rainfall, temperature, soil type, fertilizer usage, and crop variety.

The prediction model is built using machine learning algorithms, with regression techniques such as Random Forest Regression being chosen for their ability to handle complex relationships between input features and target variables. The model learns from a set of training data containing historical crop yields and corresponding agricultural factors. Once trained, the model can predict crop yields based on new agricultural data provided by the user.

### We have Optimized our model with the Intel `sklearnex.patch()` for model optimization.

## **Prerequisites**

- Python 3.x
- Required Python packages (scikit-learn, numpy, streamlit, openpyxl)

Install necessary packages:

```bash
pip install numpy streamlit openpyxl
```

For Intel-based Optimization:

```bash
pip install scikit-learn-intelex
```

## **Usage**

1. Clone the Repository:

```bash
git clone https://github.com/your-username/crop-yield-prediction.git
```

2. Navigate to the Project Directory:

```bash
cd crop-yield-prediction
```

3. Install Required Packages:

```bash
pip install -r requirements.txt
```

## **Converting this into pickle file**

```bash
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

predicted_value = model.predict(X_test)

```

## **Interact with the Application:**

- Once the app is running, a browser window will open with the interface.
- Enter the agricultural factors (e.g., rainfall, temperature, soil type, fertilizer usage) into the input fields and press Enter or click the **"Predict"** button.
- The predicted crop yield based on the provided agricultural data will be displayed.

## **Explore Predictions:**

- Try different combinations of agricultural factors to observe how the predicted crop yield changes.
- The app updates the prediction in real-time as you input different agricultural data.

## **Close the Application:**

- To close the app, close the browser window or press Ctrl+C in the terminal.

## **Files**

- `main.py`: Python script containing the code for predicting crop yields based on agricultural factors.
- `README.md`: Overview of the project, usage instructions, and file descriptions.
