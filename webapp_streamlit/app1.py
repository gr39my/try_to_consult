import streamlit as st
import pandas as pd
import numpy as np

import string
import secrets


def pass_gen(size=12):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    # 記号を含める場合
    # chars += '%&$#()'

    return ''.join(secrets.choice(chars) for x in range(size))

#print(pass_gen(10))


def app():
    st.title('パスワード生成くん')
    # DataFrame の表示
    st.markdown('- 読み込むごとに数値をランダムに生成')
    st.markdown('- 各列でのソートが可能')
    df = pd.DataFrame(
        {
            '8桁':[pass_gen(8),pass_gen(8),pass_gen(8),pass_gen(8),pass_gen(8)],
            '10桁':[pass_gen(10),pass_gen(10),pass_gen(10),pass_gen(10),pass_gen(10)],
            '16桁':[pass_gen(16),pass_gen(16),pass_gen(16),pass_gen(16),pass_gen(16)]
        }
    )
    st.dataframe(df) 