from style import define_layout
import streamlit as st
from descriptions import Desc

def citation_page():
    
    max_width = '90%'
    padding_top = '2.5rem'
    padding_right = '0rem'
    padding_left = '10rem'
    padding_bottom = '0rem'
    define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
   
    st.markdown(f"<p style='color: black; font-weight: bold'>Citation guidelines for the Mesothelioma Spatial Atlas</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: justify; color: black;'>{Desc.Citation}</h4>", unsafe_allow_html=True) 

    st.markdown(f"<p style='color: black; font-weight: bold'>General citation for the Mesothelioma Spatial Atlas</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: justify; color: black;'>{Desc.Citation_general}</h4>", unsafe_allow_html=True) 

    st.markdown(f"<p style='color: black; font-weight: bold'>Specific citation for image, chanel or data</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: justify; color: black;'>{Desc.Citation_specific}</h4>", unsafe_allow_html=True) 