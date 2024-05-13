import streamlit as st

with st.form(key='profile_form'):
    # テキストボックス
    name = st.text_input('name')
    address = st.text_input('address')

    age = st.slider('年齢を選択してください', 0, 100)

    # 複数選択
    hobby = st.multiselect(
        '趣味',
        ('読書','プログラミング', '野球', 'サッカー', 'バドミントン')
    )
    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn =  st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ　{name}　さん  ({address})')
        st.text(f'年齢: {age}')
        st.text(f'趣味: {",".join(hobby)}')
