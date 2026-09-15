import streamlit as st
import streamlit.components.v1 as components


# ==============================
# KONFIGURASI HALAMAN
# ==============================

st.set_page_config(
    page_title="Sistem Master Material",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==============================
# HILANGKAN UI STREAMLIT
# ==============================

st.markdown(
    """
    <style>

    /* Hilangkan menu Streamlit */
    #MainMenu {
        visibility: hidden;
    }


    /* Hilangkan header atas */
    header {
        visibility: hidden;
    }


    /* Hilangkan footer */
    footer {
        visibility: hidden;
    }


    /* Hilangkan tombol deploy */
    .stDeployButton {
        display:none;
    }


    /* Full screen content */
    .block-container {

        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;

        max-width: 100% !important;

    }


    /* Hilangkan whitespace */
    .main {
        padding:0 !important;
    }


    </style>
    """,
    unsafe_allow_html=True
)



# ==============================
# LOAD HTML WEBSITE
# ==============================

with open(
    "sistem_permintaan_master_material.html",
    "r",
    encoding="utf-8"
) as file:

    html_code = file.read()



# ==============================
# TAMPILKAN WEBSITE
# ==============================

components.html(
    html_code,
    height=2500,
    scrolling=False
)
