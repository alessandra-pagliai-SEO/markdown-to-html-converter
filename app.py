import streamlit as st
import hashlib
import os

REPORT_DIR = "reports"

os.makedirs(REPORT_DIR, exist_ok=True)

st.set_page_config(layout="wide")

st.title("Markdown SEO Report Viewer")

# ---------- funzione hash ----------
def generate_hash(content):
    return hashlib.md5(content.encode()).hexdigest()

# ---------- controlla query param ----------
query_params = st.query_params
report_id = query_params.get("report")

# ---------- se il report arriva da URL ----------
if report_id:

    file_path = os.path.join(REPORT_DIR, f"{report_id}.md")

    if os.path.exists(file_path):

        with open(file_path, "r") as f:
            md_content = f.read()

        st.markdown(md_content)

    else:
        st.error("Report non trovato.")

# ---------- upload nuovo report ----------
else:

    uploaded_file = st.file_uploader(
        "Carica un report Markdown",
        type=["md"]
    )

    if uploaded_file:

        md_content = uploaded_file.read().decode("utf-8")

        report_hash = generate_hash(md_content)

        file_path = os.path.join(REPORT_DIR, f"{report_hash}.md")

        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(md_content)

        share_url = f"?report={report_hash}"

        st.success("Report caricato")

        st.markdown("### 🔗 Link condivisibile")
        st.code(share_url)

        st.markdown("---")

        st.markdown(md_content)
