import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt

chart_data = pd.DataFrame({
    "col1": list(range(20)) * 3,
    "col2": np.random.randn(60),
    "col3": ["A"] * 20 + ["B"] * 20 + ["("] * 20,
})

chart = alt.Chart(chart_data).mark_bar().encode(
    x='col1:O',
    y='col2:Q',
    color='col3:N'
).properties(width=600, height=400)

st.altair_chart(chart, use_container_width=True)
