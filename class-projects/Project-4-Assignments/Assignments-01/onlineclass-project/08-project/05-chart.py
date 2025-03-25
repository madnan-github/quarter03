import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.DataFrame(
    np.random.randn(100,3),
    columns=["A","B","C"]
)
plt.figure(figsize=(10,6))
sns.scatterplot(x = data["A"], y = data["B"])
plt.title("Scatter plot of A & B")
st.pyplot(plt)