import streamlit as st

# Page Title
st.title("Introduction to Data Science Project 1")
st.header("Group 9")

# Team Members
st.subheader("Team Members")
team_members = [
    "Sou Pichchomrong",
    "Sroeun Bunnarith",
    "Sorng Seyha",
    "Thorn Davin",
    "Ngo Seakyarith"
]
for member in team_members:
    st.write(f"- {member}")

# Project Details
st.subheader("Project Overview")
st.write("""
This project demonstrates the use of **Linear Regression** to predict sales based on advertising budgets.
The dataset includes budgets for TV, Radio, and Newspaper advertisements.
""")

# Navigation to Sales Predictor Page
if st.button("Go to Sales Predictor"):
    st.switch_page("pages/Sales_Predictor.py")
