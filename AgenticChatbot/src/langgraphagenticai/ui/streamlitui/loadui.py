# loadui.py file for Streamlit 
import streamlit as st 
import os 

# import the config class 
from src.langgraphagenticai.ui.uiconfigfile import Config 

# create a class to load the streamlit UI 
class LoadStreamlitUI:

    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())

        with st.sidebar:  # this is for sidebar in the page
            # Get options from config 
            llm_options=self.config.get_llm_options()
            usecase_options=self.config.get_usecase_options()

            # creating LLM control 
            self.user_controls["selected_llm"]=st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"]=='Groq':
                # Model selection 
                model_options=self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"]=st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"]=st.session_state["GROQ_API_KEY"]=st.text_input("API Key", type="password")
                # Validate API Key 
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your GROQ API KEY to proceed. Don't have? Please refer:https://console.groq.com/keys")

            # Usecase selection 
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecases", usecase_options)
        return self.user_controls 