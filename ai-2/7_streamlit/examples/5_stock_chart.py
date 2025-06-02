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

    if df.empty:
        st.write(f'데이터가 없습니다. 종목 코드 또는 날짜를 확인하세요.')
    else:
        st.write('데이터프레임 컬럼 : ', df.columns.tolist())
        if 'Close' in df.columns:
            data = df.sort_index(ascending=True).loc[:, 'Close']
            
            tab1, tab2 = st.tabs(['차트', '데이터'])
            
            with tab1:
                st.line_chart(data)
            
            with tab2:
                st.dataframe(df.sort_index(ascending=False))

            with st.expander('컬럼 설명'):
                st.markdown('''
                - Open : 시가
                - High : 고가
                - Low : 저가
                - Close : 종가
                - Adj Close : 수정 종가
                - Volume : 거래량
                ''')
        else:
            st.write("'Close' 컬럼에 데이터가 없습니다.")
