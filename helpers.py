import streamlit as st

from utils.helpers import load_css, load_js

from pages.sidebar import create_sidebar
from pages.upload import upload_page
from pages.footer import create_footer


# =====================================
# ACKERMAN SYSTEM CONFIGURATION
# =====================================

st.set_page_config(
    page_title="GEO SCAN PRO | Ackerman System",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================
# LOAD DESIGN SYSTEM
# =====================================

load_css("css/ackerman_theme.css")
load_css("css/components.css")
load_css("css/animations.css")


# =====================================
# LOAD EFFECTS
# =====================================

load_js("js/stars.js")
load_js("js/effects.js")


# =====================================
# SIDEBAR
# =====================================

create_sidebar()


# =====================================
# HERO SECTION
# =====================================

st.markdown(
"""
<div class="hero">

    <div class="system-tag">
        ACKERMAN TECHNOLOGY
    </div>


    <h1>
        GEO SCAN PRO
    </h1>


    <div class="subtitle">
        AUTONOMOUS TERRAIN INTELLIGENCE SYSTEM
    </div>


    <div class="status-line">
        ● SYSTEM ONLINE
    </div>


</div>
""",
unsafe_allow_html=True
)


# =====================================
# MAIN MODULE
# =====================================

upload_page()


# =====================================
# FOOTER
# =====================================

create_footer()