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

#### **2.4.1 Denavit-Hartenberg (DH) Parameters**

The IRB 120 has six revolute joints. The DH parameters describe the relative positions and orientations of the robot's links and joints.

The DH parameters are:
1. $\theta_i$: Joint angle
2. $d_i$: Link offset
3. $a_i$: Link length
4. $\alpha_i$: Link twist

For the IRB 120, the DH parameters are typically given as:

| Joint (i) | $\theta_i$ | $d_i$ (m) | $a_i$ (m) | $\alpha_i$ (rad) |
|-----------|--------------|-------------|-------------|--------------------|
| 1         | $\theta_1$ | $d_1$     | 0           | $\pi/2$          |
| 2         | $\theta_2$ | 0           | $a_2$     | 0                  |
| 3         | $\theta_3$ | 0           | 0           | $\pi/2$          |
| 4         | $\theta_4$ | $d_4$     | 0           | $-\pi/2$         |
| 5         | $\theta_5$ | 0           | 0           | $\pi/2$          |
| 6         | $\theta_6$ | $d_6$     | 0           | 0                  |

Note: The exact numerical values for $d_i$ and $a_i$ depend on the specific configuration of the IRB 120 and should be provided in the robot's datasheet or user manual.

#### **2.4.2 Forward Kinematics**

Forward kinematics is the calculation of the position and orientation of the end-effector (robot's tool) given the joint angles.

To find the transformation matrix $ T_6^0 $ from the base frame to the end-effector frame, we use the individual transformation matrices from each frame $i-1$ to $i$ using the DH parameters:

$$
T_i^{i-1} = \begin{bmatrix}
\cos\theta_i & -\sin\theta_i \cos\alpha_i & \sin\theta_i \sin\alpha_i & a_i \cos\theta_i \\
\sin\theta_i & \cos\theta_i \cos\alpha_i & -\cos\theta_i \sin\alpha_i & a_i \sin\theta_i \\
0 & \sin\alpha_i & \cos\alpha_i & d_i \\
0 & 0 & 0 & 1
\end{bmatrix} 
$$

The overall transformation matrix is the product of the individual transformations:

$$
 T_6^0 = T_1^0 T_2^1 T_3^2 T_4^3 T_5^4 T_6^5 

$$


#### **2.4.3 Inverse Kinematics**

Inverse kinematics is the process of determining the joint angles given the position and orientation of the end-effector. This process is more complex and typically involves solving a system of nonlinear equations.

For a six-axis robot like the IRB 120, the inverse kinematics solution involves:
1. Position Kinematics: Determining the position of the wrist center (intersection of axes 4, 5, and 6) based on the end-effector position.
2. Orientation Kinematics: Determining the orientation of the wrist axes.

#### **2.4.4 Steps for Inverse Kinematics**

1. **Compute Wrist Center**:
$$
    \text{Wrist Center} = P - d_6 \cdot \hat{R} \cdot \hat{z}_6 

$$
   where $ P $ is the position of the end-effector, $ \hat{R} $ is the rotation matrix of the end-effector, and $ \hat{z}_6 $ is the z-axis of the end-effector frame.

2. **Solve for First Three Joints**:
   - Determine $\theta_1$, $\theta_2$, and $\theta_3$ based on the position of the wrist center.

3. **Solve for Last Three Joints**:
   - Calculate the orientation of the wrist relative to the base.
   - Determine $\theta_4$, $\theta_5$, and $\theta_6$ based on the orientation of the wrist.

#### **2.4.5 Analytical Inverse Kinematics Solution**

For the IRB 120, the steps can be summarized as:
1. Compute the position of the wrist center $ W $:
$$
    W = P - d_6 \cdot \hat{R} \cdot \hat{z}_6 

$$

2. Solve for $ \theta_1 $:
$$
    \theta_1 = \arctan2(W_y, W_x) 

$$

3. Solve for $ \theta_2 $ and $ \theta_3 $:
   Use geometric relationships or trigonometric methods to solve these angles based on the wrist center position.

4. Compute the rotation matrix from the base frame to the wrist frame $ R_{03} $ using $ \theta_1, \theta_2, \theta_3 $.

5. Compute the rotation matrix from the wrist frame to the end-effector frame $ R_{36} $:
$$
    R_{36} = R_{03}^T \cdot R 

$$

6. Solve for $ \theta_4, \theta_5, \theta_6 $ from $ R_{36} $ using the ZYX Euler angles or other parameterizations.

### **2.5 LSTM**

Long Short-Term Memory (LSTM) is a type of recurrent neural network (RNN) architecture designed to address the vanishing gradient problem that can occur when training traditional RNNs. LSTMs are capable of learning long-term dependencies in sequential data by maintaining a memory cell and gating mechanisms.

Here's a brief explanation of LSTM components:
- **Memory Cell**: A cell that retains information over long periods of time.
- **Input Gate**: Controls how much new information is stored in the memory cell.
- **Forget Gate**: Controls how much of the existing memory cell is discarded.
- **Output Gate**: Determines the output based on the current input and the memory cell's state.

#### **2.5.1 Context on Using LSTM for Kinematics of IRB 120**

LSTMs can be used in various ways in robotics, including for solving the forward and inverse kinematics of robots like the IRB 120:

1. **Learning from Demonstrations**:
   - LSTMs can be trained using demonstrations of robot movements. For example, if you have a dataset of joint angles and corresponding end-effector positions, you can train an LSTM to learn the mapping between joint configurations and end-effector positions. This can be particularly useful for complex robots like the IRB 120, where the kinematics equations may be nonlinear and difficult to model analytically.

2. **Trajectory Prediction**:
   - LSTMs can predict future robot trajectories based on past observations. By training an LSTM on sequences of joint angles and end-effector positions, the model can learn the dynamics of the robot's movement and predict its future trajectory. This capability can be valuable for motion planning and collision avoidance.

3. **Online Learning and Adaptation**:
   - LSTMs can adapt to changes in the robot's environment or task requirements. By continuously updating the LSTM with new data during operation, the model can refine its predictions and adjust to new conditions. This adaptability is crucial for real-world applications where the robot may encounter varying environments or tasks.

4. **Combining with Reinforcement Learning**:
   - LSTMs can be integrated into reinforcement learning algorithms to enable robots to learn complex tasks through trial and error. By using an LSTM to model the robot's state and dynamics, reinforcement learning agents can learn effective control policies for tasks such as grasping, manipulation, or navigation.

In the context of finding the forward and inverse kinematics of the IRB 120, an LSTM could be trained to learn the mapping between joint angles and end-effector positions. Once trained, the LSTM could be used to predict the end-effector position given a set of joint angles (forward kinematics), or to infer the joint angles required to achieve a desired end-effector position (inverse kinematics). This approach can be particularly useful when analytical solutions are complex or impractical, or when dealing with uncertainties and nonlinearities in the robot's dynamics.
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
