import streamlit as st
import FinanceDataReader as fdr
import datetime

date = st.date_input(
    '조회 시작일을 선택해주세요',
    datetime.datetime(2025, 5, 1)
)

code = st.text_input(
    '종목코드',
    value='',
    placeholder='종목 코드를 입력하세요' # 코스피 KS11, 코스닥 KQ11
)

if code and date:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'Close']
    st.line_chart(data)
