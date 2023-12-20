import streamlit as st
from streamlit_lottie import st_lottie
import json
import pandas as pd
import numpy as np

def text():

    preprocess = "https://www.geeksforgeeks.org/data-preprocessing-analysis-and-visualization-for-building-a-machine-learning-model/"
    powerbi = "https://www.geeksforgeeks.org/power-bi-how-to-create-calculated-measures/"
    text = "https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/"
    pdf2img = "https://www.geeksforgeeks.org/how-to-extract-images-from-pdf-in-python/"

    st.markdown("Note : All the articles are Published on <b>Geeks for Geeks</b>",unsafe_allow_html=True)
    column1,column2,coluumn3 = st.columns([1,2,1])
    with column2:
        st.subheader("Direct Publishments")

    col1, col2,col3 = st.columns(3)

    with col1:
        st.image("datapreprocessing.jpg")
        st.link_button("Data Preprocessing", preprocess)
    with col3:
        st.image("powerbi.jpg")
        for i in range(4):
            st.write("")
        st.link_button("Measures in Power BI", powerbi)

    co1,co2,co3 = st.columns(3)
    with co2:
        st.subheader("Improvements")
    st.write("")
    coll,colm,colr = st.columns(3)
    with coll:
        st.image("text.jpg")
        st.link_button("Extract Text from PDF", text)

    with colr:
        st.image("pdf2jpg.jpg")
        st.link_button("PDF to Image and Viceversa", pdf2img)

if __name__ == '__main__':
    st.set_page_config(page_title="Shivakumar-Portfolio", layout="centered", initial_sidebar_state="auto")

    st.markdown("""
                   <style>
                   [data-testid="stSidebar"] {
                   box-shadow: rgb(0 0 0 / 80%) 0px 2px 1px -1px, rgb(0 0 0 / 80%) 0px 1px 1px 0px, rgb(0 0 0 / 70%) 0px 1px 0px 0px;
                   border-radius : 15px;

                   }
                   [data-testid="stSidebarNav"] > ul {
                   min-height: 45vh;
                   }
                   [data-testid="baseLinkButton-secondary"] {
                   box-shadow: rgb(0 0 0 / 80%) 0px 2px 1px -1px, rgb(0 0 0 / 80%) 0px 1px 1px 0px, rgb(0 0 0 / 70%) 0px 10px 10px 1px;
                   }

                   </style>
               """, unsafe_allow_html=True)
    text()