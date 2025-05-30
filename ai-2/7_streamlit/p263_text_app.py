import streamlit as st

st.title('st.title(문자열) : 제목')
st.header('st.header(문자열) : 헤더')
st.subheader('st.subheader(문자열) : 서브헤더')
st.text('st.text(문자열) : 일반 텍스트')

st.text('st.code(code) : 파이썬 코드 표시')

code = '''
    def hello():
        print('hello Streamlit!!')
'''

st.code(code)

st.markdown('스트림릿에서 **마크다운**을 사용 가능.:sunglasses:')
