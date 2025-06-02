import streamlit as st

st.title('스트림릿에서의 비디오 사용 예')

st.subheader('1. 로컬 저장소의 비디오 파일을 재생')
video_file = './data/sample_video.mp4'
video_local = open(video_file, "rb")
video_bytes = video_local.read()

st.text("MP4 파일. format='video/mp4'")
st.video(video_bytes, format='video/mp4')

st.subheader("2. 유튜브 비디오를 재생")
video_url = "https://www.youtube.com/watch?v=5VxYrmnwQiA"
st.text("MP4 파일. format='video/mp4'")
st.video(video_url, format='video/mp4')
