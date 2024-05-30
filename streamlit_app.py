import streamlit as st
import base64

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
st.title("Base64 Encoder/Decoder")

# User selection: encode or decode
option = st.selectbox("Choose an option:", ["Encode", "Decode"])

# User input
input_text = st.text_area("Enter the text to be encoded/decoded:")

if st.button("Submit"):
    if option == "Encode":
        # Encode the input text to Base64
        encoded_text = base64.b64encode(input_text.encode()).decode()
        st.write("Encoded Base64 text:", encoded_text)
    elif option == "Decode":
        try:
            # Decode the input Base64 text
            decoded_text = base64.b64decode(input_text.encode()).decode()
            st.write("Decoded text:", decoded_text)
        except Exception as e:
            st.error(f"Error decoding Base64 text: {e}")

# Footer
st.markdown("**TEST**")

# https://hello-app-x2mmstm9z9.streamlit.app/
