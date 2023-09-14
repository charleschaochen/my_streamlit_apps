# 导入所需的库
import streamlit as st
import openai

# 设置OpenAI API密钥
openai.api_key = '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'

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
