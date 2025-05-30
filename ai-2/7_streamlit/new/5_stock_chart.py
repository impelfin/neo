# Finance Data Reader
# https://github.com/financedata-org/FinanceDataReader

## pip install finance-datareader

import streamlit as st
import FinanceDataReader as fdr
import datetime
import time

st.title('종목 차트 검색')

with st.sidebar:
    date = st.date_input(
        "조회 시작일을 선택해 주세요",
        datetime.datetime(2025, 6, 1)
    )

    code = st.text_input(
        '종목코드', 
        value='',
        placeholder='종목코드를 입력해 주세요'
    )

if code and date:
    df = fdr.DataReader(code, date)

    if df.empty:
        st.error("데이터가 없습니다. 종목코드 또는 날짜를 확인하세요.")
    else:
        st.write("데이터프레임 컬럼:", df.columns.tolist())
        if 'Close' in df.columns:
            data = df.sort_index(ascending=True).loc[:, 'Close']

            tab1, tab2 = st.tabs(['차트', '데이터'])

            with tab1:    
                st.line_chart(data)

            with tab2:
                st.dataframe(df.sort_index(ascending=False))

            with st.expander('컬럼 설명'):
                st.markdown('''
                - Open: 시가
                - High: 고가
                - Low: 저가
                - Close: 종가
                - Adj Close: 수정 종가
                - Volume: 거래량
                ''')
        else:
            st.error("'Close' 컬럼이 데이터에 없습니다.")
