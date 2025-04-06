import streamlit as st
import pandas as pd

st.title("BMI Calculator")

weight=st.number_input("Enter your weight in kg")
height=st.number_input("Enter your height in cm")

if st.button("Calculate BMI"):
    if weight>0 and height>0:
        st.success("BMI calculated successfully")
        bmi=weight/(height/100)**2
        st.write(f"Your BMI is {bmi}")
    else:
        st.error("Please enter valid weight and height")

if st.button("Exit"):
    st.stop()
st.subheader("categories of bmi")
st.write("underweight:less than 18.5")
st.write("normal:18.5-24.9")
st.write("overweight:25-29.9")
st.write("obesity:30 or higher")
st.info("madebytahaq")
