import streamlit as st
import pandas as pd

st.title(":blue[Find the Greatest number]")
st.write("""This App predicts the Greatest number out of three numbers""")

st.subheader('Enter any three numbers!')
primary_color = "#00f900"

def user_input_features():
  No1 = st.number_input("Number1: ")
  No2 = st.number_input("Number2: ")
  No3 = st.number_input("Number3: ")
  if (No1>No2 and No1>No3):
    No1 = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Greatest number is </p>'
    st.markdown(No1, unsafe_allow_html=True)
    #st.write(":primary_color[Greatest number is ]", No1)
  elif (No2>No1 and No2>No3):
     st.write("_:primary_color[Greatest number is ]_", No2)
  elif (No3>No1 and No3>No2):
     st.write("_:primary_color[Greatest number is ]_", No3)

  data = {'Number1': No1,
          'Number2': No2,
          'Number3': No3
          }

  features = pd.DataFrame(data, index=[0])
  return features

data = user_input_features()

st.subheader('User Input parameters')
st.write(data.to_dict())
