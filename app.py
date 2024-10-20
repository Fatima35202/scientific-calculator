import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Page configuration
st.set_page_config(page_title="Scientific Graphical Calculator", layout="wide")

# Add custom CSS for gradient background
st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to right, #000000, #434343, #f0f0f0);
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: rgba(0, 0, 0, 0.7);
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🧮 Scientific Graphical Calculator")
st.markdown("---")

# Sidebar for inputs
st.sidebar.header("Calculator Inputs")
operation = st.sidebar.selectbox("Choose an operation", [
    "Addition", 
    "Subtraction", 
    "Multiplication", 
    "Division", 
    "Plot Function"
])

if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
    num1 = st.sidebar.number_input("Enter first number", -1000, 1000, 0)
    num2 = st.sidebar.number_input("Enter second number", -1000, 1000, 0)

    if st.sidebar.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"

        st.success(f"The result of {operation} is: {result}")

        # Animation: Show a loading effect
        with st.spinner("Calculating..."):
            time.sleep(1)  # Simulate a time delay

elif operation == "Plot Function":
    expression = st.sidebar.text_input("Enter an expression (e.g., np.sin(x), np.log(x), x**2)", "np.sin(x)")
    x_min = st.sidebar.number_input("Minimum x value", -10, 10, -5)
    x_max = st.sidebar.number_input("Maximum x value", -10, 10, 5)

    if st.sidebar.button("Calculate and Plot"):
        try:
            x = np.linspace(x_min, x_max, 400)
            y = eval(expression)  # Evaluate the expression
            
            # Plotting
            plt.figure(figsize=(10, 6))
            plt.plot(x, y, label=f"y = {expression}", color='cyan')
            plt.title("Graph of the Function", color='white')
            plt.xlabel("x", color='white')
            plt.ylabel("y", color='white')
            plt.axhline(0, color='white', lw=0.5, ls='--')
            plt.axvline(0, color='white', lw=0.5, ls='--')
            plt.grid(color='white', linestyle='--', linewidth=0.5)
            plt.legend(facecolor='black', edgecolor='white', fontsize='small')
            st.pyplot(plt)

            # Animation: Show a loading effect
            with st.spinner("Plotting..."):
                time.sleep(1)  # Simulate a time delay

        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Fatima Tanveer")
