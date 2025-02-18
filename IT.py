import streamlit as st
import pandas as pd
import os
from pathlib import Path

# Streamlit UI Layout
st.set_page_config(page_title='Digital Assurance Tool', layout='wide')

# Sidebar for Source Selection
st.sidebar.title("📌 Select External Regulatory Source")
selected_source = st.sidebar.radio("Choose a source:", [
    "GST", "EDPMS/IDPMS", "TRACES / Form 26A", "Income Tax", "EPF"
])

# ✅ Correct Logo Path Handling
local_logo_path = Path("logo") / "kkc logo.png"  # Correct syntax using pathlib

# Display the logo (handle both local and hosted cases)
if local_logo_path.exists():
    st.image(str(local_logo_path), width=500)  # ✅ Works locally
else:
    # ✅ Use GitHub raw URL when hosting on Streamlit Cloud (replace with your actual repo details)
    logo_url = "https://raw.githubusercontent.com/your-username/your-repo/main/logo/kkc%20logo.png"
    st.image(logo_url, width=500)

# Title and Subheader
st.title("Digital Assurance Tool")
st.subheader("Statement containing compliance of conditions of Regulation 33 of LODR Regulations, 2015")

# ✅ Table Data
data = {
    "External Regulatory Information Source": [
        "[GST Portal](https://gst-extraction.streamlit.app/)", 
        "[TRACES Portal](https://tdsrecotool-8ev5hcapsychjewmbncbxs.streamlit.app/)", 
        "TRACES Portal", "EDPMS/IDPMS Report", "EDPMS/IDPMS Report"
    ],
    "Description": [
        "Revenue from operations (Goods and Services)",
        "Form 26 AS (Data updated till date ___)",
        "Total Tax Deducted at source",
        "Export Receivables covered under EDPMS",
        "Import Payables covered under IDPMS"
    ],
    "Amount as per Books of Account": ["", "", "", "", ""],
    "Amount as per External Regulatory Information Source": ["", "", "", "", ""],
    "Date on which the External Regulatory Information source was noted by the auditor/independent practitioner": ["", "", "", "", ""],
    "Reconciling items (C-D)": ["", "", "", "", ""],
    "Management Explanation": ["", "", "", "", ""]
}

df = pd.DataFrame(data)

# ✅ Apply custom CSS to properly justify table headers
st.markdown(
    """
    <style>
    table {
        width: 100% !important;
    }
    th {
        text-align: justify !important;
        padding: 10px;
    }
    td {
        padding: 8px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# ✅ Display Table with Clickable Links
st.write("### Table")

def make_clickable(val):
    """Convert URLs in the table into clickable links."""
    if val.startswith("[") and val.endswith(")"):
        return f'<a href="{val[val.find("(")+1:val.find(")")]}" target="_blank">{val[1:val.find(")")-1]}</a>'
    return val

df = df.applymap(make_clickable)
st.write(df.to_html(escape=False), unsafe_allow_html=True)
