import streamlit as st
import cv2 as cv
import numpy as np

st.title("Welcome!")
st.write("Please Enter Your Name: ")
name = st.text_input("Type Name")

if name:
    st.write("Hello ", name)
    stroke_title = '<p style="font-family:Courier; font-size: 15px;">Let us Talk about Stroke</p>'
    st.markdown(stroke_title, unsafe_allow_html=True)
    img = cv2.imread("stroke.png", 1)
    image = np.array([img])
    st.write("A stroke, sometimes called a brain attack, occurs when something blocks blood supply to part of the brain or when a blood vessel in the brain bursts. In either case, parts of the brain become damaged or die. A stroke can cause lasting brain damage, long-term disability, or even death.")
    st.write('Use the sidebar options to navigate the app,')
    st.write("Click on Data and it's Visualization to see how the data used for this app looks")
    st.write("The page titled, 'Will You have a Stroke', is meant to make use of Gaussian Naive Bayes to predict whether you will have a stroke or not based on the parameters you enter")
