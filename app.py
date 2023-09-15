import streamlit as st
from utils import get_screen_width_height
from start_page import start_page
from mobile.start_page_mobile import start_page_mobile

st.set_page_config(
        layout='wide',
        page_title='Mesothelioma Spacial Atlas',
        page_icon="./assets/figures/meso_ribbon.png",
        # initial_sidebar_state="collapsed",
)

st.elements.utils._shown_default_value_warning=True

width = get_screen_width_height()

mobile_device = int(width) < 600

if mobile_device :  #  mobile device detected
    start_page_mobile()
else:
    start_page()
