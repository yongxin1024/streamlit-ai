import streamlit as st

from utils.ai_utils import get_chat_response
from utils.streamlit_utils import ai_message, human_message, openai_key_side_bar

st.subheader('💬Chat without memory')

api_key = openai_key_side_bar()

ai_message("Hello, I'm your AI assistant. How Can I help?")

query = st.chat_input()
if 'chat_message_cwom' not in st.session_state:
	st.session_state.chat_message_cwom = []

for message in st.session_state.chat_message_cwom:
	human_message(message['query'])
	ai_message(message['answer'])

if query:
	if not api_key:
		st.warning("Please input your api key")
		st.stop()
	human_message(query)
	with st.spinner('AI is thinking, please wait...'):
		# get Answer here
		answer = get_chat_response(prompt=query, openai_api_key=api_key)
		ai_message(answer)
		st.session_state.chat_message_cwom.append({'query': query, 'answer': answer})
