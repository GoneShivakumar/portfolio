import streamlit as st
from streamlit_lottie import st_lottie
import json


def text():

    coll, colm, colr = st.columns([1, 7, 1])

    with colm:
        st.title("ABOUT")
        st.markdown("""Results-driven Python Developer with over 2 years of
                    experience and a demonstrated track record of effectively
                    delivering impactful projects. Capable of simplifying
                    operations and decreasing manual effort through automation.
                    Key projects include effective PDF data extraction,
                    development of insightful Power BI dashboards for HR data,
                    and the comprehensive automation of Excel dashboards
                    utilizing Selenium, APIs, Plotly, and Streamlit. Demonstrated
                    ability to do EDA, transform and model data, and drive datadriven decision-making. Published articles on GeeksforGeeks,
                    Seeking to bring technical experience and innovation to a fastpaced team.""")

    with coll:
        for i in range(2):
            st.write("")
        st.image('P 1365.jpg')

    col1,col2,col3 = st.columns([1,7,2])

    with col2:
        st.header("Contact Details")
        st.markdown("""shivakumargone91@gmail.com
                        \nWarangal, Telangana
                        """)

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