import streamlit as st
import pandas as pd
from auth import require_login

@require_login
def contents():

    # データ分析関連
    df = pd.read_csv('./data/平均気温.csv', index_col='月')
    st.line_chart(df)


if __name__ == "__main__":
    contents()


