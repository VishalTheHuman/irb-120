import streamlit as st

st.set_page_config(page_title="Theory", page_icon="📃", layout= "wide")
con = st.container(border = True)
con.title("2.1 Theory 📃", anchor = False)

con.markdown(r"""
### **2.1 History of the IRB 120 Manipulator**

The IRB 120 is part of ABB's extensive range of industrial robots, known for their reliability, precision, and versatility. ABB, a leader in industrial robotics, introduced the IRB 120 to meet the demand for a compact and agile robot suitable for small parts assembly and laboratory automation. Launched in the early 2010s, the IRB 120 quickly became popular due to its lightweight design, ease of integration, and advanced control capabilities. It marked a significant step in making high-performance robotic solutions accessible to smaller manufacturing environments and research labs, complementing ABB's larger robots used in heavy industries.

### **2.2 Components of the IRB 120**

The ABB IRB 120 is a sophisticated industrial robot with key components that ensure precision, flexibility, and reliability:

- **Base**: Provides stability and houses power and data connections.
- **Joint 1 (Waist)**: Enables horizontal rotation for wide-area positioning.
- **Joint 2 (Shoulder)**: Allows vertical arm movement for different heights.
- **Joint 3 (Elbow)**: Moves the forearm towards/away from the body, increasing reach.
- **Joint 4 (Wrist Roll)**: Rotates the wrist about the forearm's axis for orientation.
- **Joint 5 (Wrist Pitch)**: Tilts the wrist up/down for precise positioning.
- **Joint 6 (Wrist Yaw)**: Rotates the end-effector around its axis for exact orientation.
- **End-Effector**: Tool at the wrist for interacting with the environment, customizable for different tasks.
  
  
These components collectively enable the IRB 120 to perform complex tasks with high precision and flexibility, making it suitable for a wide range of industrial and laboratory applications.

### **2.3 Basic Operational Principles of the IRB 120**

**Degrees of Freedom (DOF)**: The IRB 120 has six degrees of freedom, enabling movement in three translational and three rotational directions.

**Forward Kinematics**: This calculates the end effector's position and orientation from given joint parameters using Denavit-Hartenberg (D-H) parameters to describe the robot's geometry systematically.

**Inverse Kinematics**: This determines the joint parameters needed to achieve a desired end effector position and orientation.

**Control Mechanisms**:
  - **Resolved Rate Motion Control**: Adjusts joint velocities to achieve the desired end effector velocity.
  - **Advanced Algorithms**: Utilize optimization techniques like genetic algorithms to enhance trajectory planning and efficiency.
  

### **2.4 Mathematics Behind**

The kinematic parameters of IRB 120 are $ 	\theta_1, \theta_2, \theta_3, \theta_4, \theta_5, $ and $ \theta_6 $

The matrix describing the end effector's position and attitude relative to the reference coordinate system is:

$$
\begin{bmatrix}
n_x & n_y & n_z & 0 \\
o_x & o_y & o_z & 0 \\
a_x & a_y & a_z & 0 \\
p_x & p_y & p_z & 1
\end{bmatrix}
$$

Where $ n, o, a $ represent the end effector's orientation, and $ p $ is its position, with $ p_x, p_y, p_z $ being its coordinates in the reference coordinate system.

The relationship between adjacent coordinate systems (n-1 and n) is given by:

$$
A_n = R_z(\theta_n) \times R_x(\alpha_n) 
$$

$$
\begin{bmatrix}
\cos \theta_n & -\sin \theta_n \cos \alpha_n & \sin \theta_n \sin \alpha_n & 0 \\
\sin \theta_n & \cos \theta_n \cos \alpha_n & -\cos \theta_n \sin \alpha_n & 0 \\
0 & \sin \alpha_n & \cos \alpha_n & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

In this matrix:
- $ R_z(\theta_n) $ represents the rotation around the z-axis by angle $ \theta_n $.
- $ R_x(\alpha_n) $ represents the rotation around the x-axis by angle $ \alpha_n $.

""")


st.markdown("""
    <style>
    strong{
        font-weight:bold;
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
