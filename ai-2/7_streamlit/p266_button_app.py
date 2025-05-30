import streamlit as st

st.title('스트림릿에서의 버튼 입력 사용 예')

clicked = st.button('Button 1')
st.write('Button 1 Status: ', clicked)

if clicked:
    st.write('Button 1 was clicked')
else:
    st.write('Button 1 was not clicked')

clicked = st.button('Button 2')
st.write('Button 2 Status: ', clicked)

if clicked:
    st.write('Button 2 was clicked')
else:
    st.write('Button 2 was not clicked')