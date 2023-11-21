import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Santiago Simões")
    content = """Hello, I'm Santiago! I worked at Roblox for 5 years and I made two big games that got really famous 
    at that time. I've also spent some months learning Unity and I've been taking a look at Unreal Engine 5 and 
    Python (because I want to make things easier in my daily life and to make applications/programs)."""
    st.info(content)

st.write("Below you can see some of my projects. You can contact me if you are interested in any deal.")

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])