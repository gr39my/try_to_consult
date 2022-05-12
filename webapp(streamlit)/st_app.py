import app1
import app2
import streamlit as st
PAGES = {
    "パスワード生成くん": app1,
    "ルイザ・グロス・ホロウィッツ賞クイズ": app2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()