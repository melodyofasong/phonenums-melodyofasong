import streamlit as st

f = "E:\\Harshita's Explorations\\github\\phonenums-melodyofasong\\assets\\About.md"
md_path = "E:\\Harshita's Explorations\\Classifieds phone numbers\\phonenums\\streamlit-phonenums-v1\\assets\\About.md"
with open(f, "r") as f:
    content = f.read()
st.markdown(content)
