import streamlit as st
from style import define_layout

def contact_page():
    
    max_width = '90%'
    padding_top = '1rem'
    padding_right = '0rem'
    padding_left = '10rem'
    padding_bottom = '0rem'
    define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
   

    a, b = st.columns([1, 1.6 ])
    a.image('https://wexfordscitech.com/wp-content/uploads/2021/03/Assembly-web-5.png')
    a.markdown("""<span style="font-size:16px;">University of Pittsburgh, UPMC Hillman Cancer Center, Assembly Building</span>""", unsafe_allow_html=True)
    a.markdown("""<span style="font-size:14px;">Hatice Osmanbeyoglu<br>Principal Investigator<br>✉️ osmanbeyogluhu@pitt.edu</span>""", unsafe_allow_html=True)
    a.markdown("""<span style="font-size:14px;">Xiaojun Ma<br>Senior Software Engineer<br>✉️ xim33@pitt.edu</span>""", unsafe_allow_html=True)
    
    b.markdown("""<div style="width: 100%"><iframe width="100%" height="600" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q=5051%20Centre%20Avenue%20Pittsburgh,%20PA%2015213+(My%20Business%20Name)&amp;t=p&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"><a href="https://www.maps.ie/distance-area-calculator.html">measure distance on map</a></iframe></div>""", unsafe_allow_html=True)

 