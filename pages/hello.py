import streamlit as st
from auth import require_login

@require_login
def page1():
    st.title("ページ1")
    st.write("ここにページ1の内容を追加します")

if __name__ == "__main__":
    page1()
