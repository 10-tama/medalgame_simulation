# Streamlitをインポート
import streamlit as st

# タイトルを表示
st.title('Hello, Streamlit!')

# テキストを表示
st.write('StreamlitをVSCode上で起動しました。')

# ボタンの作成
if st.button('Say Hello'):
    st.write('Hello, World!')
