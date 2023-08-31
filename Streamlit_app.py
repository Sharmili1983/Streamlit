pip install -q streamlit
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
#Find the Greatest number

This app predicts the Greatest number out of three numbers.
""")

st.header('User Input Parameters:')

def user_input_features():
  No1 = st.number_input("Number1: ")
  No2 = st.number_input("Number2: ")
  No3 = st.number_input("Number3: ")

  if (No1>No2 and No1>No3):
    print("Greatest number is ", No1)
  elif (No2>No1 and No2>No3):
    print("Greatest number is ", No2)
  elif (No3>No1 and No3>No2):
    print("Greatest number is ", No3)

  data = {'Number1': No1,
          'Number2': No2,
          'Number3': No3
          }

  features = pd.DataFrame(data, index=[0])
  return features

data = user_input_features()

st.subheader('User Input parameters')
st.write(data.to_dict())
