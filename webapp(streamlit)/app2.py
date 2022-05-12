import streamlit as st
import time


def btn(label="ボタン",key=None,onclick=None,done=None):
    if st.button(label,key=key,on_click=onclick) and done:
        done()

def pop(msg, done=None, interval=1):
    with st.spinner(msg):
        time.sleep(interval)
    if done:
        done()



def app():
    st.markdown('# ルイザ・グロス・ホロウィッツ賞')
    st.markdown('# 日本人受賞者を覚えよう')
    st.markdown('## 問題')
    st.markdown('生物学や生化学の研究者に贈られるルイザ・グロス・ホロウィッツ賞を現在、日本人で唯一受賞したのは誰？')
    col1, col2 = st.columns(2)
    with col1:
        btn(
            label="利根川進",
            done=lambda:[
                pop("'利根川進'が選択されました"),
                st.success("正解！")
                ]
            )
    with col2:
        btn(
            label="木村資生",
            done=lambda:[
                pop("'木村資生'が選択されました"),
                st.success("不正解！"),
                st.markdown('あなたはルイザ・グロス・ホロウィッツ賞の日本人受賞者を１人も覚えていません。'),
                time.sleep(1),
                st.markdown('木村資生さんは、生物学分野の業績を称える賞であるダーウィンメダルを日本人で唯一受賞している生物学者です')
                ]
            )