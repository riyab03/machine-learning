import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

#loading saved models
dia_model = pickle.load(open('C:/Users/riyab/Desktop/PROJECTS-GIT/medical_proj/saved_models/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('C:/Users/riyab/Desktop/PROJECTS-GIT/medical_proj/saved_models/heart_model.sav', 'rb'))
kidney_model = pickle.load(open('C:/Users/riyab/Desktop/PROJECTS-GIT/medical_proj/saved_models/kidney_model.sav', 'rb'))
lung_model = pickle.load(open('C:/Users/riyab/Desktop/PROJECTS-GIT/medical_proj/saved_models/lung_data.sav', 'rb'))


#sidebar
with st.sidebar:
    selected=option_menu('Multiple disease',
                         ['diabetes prediction',
                          'heart prediction',
                          'kidney prediction',
                          'Lung cancer prediction'],
                         default_index=0)

if (selected == 'diabetes prediction'):
    st.title('diabetes prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Glucose Level")

    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")

    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")

    with col2:
        Insulin = st.text_input("Insulin Level")

    with col3:
        BMI = st.text_input("BMI Value")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")

    with col2:
        Age = st.text_input("Age of the Person")

    # code for Prediction
    diab_diagnosis = " "

    # creating a button for Prediction

    if st.button("Diabetes Test Result"):
        diab_prediction = dia_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 0):
            diab_diagnosis = "Hurrah! You have no Diabetes."
        else:
            diab_diagnosis = "Sorry! You have Diabetes."

    st.success(diab_diagnosis)




if (selected == 'heart prediction'):
    st.title('Heart prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age")

    with col2:
        sex = st.number_input("Sex")

    with col3:
        cp = st.number_input("Chest Pain Types")

    with col1:
        trestbps = st.number_input("Resting Blood Pressure")

    with col2:
        chol = st.number_input("Serum Cholestoral in mg/dl")

    with col3:
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl")

    with col1:
        restecg = st.number_input("Resting Electrocardiographic Results")

    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved")

    with col3:
        exang = st.number_input("Exercise Induced Angina")

    with col1:
        oldpeak = st.number_input("ST Depression induced by Exercise")

    with col2:
        slope = st.number_input("Slope of the peak exercise ST Segment")

    with col3:
        ca = st.number_input("Major vessels colored by Flourosopy")

    with col1:
        thal = st.number_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")

    # code for Prediction
    heart_diagnosis = " "

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 0):
            heart_diagnosis = "Hurrah! Your Heart is Good."
        else:
            heart_diagnosis = "Sorry! You have Heart Problem."

    st.success(heart_diagnosis)


if (selected == 'kidney prediction'):
    st.title('Kidney prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        al = st.text_input("al")

    with col2:
        rbc = st.text_input("rbc(1/0)")

    with col3:
        pc = st.text_input("pc(1/0)")

    with col1:
        bgr = st.text_input("bgr")

    with col2:
        bu = st.text_input("bu")

    with col3:
        sc = st.text_input("sc")

    with col1:
        sod = st.text_input("sod")

    with col2:
        hemo = st.text_input("hemo")

    with col3:
        pcv = st.text_input("pcv")

    with col1:
        rc = st.text_input("rc")

    with col2:
        htn = st.text_input("htn(1/0)")

    # Convert the input values to numeric
    if any(value == '' for value in [al, rbc, pc, bgr, bu, sc, sod, hemo, pcv, rc, htn]):
        st.error("Please provide values for all input fields.")
    else:
        # Convert the input values to a numeric array
        input_data = np.array([[float(al), float(rbc), float(pc), float(bgr), float(bu), float(sc),
                                float(sod), float(hemo), float(pcv), float(rc), float(htn)]], dtype=float)

    # code for Prediction
    kidney_diagnosis = " "

    # creating a button for Prediction
    if st.button("Kidney Test Result"):
        kidney_prediction = kidney_model.predict(input_data)

        if kidney_prediction[0] == 0:
            kidney_diagnosis = "Hurrah! You are predicted to have no Kidney issues."
        else:
            kidney_diagnosis = "Sorry! You are predicted to have Kidney issues."

    st.success(kidney_diagnosis)


if (selected == 'Lung cancer prediction'):
    st.title('Lung cancer prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Air_Pollution = st.text_input("Air Pollution")

    with col2:
        Alcohol_use = st.text_input("Alcohol use")

    with col3:
        Dust_Allergy = st.text_input("Dust Allergy")

    with col1:
        Genetic_Risk = st.text_input("Genetic Risk")

    with col2:
        Balanced_Diet = st.text_input("Balanced Diet")

    with col3:
        Obesity = st.text_input("Obesity")

    with col1:
        Smoking = st.text_input("Smoking")

    with col2:
        Passive_Smoker = st.text_input("Passive Smoker")

    with col3:
        Coughing_of_Blood = st.text_input("Coughing of Blood")

    with col1:
        Fatigue = st.text_input("Fatigue")

    with col2:
        Shortness_of_Breath = st.text_input("Shortness of Breath")
        
    with col3:
        Snoring = st.text_input("Snoring")
        
    # Convert the input values to numeric
    if any(value == '' for value in [Air_Pollution, Alcohol_use, Dust_Allergy, Genetic_Risk, Balanced_Diet, Obesity, Smoking, Passive_Smoker, Coughing_of_Blood, Fatigue, Shortness_of_Breath,Snoring]):
        st.error("Please provide values for all input fields.")
    else:
        # Convert the input values to a numeric array
        input_data = np.array([[float(Air_Pollution), float(Alcohol_use), float(Dust_Allergy), float(Genetic_Risk), float(Balanced_Diet), float(Obesity),
                                float(Smoking), float(Passive_Smoker), float(Coughing_of_Blood), float(Fatigue), float(Shortness_of_Breath),float(Snoring)]], dtype=float)

    # code for Prediction
    lung_diagnosis = " "

    # creating a button for Prediction
    if st.button("Lung cancer Test Result"):
        lung_prediction = lung_model.predict(input_data)

        if lung_prediction[0] == 0:
            lung_diagnosis = "Sorry! You are predicted to have Lung issues."
        elif lung_prediction[0] == 1:
            lung_diagnosis = "Hurrah! You are predicted to have no Lung issues."
        else:
            lung_diagnosis = "Sorry! You can have Lung issues.Take Care"

    st.success(lung_diagnosis)

# Air Pollution
















