import sys

import streamlit as st
from streamlit import runtime
from streamlit.web import cli as stcli


def main():
    pages = {
        "Solutions": [
            st.Page("src/pages/welcome.py", title="Welcome", icon="👋"),
            st.Page("src/pages/split_pdf.py", title="Split PDF", icon="📖"),
            st.Page("src/pages/merge_pdf.py", title="Merge PDF", icon="📒"),
            # st.Page("src/pages/merge_pdf.py", title="Detect PDF layout", icon="📓"),
        ]
    }

    pg = st.navigation(
        pages,
        position="sidebar",
    )
    pg.run()


if __name__ == "__main__":
    if runtime.exists():
        main()
    else:
        sys.argv = [
            "streamlit",
            "run",
            sys.argv[0],
            "--server.port",
            "8111",
            "--server.address",
            "0.0.0.0",
            "--server.headless",
            "true",
            "--theme.base",
            "light",
        ]
        sys.exit(stcli.main())
