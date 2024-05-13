import streamlit as st
from PIL import Image


st.title('IMDS')
st.caption('チェックプログラム')

image = Image.open('./data/ダウンロード.png')
st.image(image, width=200)
