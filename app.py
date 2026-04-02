import streamlit as st
import markdown

st.set_page_config(page_title="Markdown HTML Viewer", layout="wide")

st.title("Markdown → HTML Page Viewer")

uploaded_files = st.file_uploader(
    "Upload Markdown files",
    type=["md"],
    accept_multiple_files=True
)

# CSS per migliorare la visualizzazione
custom_css = """
<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css"/>

<style>

body {
    background-color: #fafafa;
}

.markdown-body {
    box-sizing: border-box;
    max-width: 900px;
    margin: 40px auto;
    padding: 45px;
    background: white;
    border-radius: 8px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
}

/* headings */
.markdown-body h1 {
    border-bottom: 2px solid #eee;
    padding-bottom: .3em;
}

.markdown-body h2 {
    border-left: 4px solid #4CAF50;
    padding-left: 10px;
}

/* tables */
.markdown-body table {
    border-collapse: collapse;
    width: 100%;
    margin: 25px 0;
}

.markdown-body th,
.markdown-body td {
    border: 1px solid #ddd;
    padding: 10px;
}

.markdown-body th {
    background-color: #f6f8fa;
    text-align: left;
}

/* code blocks */
.markdown-body pre {
    background: #f6f8fa;
    padding: 15px;
    border-radius: 6px;
    overflow-x: auto;
}

/* blockquotes */
.markdown-body blockquote {
    border-left: 4px solid #ccc;
    padding-left: 15px;
    color: #666;
    margin-left: 0;
}

</style>
"""

if uploaded_files:

    file_names = [file.name for file in uploaded_files]

    selected_file = st.sidebar.selectbox(
        "Select page",
        file_names
    )

    for file in uploaded_files:

        if file.name == selected_file:

            md_content = file.read().decode("utf-8")

            html = markdown.markdown(
                md_content,
                extensions=[
                    "extra",
                    "tables",
                    "fenced_code",
                    "toc",
                    "pymdownx.superfences"
                ]
            )

            full_html = f"""
            {custom_css}
            <article class="markdown-body">
            {html}
            </article>
            """

            st.components.v1.html(
                full_html,
                height=900,
                scrolling=True
            )

else:
    st.info("Upload one or more Markdown files to preview them as HTML pages.")
