import streamlit as st 
import pandas as pd
from io import BytesIO

st.title('스트림릿의 다운로드 버튼 사용 예')

st.subheader('텍스트 파일 다운로드 예제')

folder = './data/'

with open(folder + '서연의_이야기.txt', encoding='utf-8') as f:
    text_data = f.read()
    st.download_button(
        label = '텍스트 파일 다운로드',
        data = text_data,
        file_name = '서연의 이야기.txt',
        mime = 'text/plain'
    )

st.subheader('이미지 파일 다운로드 예제')

with open(folder + 'sample_image.png', 'rb') as img_file:
    st.download_button(
        label = '이미지 파일 다운로드',
        data = img_file,
        file_name = 'sample_image.png',
        mime = 'image/jpeg'
    )

st.subheader('오디오 파일 다운로드 예제')

with open(folder + '서연의_하루_TTS_배경음악_short.mp3', 'rb') as audio_file:
    st.download_button(
        label = '이미지 파일 다운로드',
        data = audio_file,
        file_name = '서연의_하루_TTS_배경음악_short.mp3',
        mime = 'image/jpeg'
    )
