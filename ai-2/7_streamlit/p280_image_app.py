import streamlit as st
from PIL import Image

st.title('스트림릿에서의 이미지 표시 사용 예')

st.subheader('1. 로컬 저장소의 이미지 파일을 표시')
image_file = './data/avenue.jpg'
image_local = Image.open(image_file)
st.image(image_local, width=350, caption='로컬 저장소에 있는 이미지 파일을 표시')

st.subheader('2. 웹상에 있는 이미지 파일을 표시')
image_url = "https://cdn.pixabay.com/photo/2023/05/29/06/25/mountains-8025144_1280.jpg" 
st.image(image_url, width=350, caption='웹상에 있는 이미지 파일을 표시')