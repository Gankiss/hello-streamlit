import streamlit as st

# Set the black color scheme
st.markdown(
    """
    <style>
    .reportview-container {
        background: black;
        color: white;
    }
    .sidebar .sidebar-content {
        background: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("Simple Addition App")

# User inputs
number1 = st.number_input("Enter first number:", step=1.0, format="%.2f")
number2 = st.number_input("Enter second number:", step=1.0, format="%.2f")

# Add the two numbers
result = number1 + number2

# Display the result
st.write("Result of addition:", result)

# Footer
st.markdown("**Hello Jenners**")
