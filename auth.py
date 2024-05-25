import streamlit as st

# 認証コード設定
PASSWORD = "a"

# セッションステートを初期化
def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

# ログインフォームの表示関数
def login():
    st.title("ログイン")
    password = st.text_input("認証コードを入力してください", type="password")
    if st.button("認証"):
        if password == PASSWORD:
            st.session_state.logged_in = True
            st.success("認証に成功しました")
        else:
            st.error("認証が間違っています")

# デコレータの実装
def require_login(func):
    def wrapper(*args, **kwargs):
        init_session_state()
        if not st.session_state.logged_in:
            login()
        else:
            func(*args, **kwargs)
    return wrapper
