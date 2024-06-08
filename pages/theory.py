import streamlit as st

st.set_page_config(page_title="Theory", page_icon="📃", layout= "wide")

st.title("Theory 📃", anchor = False)
st.image("assets/theory.gif")
st.markdown("""
    <style>
    
    .e1nzilvr1{
        align-items:center;
        text-align:center;
    } 
    div[data-testid="StyledLinkIconContainer"]{
        text-align:left;
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
    </style>
    
    """, unsafe_allow_html=True)

st.header(":orange[Introduction]")

st.markdown("""The IRB 120 is a compact and versatile industrial robot developed by ABB Robotics. With its small footprint and high precision, it's ideal for applications requiring agility in confined spaces. Equipped with advanced motion control and programming capabilities, it excels in tasks like material handling, assembly, and machine tending. Its user-friendly interface, including the IRC5 controller, makes programming and operation straightforward, even for novices. The robot's robust design ensures reliability and durability in demanding industrial environments, while its modular construction allows for easy integration and customization to meet specific application requirements. Additionally, its compact design enables it to be easily transported between different workstations, enhancing its adaptability.""")

st.header(":orange[Configuration]")

st.markdown("""The IRB 120 offers various configurations to suit diverse industrial needs. It comes in both floor and wall-mounted versions, providing flexibility in installation. With multiple mounting options, including inverted, tilted, and shelf-mounted orientations, it adapts seamlessly to different production layouts. The robot's compact design, lightweight construction, and small footprint make it suitable for installations in constrained spaces. Additionally, optional features such as different wrist configurations and payload capacities enhance its versatility. Whether used standalone or as part of a robotic system, the IRB 120's configurable options ensure optimal performance and integration with existing workflows.""")

st.header(":orange[Inverse Kinematics]")

st.markdown("""Inverse kinematics in the IRB 120 involve determining the joint angles required to achieve a specific end-effector position and orientation. Due to its six degrees of freedom (DOF), solving inverse kinematics for the IRB 120 requires complex mathematical calculations. Using geometric and trigonometric principles, the robot's kinematic chain, comprising rotational joints and links, is analyzed to derive the joint angles corresponding to the desired end-effector pose. Advanced algorithms, such as iterative methods or closed-form solutions, are employed to compute these angles efficiently. Accurate inverse kinematics computation is crucial for precise robot motion control and task execution in various industrial applications.""")

