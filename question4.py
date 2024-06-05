# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:45:47 2024

@author: User
"""

import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('prediction_model.sav', 'rb'))

def heart_predict(patient_data):
    np_input = np.asarray(patient_data)
    np_reshaped = np_input.reshape(1, -1)
    prediction = model.predict(np_reshaped)
    if prediction[0] == 0:
        return 'Healthy'
    else:
        return 'Heart Disease'

def main():
    st.set_page_config(page_title="Heart Prediction", layout="wide")
    
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        body {
            background-color: black;
            color: white;
        }
        .stApp {
            background-color: black;
            color: white;
        }
        .stNumberInput div, .stTextInput div, .stSelectbox div, .stButton button {
            background-color: white;
            color: black;
        }
        .stNumberInput div > label, .stTextInput div > label, .stSelectbox div > label, .stButton button {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("Heart Prediction System")

    sex_options = {"Male": 1, "Female": 0}
    cp_options = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Typical Angina": 2, "Asymptomatic": 3}
    fbs_options = {"True": 1, "False": 0}
    restecg_options = {"Normal": 0, "Abnormal": 1, "Ventricular hypertrophy": 2}
    exang_options = {"Yes": 1, "No": 0}
    slope_options = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
    thal_options = {"Unknown": 0, "Normal": 1, "Fixed Defect": 2, "Reversible Defect": 3}
    
    age = st.number_input("Age", min_value=0, max_value=120)
    sexView = st.selectbox("Select your Gender:", list(sex_options.keys()))
    sex = sex_options[sexView]
    cpView = st.selectbox("Chest Pain:", list(cp_options.keys()))
    cp = cp_options[cpView]
    trestbps = st.number_input("Resting Blood Pressure", min_value=0)
    chol = st.number_input("Serum Cholesterol in mg/dl", min_value=0)
    fbsView = st.selectbox("Fasting Blood Sugar >120mg/dl:", list(fbs_options.keys()))
    fbs = fbs_options[fbsView]
    restecgView = st.selectbox("Resting Electrocardiographic:", list(restecg_options.keys()))
    restecg = restecg_options[restecgView]
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0)
    exangView = st.selectbox("Exercise Induced Angina:", list(exang_options.keys()))
    exang = exang_options[exangView]
    oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, format="%.2f")
    slopeView = st.selectbox("Slope of peak exercise ST segment:", list(slope_options.keys()))
    slope = slope_options[slopeView]
    ca = st.number_input("Number of major vessels colored by fluoroscopy", min_value=0)
    thalView = st.selectbox("Status of your heart:", list(thal_options.keys()))
    thal = thal_options[thalView]

    diagnosis = ''
    
    # Button for prediction
    if st.button("Predict Heart Health"):
        diagnosis = heart_predict([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
    st.success(diagnosis)

if __name__ == '__main__':
    main()
