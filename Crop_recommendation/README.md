# **Crop Recommendation based on Soil Moisture**

This project aims to recommend suitable crops based on soil moisture values using a Decision Tree Classifier algorithm. The prediction is made using a Python script (main.py) that utilizes the scikit-learn library for machine learning tasks. The user interface for interacting with the recommendation model is built using Streamlit, a popular Python library for creating web applications.

## **Project Description**

Agricultural practitioners often face the challenge of selecting the most appropriate crops for their soil conditions. Soil moisture is a crucial factor that significantly influences crop selection and yield. By harnessing machine learning techniques, this project provides a solution for recommending the most suitable crops based on the soil moisture levels.

The Decision Tree Classifier algorithm is chosen for its simplicity and interpretability. It learns from a set of training data containing soil moisture values and corresponding crop types. Once trained, the model can recommend crop types based on new soil moisture values provided by the user.

### We have Optimized our model with the Intel `sklearnex.patch()` for the model optimization.

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
git clone https://github.com/your-username/crop-recommendation.git
```

2. Navigate to the Project Directory:

```bash
cd crop-recommendation
```

3. Install Required Packages:

```bash
pip install -r requirements.txt
```

 4. Converting Pickle:

```bash
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

tf.saved_model.save(model, 'saved_model_path')
```

## **Interact with the Application:**

- Once the app is running, a browser window will open with the interface.
- Enter the soil moisture value into the input field and press Enter or click the **"Recommend"** button.
- The recommended crop based on the provided soil moisture value will be displayed.

## **Explore Recommendations:**

- Try different soil moisture values to observe how the recommended crop changes.
- The app updates the recommendation in real-time as you input different soil moisture values.

## **Close the Application:**

- To close the app, close the browser window or press Ctrl+C in the terminal.

## **Files**

- `main.py`: Python script containing the code for recommending crops based on soil moisture values.
- `predicted_values.xlsx`: Excel file containing soil moisture values for recommendation.
- `README.md`: Overview of the project, usage instructions, and file descriptions.
