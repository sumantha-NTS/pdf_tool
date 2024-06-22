import streamlit as st
from src.services import pdf_services

st.set_page_config(page_title="Convert Scanned PDF", page_icon=":book:", layout="wide")

with st.sidebar:
    file = st.file_uploader("Upload a file", type="pdf")
    submit = st.button("Submit", type="primary", disabled=False, use_container_width=True)


if submit:
    if file is None:
        st.error("Please upload a file")
        st.stop()

    file_data = file.getvalue()

    result = pdf_services.process_pdf_pipeline(file=file_data, image_dpi=300, deskew=True, remove_background=False)

    st.download_button(label="Download", data=result, file_name="converted.pdf", mime="application/pdf")
