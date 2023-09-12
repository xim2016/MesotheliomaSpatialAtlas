import streamlit as st
from streamlit_js_eval import streamlit_js_eval
st.write(f"Screen width is {streamlit_js_eval(js_expressions='screen.width', key = 'SCR')}")