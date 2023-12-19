import streamlit as st
from streamlit_lottie import st_lottie
import json
import base64


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def text():
    col1, col2, col3 = st.columns([7, 1, 1])
    with col1:
        for i in range(10):
            st.write(" ")
        title = "<p style='font-family:Sans-serif; color:white; font-size: 50px;'><b>I'm GONE SHIVAKUMAR</b></p>"
        st.markdown(title, unsafe_allow_html=True)

        brief = "<p style='font-family:Sans-serif; color:white; font-size: 18px;'><b>A Python Developer based in India</b></p>"
        st.write(brief, unsafe_allow_html=True )

if __name__ == '__main__':

    st.set_page_config(page_title="Shivakumar-Portfolio", layout="wide", initial_sidebar_state="auto")
    set_background('b.jpg')

    with st.sidebar:
        with open('animation_ln20m6yl.json', 'rb') as anime:
            url = json.load(anime)

        st_lottie(url, reverse=True,height=300,width=300,speed=1,loop=True,quality='high',key='Car')

    st.markdown("""
        <style>
        [data-testid="stSidebar"] {
        # box-shadow: rgb(0 0 0 / 80%) 0px 2px 1px -1px, rgb(0 0 0 / 80%) 0px 1px 1px 0px, rgb(0 0 0 / 70%) 0px 1px 28px 40px;
        border-radius : 15px;
        
        }
        [data-testid="stSidebarNav"] > ul {
        min-height: 45vh;
        }
        </style>
    """, unsafe_allow_html=True)
    st.snow()
    text()
