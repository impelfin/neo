import streamlit as st

st.title('스트림릿에서 세션 상태 사용 예')

if 'count' not in st.session_state:
    st.session_state['count'] = 0

if 'registered' not in st.session_state:
    st.session_state['registered'] = []

user_input = st.text_input('이름', value='이름을 입력하세요', key='name')

clicked = st.button('등록')

if clicked:
    st.session_state['count'] += 1
    st.write('버튼 입력 횟수 : ', st.session_state['count'])

    name = st.session_state['name']
    st.session_state['registered'].append(name)
    st.write('등록된 이름 리스트 : ', st.session_state['registered'])
    