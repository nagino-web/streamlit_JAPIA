import streamlit as st
from auth import require_login


# メインの内容
@require_login
def main_page():
    st.title("WELCOME HH120 TOOL WEB APPS")
    st.write("あなたは認証済みです")

if __name__ == "__main__":
    main_page()
