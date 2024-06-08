import streamlit as st
import json
st.set_page_config(page_title="FAQ", page_icon="❓")

st.image("assets/faq.gif")
st.title("FAQ ❓", anchor = False)

st.markdown("""
    <style>
    
    .e1f1d6gn0{
        align-items:center;
        text-align:center;
    } 
    img{
        align-items:center;
        width:250px;
    }
    .e115fcil2 {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    p{
        text-align:left;
    }
    </style>
    """, unsafe_allow_html=True)

data = json.loads(open("data/faq.json", "r").read())

for i in range(data["count"]):
    with st.expander(data["faq"]["question"][i]):
        st.write(data["faq"]["answer"][i])