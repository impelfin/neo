import streamlit as st

st.title('스트림릿에서의 체크 박스 사용 예')

checked1 = st.checkbox('checkbox 1')
st.write('checkbox 1 Status: ', checked1)

if checked1:
    st.write('checkbox 1 was checked')
else:
    st.write('checkbox 1 was not checked')

checkd2 = st.checkbox('checkbox 2')
st.write('checkbox 2 Status: ', checkd2)

if checkd2:
    st.write('checkbox 2 was checkd')
else:
    st.write('checkbox 2 was not checkd')