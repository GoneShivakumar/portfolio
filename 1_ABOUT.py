import streamlit as st
from streamlit_lottie import st_lottie
import json


def text():

    coll, colm, colr = st.columns([1, 7, 1])

    with colm:
        st.title("ABOUT")
        st.markdown("Hi there! I am Gone Shivakumar!, I've been coding for over 1 years now. "
                 "As a Full Stack developer I've worked both with startups and large corporations "
                 "to help build & scale their companies. Along the journey I realised my passion "
                 "existed in helping others excel and pursue their dreams as upcoming developers. "
                 "I enjoy taking complex problems and turning them into simple and beautiful interface design. "
                 "I also love the logic and structure of coding and always strive to write elegant and efficient code")

    with coll:
        for i in range(2):
            st.write("")
        st.image('P 1365.jpg')

    col1,col2,col3 = st.columns([1,7,2])

    with col2:
        st.header("Contact Details")
        st.markdown("""Shivakumar
                        \n1/7,North Street,
                        \nS Ogaiyur, sdfsadfs
                        \nIndia Tamilnadu, 606 204
                        \n+91 123423545
                        \n23423423sdfsd@gmail.com""")

    resume = 'MyResume.pdf'
    with col3:
        for i in range(2):
            st.write("")
        with open(resume, 'rb') as file:
            st.download_button(label="Download Resume", data=file, file_name='shivakumar_resume.pdf',mime='pdf',)

if __name__ == '__main__':

    st.set_page_config(page_title="Shivakumar-Portfolio", layout="wide", initial_sidebar_state="auto")

    st.markdown("""
            <style>
            [data-testid="stSidebar"] {
            box-shadow: rgb(0 0 0 / 80%) 0px 2px 1px -1px, rgb(0 0 0 / 80%) 0px 1px 1px 0px, rgb(0 0 0 / 70%) 0px 1px 0px 0px;
            border-radius : 15px;

            }
            [data-testid="stSidebarNav"] > ul {
            min-height: 45vh;
            }
            [data-testid="baseButton-secondary"] {
            box-shadow: rgb(0 0 0 / 80%) 0px 2px 1px -1px, rgb(0 0 0 / 80%) 0px 1px 1px 0px, rgb(0 0 0 / 70%) 0px 10px 10px 1px;
            }
            </style>
        """, unsafe_allow_html=True)

    text()