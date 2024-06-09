import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Simulation", page_icon="🤖", layout="wide")

FORWARD = "https://irb-120.vercel.app/forward.html" 
INVERSE = "https://irb-120.vercel.app/inverse.html" 

st.title(":orange[Simulation] of :red[IRB-120]")

st.markdown(f"""
    <iframe src={FORWARD} width="1080" height="600" frameborder="0"></iframe>
    """, unsafe_allow_html=True)