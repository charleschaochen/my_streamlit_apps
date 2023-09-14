# 导入所需的库
import streamlit as st
import openai


with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"


# 设置OpenAI API密钥
openai.api_key = openai_api_key

# 创建一个输入框，让用户输入他们的问题
question = st.text_input("Enter your question")

# 当用户输入他们的问题后，使用GPT-3生成一个回答
if question:
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=question,
      temperature=0.5,
      max_tokens=100
    )
    st.write(response.choices[0].text.strip())
