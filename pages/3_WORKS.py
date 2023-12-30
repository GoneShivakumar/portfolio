import streamlit as st
from streamlit_lottie import st_lottie
import json


def text():

    st.subheader("Excel Dashboards Automation:")
    st.markdown("""◾  Implemented automation by collecting data from
                    diverse sources (ApTest, JIRA, Database) using
                    Selenium and APIs.
                    \n◾  Stored, connected, and processed data in a database,
                    enhancing data cohesion.
                    \n◾  Transformed Excel formulas into Python scripts.
                    \n◾  Created an interactive web user interface (UI) using
                    Streamlit, generated charts with Plotly.
                    \n◾  Achieved a remarkable 95% reduction in manual efforts
                    through streamlined automation.""")
    st.divider()
    st.subheader("Power BI Dashboard for HR Data:")
    st.markdown("""◾ Conducted exploratory data analysis (EDA) to derive
                    actionable insights.
                    \n◾ Loaded, transformed, and modeled data in Power BI
                    Desktop for quick access.
                    \n◾ Designed interactive dashboards for HR data,
                    facilitating data-driven decision-making.""")
    st.divider()
    st.subheader("PDF Extraction Project:")
    st.markdown("""◾ Developed Python scripts to efficiently extract data
                    from editable PDFs, significantly reducing manual
                    effort.""")



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