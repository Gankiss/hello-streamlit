import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Cybersecurity Analyst Dashboard")

# Section for uploading log files
st.header("Upload Log Files")
uploaded_file = st.file_uploader("Choose a log file", type=["csv", "txt"])

if uploaded_file is not None:
    # Assume the log file is in CSV format
    logs_df = pd.read_csv(uploaded_file)
    st.write("Log File Data")
    st.dataframe(logs_df)

    # Visualize log data
    st.header("Log Data Visualization")
    log_columns = st.multiselect("Select columns to visualize", logs_df.columns)
    if log_columns:
        st.line_chart(logs_df[log_columns])

# Section for threat data visualization
st.header("Threat Data Visualization")
# Dummy threat data
threat_data = {
    'Threat Type': ['Malware', 'Phishing', 'DDoS', 'Ransomware'],
    'Occurrences': [45, 30, 15, 10]
}
threat_df = pd.DataFrame(threat_data)
st.bar_chart(threat_df.set_index('Threat Type'))

# Section for displaying alerts
st.header("Recent Alerts")
# Dummy alerts
alerts = [
    "Suspicious login detected from IP 192.168.1.1",
    "Multiple failed login attempts",
    "Malware detected in email attachment"
]
for alert in alerts:
    st.warning(alert)

# Section for network traffic analysis
st.header("Network Traffic Analysis")
# Dummy network traffic data
traffic_data = {
    'Time': pd.date_range(start='1/1/2024', periods=24, freq='H'),
    'Traffic (MB)': [50, 45, 40, 60, 70, 65, 80, 85, 90, 95, 100, 110, 105, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50]
}
traffic_df = pd.DataFrame(traffic_data)
st.line_chart(traffic_df.set_index('Time'))

# Additional feature: User-defined query
st.header("Custom Query")
query = st.text_input("Enter a query (e.g., filter logs for a specific IP address)")
if query:
    st.write("Query results (dummy data):")
    st.write(logs_df.head(5))  # In real application, process the query on logs_df

# Footer
st.markdown("**Developed by [Your Name]**")

