from style import define_layout
import streamlit as st
# from descriptions import Desc

def citation_page():
    
    max_width = '90%'
    padding_top = '2.5rem'
    padding_right = '0rem'
    padding_left = '10rem'
    padding_bottom = '0rem'
    define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
   
    Citation = "While we encourage you to use these resources for your research and commercial purposes, we want to ensure that our content is given proper citation in all cases where it is used."

    Citation_general = "If you cite or display any content, or reference this website, in any format, written or otherwise, including print or web publications, presentations, grant applications, websites, other online applications such as blogs, or other works, you must include a reference to our website:https://mesotheliomaspatialatlas.streamlit.app."
    Citation_specific = "If you use images, or reference a specific image type, or other data downloaded from the site, in addition to citing the Mesothelioma Spacial Atlas, please also cite the specific image,  or data used and the URL that links directly to that information in a manner that will allow a third party to navigate to that image or data on the site."

    st.markdown(f"<p style='color: black; font-weight: bold'>Citation guidelines for the Mesothelioma Spatial Atlas</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: justify; color: black;'>{Citation}</h4>", unsafe_allow_html=True) 

    st.markdown(f"<p style='color: black; font-weight: bold'>General citation for the Mesothelioma Spatial Atlas</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: justify; color: black;'>{Citation_general}</h4>", unsafe_allow_html=True) 

    st.markdown(f"<p style='color: black; font-weight: bold'>Specific citation for image, chanel or data</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: justify; color: black;'>{Citation_specific}</h4>", unsafe_allow_html=True) 