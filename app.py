import streamlit as st
from utils import get_screen_width_height
from start import start
from mobile.start import start_mobile

st.set_page_config(
        layout='wide',
        page_title='Mesothelioma Spacial Atlas',
        page_icon="./assets/figures/meso_ribbon.png",
        # initial_sidebar_state="collapsed",
)

st.elements.utils._shown_default_value_warning=True

width, height = get_screen_width_height()
# st.write(width)
if int(width) < 600 :  # suppose it is mobile device
    start_mobile()
else:
    start()