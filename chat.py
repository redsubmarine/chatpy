#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


import streamlit as st
from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title="뭐든지 물어봐")
st.title("뭐든 무러봐")


# In[3]:


def generate_response(input_text):
    llm = ChatOpenAI(temperature=0, model_name='gpt-4o')
    st.info(llm.predict(input_text))

with st.form('Question'):
    text = st.text_area('질문 입력:', 'What types of text models does OpenAI provide?')
    submitted = st.form_submit_button("Send")
    generate_response(text)


