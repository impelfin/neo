import streamlit as st

st.title('스트림릿에서의 오디오 사용 예')

st.subheader('1. 로컬 저장소의 오디오 파일을 재생')
audio_file = './data/서연의_하루_TTS_배경음악_short.mp3'
audio_local = open(audio_file, "rb")
audio_bytes = audio_local.read()

st.text("MP3 파일. format='audio/mp3'")
st.audio(audio_bytes, format='audio/mp3')

st.subheader("2. 웹상에 있는 오디오 파일을 재생")
audio_url1 = "https://samplelib.com/lib/preview/wav/sample-15s.wav" 
st.text("WAV 파일. format='audio/wav'")
st.audio(audio_url1, format='audio/wav')

audio_url2 = "https://cdn.pixabay.com/download/audio/2022/10/14/audio_9939f792cb.mp3"
st.text("MP3 파일. format='audio/mpeg'")
st.audio(audio_url2, format='audio/mpeg')

audio_url3 = "https://freetestdata.com/wp-content/uploads/2021/09/Free_Test_Data_1MB_OGG.ogg"
st.text("OGG 파일. format='audio/ogg'")
st.audio(audio_url3, format='audio/ogg')
