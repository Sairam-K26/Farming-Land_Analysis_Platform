**Plant Type Prediction based on Soil Moisture**


This project aims to predict the best-fitted plant type based on soil moisture values using a Decision Tree Classifier algorithm. The prediction is made using a Python script (main.py) that utilizes the scikit-learn library for machine learning tasks. The user interface for interacting with the prediction model is built using Streamlit, a popular Python library for creating web applications.

**Project Description**

Gardening and farming enthusiasts often face the challenge of selecting the most suitable plants for their soil conditions. Soil moisture is a critical factor that influences the growth and health of plants. By leveraging machine learning techniques, this project provides a solution for predicting the most suitable plant types based on the soil moisture levels.

The Decision Tree Classifier algorithm is chosen for its simplicity and interpretability. It learns from a set of training data containing soil moisture values and corresponding plant types. Once trained, the model can predict the plant type based on new soil moisture values provided by the user.

**Prerequisites**

Before running the application, ensure you have the following installed:

Python 3.x
Required Python packages (scikit-learn, numpy, streamlit, openpyxl)
You can install the required packages using pip:

```
pip install scikit-learn numpy streamlit openpyxl
```

**Usage**

Follow these steps to use the application:

Clone the Repository:

Clone the repository to your local machine:

```
git clone https://github.com/your-username/plant-type-prediction.git
```

Navigate to the Project Directory:

```
cd plant-type-prediction
```

**Install Required Packages:**

Install the required Python packages:

```
pip install -r requirements.txt
```

Run the Streamlit App:

Launch the Streamlit app:

```
streamlit run main.py
```

Interact with the Application:

Once the app is running, a browser window will open with the interface.

Enter the soil moisture value into the input field and press Enter or click the "Predict" button.

The predicted plant type based on the provided soil moisture value will be displayed.


**Explore Predictions:**

Try different soil moisture values to observe how the predicted plant type changes.
The app updates the prediction in real-time as you input different soil moisture values.

**Close the Application:**

To close the app, close the browser window or press Ctrl+C in the terminal.


**Files**

main.py: Python script containing the code for predicting plant types based on soil moisture values.

predicted_values.xlsx: Excel file containing soil moisture values to be predicted.

README.md: Overview of the project, usage instructions, and file descriptions.# soil-moisture-detection-and-plant-prediction
