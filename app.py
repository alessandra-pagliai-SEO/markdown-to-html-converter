import streamlit as st
import markdown

st.set_page_config(page_title="Markdown Viewer", layout="wide")

st.title("Markdown → HTML Viewer")

uploaded_files = st.file_uploader(
    "Carica uno o più file Markdown",
    type=["md"],
    accept_multiple_files=True
)

if uploaded_files:

    file_names = [file.name for file in uploaded_files]
    selected_file = st.sidebar.selectbox("Seleziona una pagina", file_names)

    for file in uploaded_files:
        if file.name == selected_file:

            md_content = file.read().decode("utf-8")

            html = markdown.markdown(
                md_content,
                extensions=["extra", "toc", "tables", "fenced_code"]
            )

            st.markdown("### Preview")

            st.components.v1.html(
                html,
                height=800,
                scrolling=True
            )

else:
    st.info("Carica file Markdown per visualizzare la pagina HTML.")
