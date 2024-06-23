import streamlit as st
from src.services import pdf_services
from io import BytesIO
from PyPDF2 import PdfReader
import base64

st.set_page_config(page_title="Split PDF", page_icon=":book:", layout="wide")

with st.sidebar:
    file = st.file_uploader("Upload a file", type="pdf")
    pages = st.text_input("Enter the pages to split (e.g. 1-2,3)", value="1")
    submit = st.button("Submit", type="primary", disabled=False, use_container_width=True)


if submit:
    if file is None:
        st.error("Please upload a file")
        st.stop()

    pdf_file = PdfReader(BytesIO(file.getvalue()))

    with st.sidebar:
        st.success(f"{len(pdf_file.pages)} pages found")

    with st.spinner("Splitting PDF..."):
        split_pages = pages.split(",")
        result = pdf_services.split_pdf(pdf_file, pages=split_pages)

    st.subheader("Results")

    tabs = st.tabs([f"Page {i}" for i in split_pages])

    for i, page in enumerate(result):
        if page[0] == "error":
            st.error(page[1])
            continue

        pdf_base64 = base64.b64encode(page[1]).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="1400" height="700" type="application/pdf"></iframe>'

        # Display file in PDF format
        tabs[i].markdown(pdf_display, unsafe_allow_html=True)
