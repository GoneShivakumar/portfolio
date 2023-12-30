import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
import json
import pandas as pd
import numpy as np

def text():

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("EDUCATION")

    with col2:
        st.write('<b>"Vaagdevi Engineering College, Warangal"</b>', unsafe_allow_html=True)
        st.write("Bachelor of Technology in Computer Science and Engineering")
        st.write("Graduated 2021")
    st.divider()

    coll, colm = st.columns(2)

    with coll:
        st.subheader("WORK")

    with colm:
        st.write('<b>"HCL Technologies, Chennai"</b>',unsafe_allow_html=True)
        st.write("Software Engineer. September 2021 - present")
        st.write("Python Developer")
    st.divider()

    colle,colmi= st.columns(2)
    with colle:
        st.subheader("SKILLS")

    with colmi:
        tab1,tab2 = st.tabs(["Technichal Skills", "Tools and Libraries"])
        with tab1:
            dic = {'Skills':["python", "SQL", "Statistics", "ML", "Data Analytics", "Data Reporting", "Data Extraction", "Automation Engineering"], 'Rating':[10,10,10,10,10,10,10,10]}
            df = pd.DataFrame(dic)
            # chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            print(df)
            fig = px.bar(df, x="Skills", y="Rating", color="Skills")
            fig.update_layout(
                xaxis=dict(title="Skills", title_font=dict(family="Serif", size=18,color="#0A0909")),
                yaxis=dict(title="Rating",title_font=dict(family="Serif",size=18,color="#0A0909")))
            fig.update_xaxes(tickfont=dict(family='Serif',size=16,color='black',))
            fig.update_yaxes(tickfont=dict(family='Serif', size=16, color='black', ))
            st.plotly_chart(fig, use_container_width=True)
            # st.bar_chart(df,x="Skill",y="Rating", color=["#228B22"])

        with tab2:
            st.info("Power BI")
            st.info("Pandas")
            st.info("Plotly")
            st.info("Streamlit")
            st.info("numpy")
            st.info("Spcay")
            st.info("PyMuPDF")
            st.info("Regular Expressions")
            st.info("Selenium")
            st.info("Jupyter Notebook")

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
               [data-testid="stAlert"] {
               box-shadow: rgb(0 0 0 / 80%) 0px 2px 1px -1px, rgb(0 0 0 / 80%) 0px 1px 1px 0px, rgb(0 0 0 / 70%) 0px 10px 10px 1px;
               }
               </style>
           """, unsafe_allow_html=True)

    text()
