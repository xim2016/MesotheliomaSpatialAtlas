import streamlit as st
# from streamlit_option_menu import option_menu
from data_page import data_page
from data_page2 import data_page2
from contact_page import contact_page
from home_page import home_page
from citation_page import citation_page
import hydralit_components as hc

from style import page_style, footer


#disable streamlit warning
st.elements.utils._shown_default_value_warning=True

st.set_page_config(
        layout='wide',
        page_title='Mesothelioma Spacial Atlas',
        page_icon="./assets/figures/meso_ribbon.png",
        # initial_sidebar_state="collapsed",
)



st.markdown(page_style, unsafe_allow_html=True) ## Footer
# change font
with open( "font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# max_width = 2000
# padding_top = 1.7
# padding_right = 0
# padding_left =  0
# padding_bottom = 0
# define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
    



menu_data = [
        {'icon': "🏠", 'label':"About"},
        {'icon':"📊",'label':"Data"},
        {'icon':"📊",'label':"Data2"},
        {'icon':"☎️",'label':"Contact"},
        {'icon':"📲",'label':"Citation"},
        
    ]
over_theme = {'txc_inactive': 'white','menu_background':'#0f4d92','txc_active':'black'} #2e5090#0F52BA #048bbc #016490


chosen_tab = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        hide_streamlit_markers=False, 
        # sticky_mode='pinned'
    )


_, cm, _ = st.columns([1,15,1])
with cm: 
   
    if chosen_tab == "About":
        home_page()
        
    elif chosen_tab == "Contact":
        contact_page()

    elif chosen_tab == "Data":
        data_page()

    elif chosen_tab == "Data2":
        data_page2()
        
    elif chosen_tab == "Citation":
        citation_page()

    # for i in range(1):
    #     st.markdown('#')
    st.divider()
    st.markdown(footer,unsafe_allow_html=True) 

