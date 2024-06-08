import streamlit as st
import json

st.set_page_config(page_title="Contributors", page_icon="👥", layout="wide")
st.markdown("""
    <style>
    img{
        align-items:center;
        width:300px;
    }
    .e115fcil2 {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    </style>
""", unsafe_allow_html = True)
st.image("assets/contribution.gif")
st.title("Contributors 👥")
data = json.loads(open("data/contributors.json").read())
container = st.container(border=True)
for i in range(data["count"]):

    person = container.container()
    c1, c2, c3 = person.columns(3)
    c2.markdown("""
    <style>
    p{
        padding-bottom: 15px;
    }
    .e1f1d6gn0, .e1f1d6gn3, .e1f1d6gn4{
        align-items:center;
        text-align:center;
    } 
    
    div[data-testid="column"]{
        align-items:center;
        text-align:center;

    }
    </style>
    """, unsafe_allow_html=True)
    
    c2.markdown(f"""**:orange[Name :]  {data["users"][i]}**  
**:orange[Roll Number :]  {data["rollnumbers"][i]}**    
**:orange[Contribution :]  {data["contribution"][i]}** 
""", unsafe_allow_html=True
    )
