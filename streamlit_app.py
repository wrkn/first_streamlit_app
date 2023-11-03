import streamlit as st
import pandas as pd

st.title('My Parents New Healthier Diner')
st.header('Breakfast menu')
st.text('Omege 3 and Bluberry Oatmeal')
st.text('Kale, Spinach and Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

st.multiselect("Pick some fruits:", list(my_fruit_list.index))

st.dataframe(my_fruit_list)

