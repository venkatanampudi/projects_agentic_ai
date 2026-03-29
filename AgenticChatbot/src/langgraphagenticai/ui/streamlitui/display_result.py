import json
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import streamlit as st

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message=None):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot" and user_message:
            for event in graph.stream({
                "messages": [HumanMessage(content=user_message)]
            }):
                print(event.values())

                for value in event.values():
                    print(value["messages"])

                    with st.chat_message("user"):
                        st.write(user_message)

                    messages = value["messages"]
                    last_message = messages[-1] if isinstance(messages, list) else messages

                    with st.chat_message("assistant"):
                        st.write(last_message.content)