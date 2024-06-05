# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:45:47 2024

@author: User
"""

import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('Prediction_model.sav', 'rb'))

def heart_predict(patient_data):
    np_input = np.asarray(patient_data)
    np_reshaped = np_input.reshape(1, -1)
    prediction = model.predict(np_reshaped)
    if prediction[0] == 0:
        return 'Healthy'
    else:
        return 'Heart Disease'

def main():
    st.set_page_config(page_title="Heart Prediction", layout="centered")
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #18191A;
            color: #E4E6EB;
        }
        .stNumberInput, .stTextInput, .stSelectbox, .stButton {
            margin-bottom: 1rem;
        }
        .stNumberInput > div, .stTextInput > div, .stSelectbox > div, .stButton > button {
            background-color: #242526;
            color: #E4E6EB;
            border: 1px solid #3A3B3C;
            border-radius: 0.25rem;
        }
        .stNumberInput > div > label, .stTextInput > div > label, .stSelectbox > div > label {
            color: #B0B3B8;
        }
        .stButton button {
            background-color: #3A3B3C;
            border: none;
            padding: 0.5rem 1rem;
            color: #E4E6EB;
            border-radius: 0.25rem;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #4E4F50;
        }
        .stSuccess {
            background-color: #28a745 !important;
            color: #fff !important;
            font-size: 1rem;
            border-radius: 0.25rem;
            padding: 0.5rem;
            text-align: center;
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
    sex = st.selectbox("Gender:", list(sex_options.keys()))
    sex = sex_options[sex]
    cp = st.selectbox("Chest Pain:", list(cp_options.keys()))
    cp = cp_options[cp]
    trestbps = st.number_input("Resting Blood Pressure bps", min_value=0)
    chol = st.number_input("Cholesterol in mg/dl", min_value=0)
    fbs = st.selectbox("Blood Sugar >120mg/dl:", list(fbs_options.keys()))
    fbs = fbs_options[fbs]
    restecg = st.selectbox("Resting ECG:", list(restecg_options.keys()))
    restecg = restecg_options[restecg]
    thalach = st.number_input("Maximum Heart Rate", min_value=0)
    exang = st.selectbox("Exercise Induced Angina:", list(exang_options.keys()))
    exang = exang_options[exang]
    oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, format="%.2f")
    slope = st.selectbox("Slope", list(slope_options.keys()))
    slope = slope_options[slope]
    ca = st.number_input("Number of major blood vessels", min_value=0)
    thal = st.selectbox("Status:", list(thal_options.keys()))
    thal = thal_options[thal]

    diagnosis = ''
    
    if st.button("Predict Heart Health"):
        diagnosis = heart_predict([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
    if diagnosis:
        st.success(diagnosis)

if __name__ == '__main__':
    main()
