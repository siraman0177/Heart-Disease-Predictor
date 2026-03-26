#  Heart Disease Prediction App

##  Overview

This is a Machine Learning web application built using **Streamlit** that predicts the risk of heart disease based on user input.

The model uses a **K-Nearest Neighbors (KNN)** algorithm trained on heart-related medical data to classify whether a person is at **high risk or low risk** of heart disease.


##  Features

* Interactive UI using Streamlit
* Real-time prediction
* Uses trained ML model (`.pkl` files)
* User-friendly input sliders and dropdowns
* Instant result display



##  Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Joblib



##  Project Structure

```
heart-disease-app/
│
├── app.py                # Main Streamlit app
├── knn_heart.pkl        # Trained ML model
├── scaler.pkl           # Data scaler
├── column.pkl           # Expected input columns
├── heart.csv            # Dataset (optional)
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## How It Works

1. User enters health-related details (age, cholesterol, BP, etc.)
2. Input data is processed and formatted
3. Data is scaled using a pre-trained scaler
4. KNN model predicts the risk
5. Result is displayed on the screen


