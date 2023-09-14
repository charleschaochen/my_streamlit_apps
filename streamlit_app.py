# 导入streamlit库
import streamlit as st

# 创建一个输入框，让用户输入他们的名字
name = st.text_input("Enter your name")

# 当用户输入他们的名字后，显示一个问候语
if name:
    st.write(f"Hello, {name}!")

# 运行这个Streamlit应用，你需要在命令行中输入以下命令：
# streamlit run your_script.py
