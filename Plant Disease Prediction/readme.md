# **Plant Disease Detection System**


This repository contains the code and necessary files for a Plant Disease Detection System. The system is designed to identify diseases in plants using image processing techniques and machine learning algorithms.

## **Requirements**

Python 3.x


TensorFlow


Keras


OpenCV


NumPy


Matplotlib


Flutter(for web application, if applicable)


You can download them using the following commands:

```
pip install  numpy matplotlib tensorflow keras opencv 
```

For Intel based Optimisation 

```
!pip install scikit-learn-intelex
```

## **Usage**

**Clone the Repository:**



```
git clone https://github.com/your-username/Plant-Disease-Prediction.git
```

**Install dependencies:**


```
pip install -r requirements.txt
```

**Dataset**

The dataset used in this project can be found [here](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset).

**Training the Model**

Train the model with the dataset given 



## **Converting this into pickle file**

```bash
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

predicted_value = model.predict(X_test)

```
