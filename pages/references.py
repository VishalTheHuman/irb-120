import streamlit as st
import pandas as pd

st.set_page_config(page_title="References", page_icon="📝", layout= "wide")

st.image("assets/references.gif")
st.title("References 📝", anchor = False)
df = pd.read_csv("data/references.csv")

st.markdown("""
    <style>
    
    .e1f1d6gn0, .e1f1d6gn3, .e1f1d6gn4{
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
    div{
        font-weight:bold;
    }
    </style>
    """, unsafe_allow_html=True)
st.dataframe(df, column_config={
        "Website": st.column_config.LinkColumn(
            "Website",
            validate="^https://[a-zA-Z0-9]+/.*",
            display_text="https://([a-zA-Z0-9]*?)/.*"
        )
    }, 
    use_container_width = True, hide_index = True)