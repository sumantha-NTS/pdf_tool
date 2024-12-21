import streamlit as st
from streamlit.web import cli as stcli
import sys
from streamlit import runtime
from src.config import config


st.set_page_config(
    page_title="PDF-Hive",
    page_icon="📖",
    layout="wide",
)


st.markdown(
    """
# 📚 PDF-Hive

#### Welcome to the PDF-pal tool. Your bustling hub for all your PDF needs.
"""
)
