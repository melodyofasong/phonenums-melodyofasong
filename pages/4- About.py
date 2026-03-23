import streamlit as st

with open("assets/About.md", "r") as f:
    content = f.read()
st.markdown(content)
