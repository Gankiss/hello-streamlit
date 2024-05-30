import streamlit as st
import random
import string
from collections import Counter
import matplotlib.pyplot as plt

# Title of the app
st.title("Simple Data Analysis App")

# Section 1: Random Data Generation and Visualization
st.header("Random Data Generation and Visualization")

# Generate random data
data_length = st.slider("Select the number of data points", 10, 100, 50)
random_data = [random.randint(1, 100) for _ in range(data_length)]
st.write("Generated Data:", random_data)

# Visualize the data
fig, ax = plt.subplots()
ax.plot(random_data, marker='o')
ax.set_title("Random Data Visualization")
st.pyplot(fig)

# Section 2: Basic Statistical Analysis
st.header("Basic Statistical Analysis")
mean_value = sum(random_data) / len(random_data)
median_value = sorted(random_data)[len(random_data) // 2]
mode_value = Counter(random_data).most_common(1)[0][0]

st.write(f"Mean: {mean_value}")
st.write(f"Median: {median_value}")
st.write(f"Mode: {mode_value}")

# Section 3: Text Analysis and Word Frequency Count
st.header("Text Analysis and Word Frequency Count")

# Input text
input_text = st.text_area("Enter some text for analysis")

if input_text:
    # Clean and split the text
    words = input_text.translate(str.maketrans('', '', string.punctuation)).lower().split()
    
    # Calculate word frequency
    word_freq = Counter(words)
    
    st.write("Word Frequency:")
    for word, freq in word_freq.items():
        st.write(f"{word}: {freq}")
    
    # Visualize word frequency
    fig, ax = plt.subplots()
    ax.bar(word_freq.keys(), word_freq.values())
    ax.set_title("Word Frequency Visualization")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Footer
st.markdown("**Developed by [Your Name]**")

