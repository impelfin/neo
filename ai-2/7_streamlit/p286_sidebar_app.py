import streamlit as st
from PIL import Image

# -------------------- side bar --------------------
st.sidebar.title('Sidebar')
st.sidebar.header('텍스트 입력 사용 예')
user_id = st.sidebar.text_input('아이디(ID) 입력', value='root', max_chars=15)
user_password = st.sidebar.text_input('패스워드(Password) 입력', value='1234', type='password')

st.sidebar.header('셀렉트 박스 사용 예')
selectbox_option = ['진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '월하정인']
your_option = st.sidebar.selectbox('좋아하는 작품은?', selectbox_option, index=3)
st.sidebar.write('**당신의 선택** :', your_option)

# -------------------- Main view --------------------
folder = './data/'

image_files = ['Vermeer.png', 'Gogh.png', 'Munch.png', 'ShinYoonbok.png']

selectbox_options_index = selectbox_option.index(your_option)
img_file = image_files[selectbox_options_index]
image_local = Image.open(folder + img_file)

st.image(image_local, width=400, caption=your_option)
