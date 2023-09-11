import streamlit as st
from PIL import Image
from descriptions import Desc
from style import define_layout

@st.cache_data
def load_homeImg():
    img =  Image.open('./assets/figures/home.png')
    st.image(img)  

def home_page():

    max_width = '90%'  # '1900px'
    padding_top = '2.5rem'
    padding_right = '0rem'
    padding_left = '10rem'
    padding_bottom = '0rem'
    define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
    
    title = '<p style="font-family:sans-serif; color:#5f6060;background-color:white; font-size: 28px; line-height: 60px; padding-top: 0px; padding-bottom: 0px;border-radius: 5px; font-weight: bold;text-align: center">The Human Spatial Atlas of Malignant Mesothelioma</p>'  #sans-serif   Soin Sans Pro
    st.markdown(title, unsafe_allow_html=True)
    # _,m0, _ =  st.columns([1,40,1])
    # m0.markdown(title, unsafe_allow_html=True)

    _,m1,_ = st.columns([1,5,1])
    # _,m2_,_ = st.columns([1,40,1])
    
    with m1:  
        
        st.markdown("#")
        load_homeImg()
        


    #     # st.markdown('---')
    # with m2_:
        st.markdown("#")
        st.markdown(f"<p style='text-align: justify; color: black; font-size: 14px'>{Desc.Abstract}</h4>", unsafe_allow_html=True) 
        st.markdown("#")
        st.markdown(' Read our paper from here 👉 https://www.biorxiv.org/content/10.1101/2023.09.06.556559v1')    

       
    