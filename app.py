import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sistem Permintaan Master Material",
    page_icon="📦",
    layout="wide"
)

with open("sistem_permintaan_master_material.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(
    html_code,
    height=1800,
    scrolling=True
)
