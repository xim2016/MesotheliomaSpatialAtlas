import streamlit as st
from PIL import Image
from descriptions import Desc
from style import define_layout



def home_page():

    max_width = '90%'  # '1900px'
    padding_top = '2.5rem'
    padding_right = '0rem'
    padding_left = '10rem'
    padding_bottom = '0rem'
    define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
    
    title = '<p style="font-family:sans-serif; color:#5f6060;background-color:white; font-size: 46px; line-height: 60px; padding-top: 0px; padding-bottom: 0px;border-radius: 5px; font-weight: bold;text-align: center">The Human Spatial Atlas of Malignant Mesothelioma</p>'  #sans-serif   Soin Sans Pro
    st.markdown(title, unsafe_allow_html=True)

    st.divider()

    
    # with st.sidebar:
    #     st.write("")
    # from descriptions import Desc
    img =  Image.open('./assets/figures/home.png')
    
  
    a,_, b = st.columns([9,0.5,10])
    
    with a:  
        st.markdown("#")
        st.image(img)  

        # st.markdown('👉 Read our paper from here! https://onlinelibrary.wiley.com/doi/10.1002/jmv.28887')    


        # st.markdown('---')
    with b:
        # st.markdown(f"<p style='color: black; font-weight: bold'>Purpose</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: justify; color: black;'>{Desc.Abstract}</h4>", unsafe_allow_html=True) 
        
       
        