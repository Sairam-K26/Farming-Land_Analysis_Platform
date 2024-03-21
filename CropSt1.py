import streamlit as st
import pickle

# Load the trained Naive Bayes model
with open('NBClassifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to predict the crop
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
    predicted_crop = model.predict(input_data)
    return predicted_crop[0]

# Streamlit web app
def main():
    st.title('Crop Prediction App')

    # User input for features
    N = st.number_input('Nitrogen (N)')
    P = st.number_input('Phosphorus (P)')
    K = st.number_input('Potassium (K)')
    temperature = st.number_input('Temperature')
    humidity = st.number_input('Humidity')
    ph = st.number_input('pH')
    rainfall = st.number_input('Rainfall')

    # Predict the crop
    if st.button('Predict Crop'):
        predicted_crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
        st.success(f'Predicted Crop: {predicted_crop}')

if __name__ == '__main__':
    main()
