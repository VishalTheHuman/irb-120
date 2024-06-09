import streamlit as st

st.set_page_config(page_title="Objective", page_icon="🎯", layout= "wide")

con = st.container(border = True)
con.title("1. Objective 🎯", anchor = False)

con.markdown("""The primary objective of this project is to develop and implement a neural network-based solution for both forward and inverse kinematics of the IRB 120 robot, enhancing the accuracy, efficiency, and flexibility of robotic kinematic calculations. This involves establishing mathematical models for forward kinematics to compute the end-effector's position and orientation from joint parameters, and for inverse kinematics to determine joint parameters from the desired end-effector position and orientation. Neural networks are designed to predict end-effector positions and orientations from joint parameters and vice versa, with appropriate loss functions and optimization techniques selected for effective training. 
            
            
The models are trained using the prepared dataset and validated with separate data to ensure good generalization, with hyperparameter tuning performed to optimize performance. Model performance is evaluated using metrics like MAE, RMSE, and R², with robustness and generalization assessed through various testing scenarios. The trained neural networks are then implemented in a real-time application for the IRB 120 robot, with a user-friendly interface developed to visualize movements and facilitate input of desired parameters. By achieving these objectives, the project aims to demonstrate the effectiveness of neural networks in solving complex kinematic problems for the IRB 120 robot, paving the way for more advanced and intelligent robotic systems in the future.

## **1.1 Overview of IRB 120**

The ABB IRB 120 is a compact and versatile industrial robot designed for high-speed precision applications. It features six degrees of freedom (DOF), making it suitable for tasks such as small parts assembly, material handling, and laboratory automation. Key specifications include:

- **Degrees of Freedom**: 6
- **Payload**: 3 kg (4 kg with a vertical wrist)
- **Reach**: 580 mm
- **Repeatability**: ±0.01 mm
- **Weight**: 25 kg
- **Power Supply**: 200-600V, 50-60Hz
- **Power Consumption**: 300W
- **Operating Temperature**: 5°C to 45°C
- **Protection Standard**: IP30

The IRB 120's kinematic configuration allows for flexible and precise movements, with forward kinematics calculating end-effector position and orientation from joint angles, and inverse kinematics determining joint angles from end-effector position and orientation. The robot is typically controlled using ABB's IRC5 compact controller, which offers advanced motion control, path planning, and safety features. The compact design, combined with its high precision and ease of integration, makes the IRB 120 ideal for a wide range of industrial and laboratory applications.

## **1.2 Components of IRB-120**


The ABB IRB 120 is composed of several key components, each contributing to its precision, versatility, and reliability in industrial applications. These components include:
- Base
- Joint 1 (Waist)
- Joint 2 (Shoulder)
- Joint 3 (Elbow)
- Joint 4 (Wrist Roll)
- Joint 5 (Wrist Pitch)
- Joint 6 (Wrist Yaw)
- End Effector

Understanding the IRB-120 manipulator's design and functionality is crucial for advancing robotic applications in industrial, medical, and research settings. This project seeks to optimize the manipulator's trajectory using Neural Networks, enhancing its efficiency and precision.


""")


st.markdown("""
    <style>
    h2, strong{
        font-weight:700;
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