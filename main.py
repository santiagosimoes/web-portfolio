import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Santiago Simões")
    content = """Hello, I'm Santiago! I worked at Roblox for 5 years and I made two big games that got really famous 
    at that time. At the moment, I've also spent some months learning Unity, where I have also made and published a 
    game to Steam. I've been taking a look at Unreal Engine 5 and Python (because I want to make things easier in my 
    daily life and to make applications/programs)."""
    st.info(content)