import streamlit as st
import re

st.set_page_config(page_title="Markdown Viewer", layout="wide")

st.title("Markdown Report Viewer")

uploaded_files = st.file_uploader(
    "Upload Markdown files",
    type=["md"],
    accept_multiple_files=True
)

def linkify(text):
    """
    Trasforma URL plain text in link cliccabili
    """
    url_pattern = r'(https?://[^\s|]+)'
    return re.sub(url_pattern, r'[\1](\1)', text)


if uploaded_files:

    file_names = [f.name for f in uploaded_files]

    selected_file = st.sidebar.selectbox(
        "Select page",
        file_names
    )

    for file in uploaded_files:

        if file.name == selected_file:

            md_content = file.read().decode("utf-8")

            # rende gli URL cliccabili
            md_content = linkify(md_content)

            st.markdown(
                md_content,
                unsafe_allow_html=True
            )

else:

    st.info("Upload a Markdown file to preview it.")
