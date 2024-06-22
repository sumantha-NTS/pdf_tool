import streamlit as st

st.set_page_config(page_title="Convert Scanned PDF", page_icon=":book:", layout="wide")

with st.sidebar:
    file = st.file_uploader("Upload a file", type="pdf")
    submit = st.button("Submit", type="primary", disabled=True, use_container_width=True)
    st.warning("This feature is currently in development. Please try again later.")

if submit:
    if file is None:
        st.error("Please upload a file")
        st.stop()
