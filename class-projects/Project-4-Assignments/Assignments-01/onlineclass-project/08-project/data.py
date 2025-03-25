import streamlit as st
import pandas as pd

data = {"Name":["Muhammad Adnan","Nabeeha","Abeeha", "Munazza"],
        "Age":[42,12,8,5],
        "City":["Karachi","Islamabad","Lahore","Multan"],
        "Status":["Job","Learning","Learning","Learning"]}

df = pd.DataFrame(data)
st.title("Data with style & user input")
"""
Get an user input as number input and filter based on that number defaulty its going to be 80
"""
# User input for the minimum value to highlight
value_of_style = st.number_input("Enter the minimum number to display in yellow", value=40)

# Function to apply styling based on the user input
def highlight_values(val, threshold):
    if isinstance(val, int) and val >= threshold:
        return "background-color: yellow"
    return ""

# Apply the styling function to the DataFrame
styled_df = df.style.apply(lambda x: x.map(lambda val: highlight_values(val, value_of_style)))

# Display the styled DataFrame
st.dataframe(styled_df)