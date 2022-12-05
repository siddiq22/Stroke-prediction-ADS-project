import streamlit as st
import numpy as np
import pandas as pd
import string
import pickle

st.set_option('deprecation.showfileUploaderEncoding', False)
model = pickle.load(open('model_pkl.pkl', 'rb'))

def main():
    # front end elements of the web page
    #st.title("Stroke Predictor")
    html_temp = """
    <div style ="background-color:#946294;padding:15px">
    <h1 style ="color:black;text-align:center;">Stroke Prediction</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    st.sidebar.header("Stroke Risk Prediction")
    st.sidebar.text("This page will predict whether you \nwill have a stroke or not.")
    st.sidebar.info("Just fill in the information requested")

    age = st.slider("Age", 0, 100)
    hypertension = st.slider("Do you have hypertension? 0 for no and 1 for yes", 0, 1)
    heartdisease = st.slider("Do you have a history of heart disease? 0 for no and 1 for yes", 0, 1)
    sugar = st.slider("What is your average glucose level?", 150.0, 300.000)
    bmi = st.slider("What is your BMI?", 0.0, 70.0)

    inputs = [[age, hypertension, heartdisease, sugar, bmi]]

    if st.button("Predict"):
        result = model.predict(inputs)
        updated_res = result.flatten().astype(int)
        if updated_res == 0:
            st.write('You are not susceptible to stroke anytime soon, but it would be advisable to continue to take care of yourself regardless.')
        else:
            st.write('You are prone to suffering a stroke and therefore, it is advisable to visit your doctor for a consultation, and begin taking good care of yourself.')

if __name__=='__main__':
    main()
