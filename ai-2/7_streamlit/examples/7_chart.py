import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

chart_data = pd.DataFrame({
    "col1" : list(range(20)) *3,  
    "col2" : np.random.randn(60),  
    "col3" : ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
})

chart = alt.Chart(chart_data).mark_circle().encode(
    x = 'col1',
    y = 'col2',
    color = 'col3'
)

st.title('Chart Example')
st.altair_chart(chart, use_container_width=True)
