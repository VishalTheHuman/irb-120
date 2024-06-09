import streamlit as st
from st_pages import show_pages, Page, hide_pages
from streamlit_extras.stylable_container import stylable_container

def main():
    st.set_page_config(page_title="Home", page_icon="🏠", layout= "wide")
    show_pages(
        [
            Page("main.py", "Home", icon="🏠"),
            Page("pages/aim.py", "Objective", icon="🎯"),
            Page("pages/theory.py", "Theory", icon="📃"),
            Page("pages/faq.py", "FAQ", icon="❓"),
            Page("pages/pretest.py", "Pre-Test", icon="🧪"), 
            Page("pages/simulation.py", "Simulation", icon="🤖"),
            Page("pages/posttest.py", "Post-Test", icon="⌛"), 
            Page("pages/references.py", "References", icon="📝"), 
            Page("pages/contributors.py", "Contributors", icon="👥")
            
        ]
    )

    container = st.container()
    container.title(":orange[Forward] and :orange[Inverse Kinematics] of :red[ABB IRB 120] 🤖", anchor = False)
    container.image("assets/banner.png")
    container.header("**:blue[22AIE214] Introduction to AI Robotics**", anchor = False)
    container.markdown("""
##### :orange[Faculty :] Dr. Navaneeth Haridasan
""")


if __name__ == "__main__":
    main()