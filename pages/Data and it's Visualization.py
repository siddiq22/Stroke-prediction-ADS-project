import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Welcome to Data Visualization")
st.write("Let us look at a few factors that effect the possibility of Stroke in a person. This will allow us to visualize different reasons a person could suffer from Stroke.")
st.write("Let us look at how the data collected looks overall: ")

@st.cache
def load_data():
    dataset = pd.read_csv('./data/healthcare-dataset-stroke-data.csv')
    age_group=[]
    for i in dataset['age']:
        if i<2.0:
            age_group.append('Toddler')
        elif i>2.0 and i<=12.0:
            age_group.append('Child')
        elif i>12.0 and i<=19.0:
            age_group.append('Teen')
        elif i>19.0 and i<=60:
            age_group.append('Adult')
        else:
            age_group.append('Senior')
    dataset['age_group']=age_group
    dataset.head()
    return dataset

df = load_data()
st.write(df)
st.write('---')

st.header("Visualization")

st.write("Here, you will see the relationship between the BMI of a person vs their Gender ")
sns.scatterplot(data=df,x='bmi',y='age')
st.pyplot()

st.write('Let us look at how the two genders, Male and Female')
sns.boxplot(x=df['gender'],y=df['bmi'])
st.pyplot()
