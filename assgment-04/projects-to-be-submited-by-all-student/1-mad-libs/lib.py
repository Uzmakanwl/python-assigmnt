 
import streamlit as st



#user say input Lyna
name = input("Enter the girl name: ")
programming_language = input(" Enter the progamming language (e.g: python, nextjs, typescript , html): ")
mentor = input ("Enter the mentor name: ")
location = input ("Enter location e.g: governor house ") 

# Story created
st.print("\n Here is my little story based on mad libs game!")
st.print(f"once upon a time , there was a girl named {name}. :")
st.print(f"{name} was very curious and always learn new things ")
st.print(f"One day , she decided to learn {programming_language} language at {location}")
st.print(f"Luckly {name} found a great metor name as {mentor} who have a graet experties in {programming_language}. ")
st.print("And so , her journey continues.....!")
