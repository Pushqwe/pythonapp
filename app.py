import streamlit as st

st.title("AI Traveller APP")

destination=st.text_input("Enter Destination: ")
travel_date=st.text_input("Enter Travel Date")
budget=st.number_input("Enter Budget", min_value=0)

st.write(f"""
### Travel Summary

Destination : {destination}

Travel Date : {travel_date}

Budget : ₹{budget}
""")
