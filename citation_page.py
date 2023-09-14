from style import define_layout
import streamlit as st
# from descriptions import Desc

def citation_page():
    
    max_width = '90%'
    padding_top = '1rem'
    padding_right = '0rem'
    padding_left = '13rem'
    padding_bottom = '0rem'
    define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
   
    
    # st.markdown(f"<p style='color: black; font-weight: bold'>Citation guidelines for the Mesothelioma Spatial Atlas</h2>", unsafe_allow_html=True)
    st.markdown("**Citation guidelines for the Mesothelioma Spatial Atlas**")
    st.markdown("While we encourage you to use these resources for your research and commercial purposes, we want to ensure that our content is given proper citation in all cases where it is used.") 
    
    st.markdown("###")
    # st.markdown(f"<p style='color: black; font-weight: bold'>General citation for the Mesothelioma Spatial Atlas</h3>", unsafe_allow_html=True)
    # st.markdown(f"<p style='text-align: justify; color: black;'>{Citation_general}</h4>", unsafe_allow_html=True) 
    st.markdown("**General citation for the Mesothelioma Spatial Atlas**") 
    st.markdown("If you cite or display any content, or reference this website, in any format, written or otherwise, including print or web publications, presentations, grant applications, websites, other online applications such as blogs, or other works, you must include a reference to our website: https://mesotheliomaspatialatlas.streamlit.app.")

    st.markdown("###")
    # st.markdown(f"<p style='color: black; font-weight: bold'>Specific citation for image, chanel or data</h3>", unsafe_allow_html=True)
    st.markdown("**Specific citation for image, chanel or data**")
    st.markdown("If you use images, or reference a specific image type, or other data downloaded from the site, in addition to citing the Mesothelioma Spacial Atlas, please also cite the specific image,  or data used and the URL that links directly to that information in a manner that will allow a third party to navigate to that image or data on the site.") 
    
    st.markdown("###")
    # st.markdown(f"<p style='color: black; font-weight: bold'>Citation</h3>", unsafe_allow_html=True)
    st.markdown("**Citation**")
    st.markdown("If you find the images or data from this website helpful, please cite the paper: https://www.biorxiv.org/content/10.1101/2023.09.06.556559v1")

    st.markdown("#")