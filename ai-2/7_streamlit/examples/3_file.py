import streamlit as st
import pandas as pd
import time

file = st.file_uploader('파일 선택(csv or excel)', type=['csv', 'xlsx', 'xls'])

time.sleep(3)

if file is not None:
    ext = file.name.split('.')[-1]
    if ext == 'csv':
        df = pd.read_csv(file)
        st.dataframe(df)
    elif 'xls' or 'xlsx' in ext:
        df = pd.read_excel(file, engine='openpyxl')
        st.dataframe(df)
