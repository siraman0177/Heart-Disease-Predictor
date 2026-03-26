import streamlit as st
import pandas as pd 
import joblib
model= joblib.load('knn_heart.pkl')
scaler= joblib.load('scaler.pkl')
expected_column= joblib.load('column.pkl')

st.title("Heart stroke prediction")
st.markdown("provide the following details ")

age=st.slider("Age",18,100,40)
sex=st.selectbox("SEX",['M',"F"])
chest_pain=st.selectbox("chest pain type",['ATA','NAP','TA','ASY'])
resting_bP=st.number_input("resting blood pressure(mm hg)",80,200,120)
cholesterol=st.number_input('cholestrol(mg/dl)',100,600,200)
fastingbs=st.selectbox("fasting blood sugar >120 mg/dl",[0,1])
resting_ecg=st.selectbox("resting ECG",["Normal","ST","LVH"])
max_hr=st.slider("max heart rate")
exercise_angina=st.selectbox("exercise-induced angina",['Y','N'])
old_peak = st.slider("Old Peak (ST depression)", 0.0, 6.0, 1.0)
st_slope=st.selectbox("ST slope",["Up","Flat","Down"])

if st.button("predict"):
    raw_input={
        "Age":age,
        'RestingBP':resting_bP,
        'Cholestetol':cholesterol,
        'FastingBS':fastingbs,
        'MaxHR':max_hr,
        'Oldpeak':old_peak,
        "Sex_"+ sex:1,
        'ChestPainType_'+chest_pain:1,
        'RestingECG'+resting_ecg:1,
        'ExerciseAngina'+ exercise_angina:1,
        'ST_Slope_'+st_slope:1
    }
    input_df=pd.DataFrame([raw_input])
    for col in expected_column:
        if col not in input_df.columns:
            input_df[col]=0
    input_df=input_df[expected_column]
    scaled_input=scaler.transform(input_df)
    prediction= model.predict(scaled_input)[0]
    
    if prediction==1: st.error("high risk of heart disease") 
    else: st.success("low risk of heart disease ")
