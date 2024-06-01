import streamlit as st
import pandas as pd

# Title of the app
st.title("Country Statistics Viewer")

# Load the CSV data
csv_file_path = 'data/Countries.csv'

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

data = load_data(csv_file_path)

# User selection: country
country_list = data['Country'].unique()
selected_country = st.selectbox("Select a country:", country_list)

# Display the country stats
if selected_country:
    country_data = data[data['Country'] == selected_country].squeeze()
    st.write(f"Statistics for {selected_country}:")
    for column in country_data.index:
        st.write(f"{column}: {country_data[column]}")

# Footer
st.markdown("**Test**")




# https://hello-app-x2mmstm9z9.streamlit.app/
