import streamlit as st
import pandas as pd

# Add custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        color: #4CAF50;
        font-size: 36px;
        font-weight: bold;
    }
    .dataframe {
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the welcome message with custom CSS class
st.markdown('<div class="main"><div class="title">Welcome to Parallel World</div></div>', unsafe_allow_html=True)

# Create a DataFrame
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# Display the DataFrame with custom CSS class
st.markdown('<div class="main dataframe">', unsafe_allow_html=True)
st.write(df)
st.markdown('</div>', unsafe_allow_html=True)
