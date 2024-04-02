# **Surface Water Level Predictor**

This project aims to predict surface water levels based on various environmental factors using machine learning techniques. The prediction is made using a Python script (`main.py`) that utilizes the scikit-learn library for machine learning tasks. The user interface for interacting with the prediction model is built using Streamlit, a popular Python library for creating web applications.

## **Project Description**

Monitoring surface water levels is essential for various applications such as flood forecasting, water resource management, and environmental conservation. This project provides a solution for predicting surface water levels based on environmental variables such as rainfall, temperature, humidity, and land cover type.
![WhatsApp Image 2024-04-02 at 15 31 39_94db76be](https://github.com/Sairam-K26/Farming-Land_Analysis_Platform/assets/125663843/b87cde1f-6b78-4156-883f-29a0391c5715)


The prediction model is built using machine learning algorithms, with the Random Forest Regressor being chosen for its ability to handle complex relationships between input features and target variables. The model learns from a set of training data containing historical surface water levels and corresponding environmental factors. Once trained, the model can predict surface water levels based on new environmental data provided by the user.

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
git clone https://github.com/your-username/surface-water-level-predictor.git
```

2. Navigate to the Project Directory:

```bash
cd surface-water-level-predictor
```

3. Install Required Packages:

```bash
pip install -r requirements.txt
```

## **Run the Streamlit App:**

```bash
streamlit run main.py
```

## **Interact with the Application:**

- Once the app is running, a browser window will open with the interface.
- Enter the environmental factors (e.g., rainfall, temperature, humidity) into the input fields and press Enter or click the **"Predict"** button.
- The predicted surface water level based on the provided environmental data will be displayed.

## **Explore Predictions:**

- Try different combinations of environmental factors to observe how the predicted surface water level changes.
- The app updates the prediction in real-time as you input different environmental data.

## **Close the Application:**

- To close the app, close the browser window or press Ctrl+C in the terminal.

## **Files**

- `main.py`: Python script containing the code for predicting surface water levels based on environmental factors.
- `README.md`: Overview of the project, usage instructions, and file descriptions.
