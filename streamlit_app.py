import streamlit as st
import os
import numpy as np
import pandas as pd
import urllib.request
from PIL import Image
import glob


def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)


md_files = sorted(
    [int(x.strip("Day").strip(".md")) for x in glob.glob1("content", "*.md")]
)

# Logo and Navigation
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("streamlit-logo-secondary-colormark-darktext.png"))
st.markdown("# 30 天学 Streamlit")

days_list = [f"第{x}天" for x in md_files]

query_params = st.experimental_get_query_params()

if query_params and query_params["challenge"][0] in days_list:
    st.session_state.day = query_params["challenge"][0]

selected_day = st.selectbox("开始挑战 👇", days_list, key="day", on_change=update_params)

with st.expander("关于 #30天学Streamlit"):
    st.markdown(
        """
    **#30天学Streamlit** 是一个旨在帮助你学习构建 Streamlit 应用的编程挑战。

    你将学会：
    - 如何搭建一个编程环境用于构建 Streamlit 应用
    - 构建你的第一个 Streamlit 应用
    - 学习所有好玩的、能用在 Streamlit 应用里的输入输出组件
    """
    )

# Sidebar
st.sidebar.header("关于 Streamlit")
st.sidebar.markdown(
    "[Streamlit](https://streamlit.io) 是一个 Python 库，能够用于使用 Python 创建可交互的、数据驱动的网页应用"
)

st.sidebar.header("相关资源")
st.sidebar.markdown(
    """
- [Streamlit 文档](https://docs.streamlit.io/)
- [一图流](https://docs.streamlit.io/library/cheatsheet)
- [书籍](https://www.amazon.com/dp/180056550X) (Getting Started with Streamlit for Data Science)
- [博客](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (How to master Streamlit for data science)
"""
)

st.sidebar.header("如何部署")
st.sidebar.markdown(
    "你可以使用 [Streamlit Community Cloud](https://streamlit.io/cloud)，点点鼠标即可完成 Streamlit 应用的部署"
)

# Display content
for i in days_list:
    if selected_day == i:
        st.markdown(f"# 🗓️ {i}")
        j = i.replace("第", "Day").replace("天", "")
        with open(f"content/{j}.md", "r") as f:
            st.markdown(f.read())
        if os.path.isfile(f"content/figures/{j}.csv") == True:
            st.markdown("---")
            st.markdown("### 附图")
            df = pd.read_csv(f"content/figures/{j}.csv", engine="python")
            for i in range(len(df)):
                st.image(f"content/images/{df.img[i]}")
                st.info(f"{df.figure[i]}: {df.caption[i]}")
