import streamlit as st
import pickle
import numpy as np

lung_model = pickle.load(open('C:/Users/riyab/Desktop/lung_cancer/lung_cancer.sav', 'rb'))


st.title('Lung Cancer Prediction')

# Input Features
col1, col2, col3= st.columns(3)

with col1:
    Air_Pollution = st.slider("Air Pollution", 1.0, 8.0, 4.0)
    Alcohol_use = st.slider("Alcohol Use", 1.0, 8.0, 4.0)
    Dust_Allergy = st.slider("Dust Allergy", 1.0, 8.0, 4.0)
    Genetic_Risk = st.slider("Genetic Risk", 1.0, 7.0, 4.0)
with col2:
    Balanced_Diet = st.slider("Balanced Diet", 1.0, 7.0, 4.0)
    Obesity = st.slider("Obesity", 1.0, 8.0, 4.0)
    Smoking = st.slider("Smoking", 1.0, 8.0, 4.0)
    Passive_Smoker = st.slider("Passive Smoker", 1.0, 8.0, 4.0)
with col3:
    Coughing_of_Blood = st.slider("Coughing of Blood", 1.0, 9.0, 4.0)
    Fatigue = st.slider("Fatigue", 1.0, 9.0, 4.0)
    Shortness_of_Breath = st.slider("Shortness of Breath", 1.0, 9.0, 4.0)
    Snoring = st.slider("Snoring", 1.0, 7.0, 4.0)
# Additional features
# with col4:


# Prediction button
if st.button("Lung Cancer Test Result"):
    input_data = [
        [Air_Pollution, Alcohol_use, Dust_Allergy, Genetic_Risk,
         Balanced_Diet, Obesity, Smoking, Passive_Smoker,
         Coughing_of_Blood, Fatigue, Shortness_of_Breath, Snoring]
    ]

    lung_prediction = lung_model.predict(input_data)
    if lung_prediction[0] == 0:
        lung_diagnosis = "You have lung cancer."
    elif lung_prediction[0] == 1:
        lung_diagnosis = "You don't have any lung issues."
    elif lung_prediction[0] == 2:
        lung_diagnosis = "You can have lung issues."

    st.success(lung_diagnosis)













# import numpy as np
# import pickle
# import streamlit as st
#
# lung_model = pickle.load(open('C:/Users/riyab/Desktop/lung_cancer/lung_cancer.sav','rb'))
#
# st.title('lung Cancer prediction')
# col1, col2, col3 = st.columns(3)
#
# with col1:
#     Air_Pollution  = st.text_input("Air_Pollution")
#
# with col2:
#     Alcohol_use = st.text_input("Alcohol_use ")
#
# with col3:
#     Dust_Allergy  = st.text_input("Dust_Allergy")
#
# with col1:
#     Genetic_Risk  = st.text_input("Genetic_Risk")
#
# with col2:
#     Balanced_Diet = st.text_input("Balanced_Diet")
#
# with col3:
#     Obesity = st.text_input("Obesity ")
#
# with col1:
#     Smoking = st.text_input("Smoking")
#
# with col2:
#     Passive_Smoker = st.text_input("Passive_Smoker")
#
# with col3:
#     Coughing_of_Blood = st.text_input("Coughing_of_Blood")
#
# with col1:
#     Fatigue = st.text_input("Fatigue")
#
# with col2:
#     Shortness_of_Breath = st.text_input("Shortness_of_Breath")
#
# with col3:
#     Snoring = st.text_input("Snoring")
#
#     # code for Prediction
# lung_diagnosis = " "
#
#     # creating a button for Prediction
#
#
# if st.button("lung Cancer Test Result"):
#     input_data = [
#         [float(Air_Pollution), float(Alcohol_use), float(Dust_Allergy), float(Genetic_Risk),
#          float(Balanced_Diet), float(Obesity), float(Smoking), float(Passive_Smoker),
#          float(Coughing_of_Blood), float(Fatigue), float(Shortness_of_Breath), float(Snoring)]
#     ]
#
#     lung_prediction = lung_model.predict(input_data)
#     if (lung_prediction[0] == 0):
#         lung_diagnosis = "Sorry! You have lung cancer."
#     if (lung_prediction[0] == 1):
#             lung_diagnosis = "Hurrah! You dont have any lung issues."
#     if (lung_prediction[0] == 2):
#         lung_diagnosis = "Sorry! You can have lung issues ."
#
# st.success(lung_diagnosis)

