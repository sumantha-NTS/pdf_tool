import streamlit as st
from streamlit.web import cli as stcli
import sys
from streamlit import runtime
from src.config import config


st.set_page_config(
    page_title="PDF Tool",
    page_icon=":wave:",
    layout="wide",
)


def main():
    st.markdown(
        """
    # 📚 PDF Tool

    #### Welcome to the PDF Tool. Your one-stop solution for PDF processing, conversion, and information extraction.
    """
    )


if __name__ == "__main__":
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
