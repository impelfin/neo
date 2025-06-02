import streamlit as st
from PIL import Image

st.title('스트림릿에서의 화면 분할 사용 예')

[col1, col2] = st.columns(2)

with col1:
    st.subheader('유뷰트 비디오1')
    url_col1 = "https://www.youtube.com/watch?v=bagb1zxqMTg"
    st.video(url_col1)

with col2:
    st.subheader('유뷰트 비디오2')
    url_col2 = "https://www.youtube.com/watch?v=i-E7NiyRDa0"
    st.video(url_col2)

columns = st.columns([1.1, 1.0, 0.9])

folder = './data/'
image_files = ['dog.png', 'cat.png', 'bird.png']
image_captions = ['강아지', '고양이', '새']

for k in range(len(columns)):
    with columns[k]:
        st.subheader(image_captions[k])
        image_local = Image.open(folder + image_files[k])
        st.image(image_local, width=200, caption=image_captions[k])
        