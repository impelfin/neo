import streamlit as st
import random
import datetime

st.title(':sparkles: 로또 생성기 :sparkles:')

def generate_lotto():
    lotto = set()

    while len(lotto) < 6:
        number =random.randint(1, 46)
        lotto.add(number)

    lotto = list(lotto)
    lotto.sort()
    return lotto

button = st.button('로또 번호 생성')

if button:
    for i  in range(1, 6):
        st.write(f'{i}. 행운의 번호 : {generate_lotto()}')
    st.write(f'생성된 시간 : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

