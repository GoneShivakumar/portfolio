import streamlit as st
from streamlit_lottie import st_lottie
import json
import pandas as pd
import numpy as np
import openpyxl

def text():

    def click():
        names=[]
        emails=[]
        sub=[]
        messages=[]
        names.append(st.session_state['name'])
        emails.append(st.session_state['email'])
        sub.append(st.session_state['sub'])
        messages.append(st.session_state['message'])
        dic = {'name': names, 'email': emails, 'subject': sub, 'message': messages}
        df = pd.DataFrame(dic)
        print(df)
        try:
            existing_df = pd.read_excel('messages.xlsx', engine='openpyxl')
            comb_df = pd.concat([existing_df, df], ignore_index = True)
            comb_df.to_excel('messages.xlsx', index=False)
        except FileNotFoundError:
            df.to_excel('messages.xlsx', index=False)

    col1,col2,col3 = st.columns([1,3,1])
    with col2:
        st.write("<b>Get in touch with me</b>", unsafe_allow_html=True)
        with st.form('form', clear_on_submit=True):
            name = st.text_input("Name", key='name')
            email = st.text_input("Email", key='email')
            subject = st.text_input("Subject", key='sub')
            message = st.text_area("Message", key='message')
            submit = st.form_submit_button('Submit', on_click = click)


if __name__ == '__main__':
    st.set_page_config(page_title="Shivakumar-Portfolio", layout="centered", initial_sidebar_state="auto")
    text()