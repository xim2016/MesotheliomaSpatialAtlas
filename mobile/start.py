import streamlit as st
from data_page import data_page
from mobile.contact_page import contact_page
from mobile.home_page import home_page
from mobile.citation_page import citation_page
# import hydralit_components as hc
from streamlit_option_menu import option_menu
from mobile.style import page_style, footer

st.set_page_config(
        layout='wide',
        page_title='Mesothelioma Spatial Atlas',
        page_icon="./assets/figures/meso_ribbon.png",
        # initial_sidebar_state="collapsed",
)

st.elements.utils._shown_default_value_warning=True


# def start_mobile():
#disable streamlit warning
# st.elements.utils._shown_default_value_warning=True

# st.set_page_config(
#         layout='wide',
#         page_title='Mesothelioma Spacial Atlas',
#         page_icon="./assets/figures/meso_ribbon.png",
#         # initial_sidebar_state="collapsed",
# )



st.markdown(page_style, unsafe_allow_html=True) ## Footer
# change font
# with open( "font.css" ) as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# max_width = 2000
# padding_top = 1.7
# padding_right = 0
# padding_left =  0
# padding_bottom = 0
# define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
    



menu_data = [
        {'icon': "🏠", 'label':"About"},
        {'icon':"📊",'label':"Data"},
        {'icon':"☎️",'label':"Contact"},
        {'icon':"📲",'label':"Citation"},
        
    ]
# over_theme = {'txc_inactive': 'white','menu_background':'#0f4d92','txc_active':'black'} #2e5090#0F52BA #048bbc #016490


# chosen_tab = hc.nav_bar(
#         menu_definition=menu_data,
#         override_theme=over_theme,
#         hide_streamlit_markers=False, 
#         # sticky_mode='pinned'
#     )

over_theme = {'txc_inactive': 'black','menu_background':'white','txc_active':'white','option_active':'#0f4d92'}
font_fmt = {'font-class':'h3','font-size':'50%'}

# chosen_tab = hc.option_bar(
#     option_definition=menu_data,
#     title='',
#     key='PrimaryOptionx',
#     override_theme=over_theme,
#     horizontal_orientation=True)

chosen_tab = option_menu(None, ["About", "Data",  "Contact", "Citation"], 
    icons=['🏠', '📊', "☎️", '📲'], 
    default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        # "icon": {"color": "orange", "font-size": "10px"}, 
        "nav-link": {"font-size": "11px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#0f4d92"},
    }
)


_, cm, _ = st.columns([1,15,1])
with cm: 

    if chosen_tab == "About":
        home_page()
        
    elif chosen_tab == "Contact":
        contact_page()

    elif chosen_tab == "Data":
        data_page()
    
    elif chosen_tab == "Citation":
        citation_page()

    # for i in range(1):
    #     st.markdown('#')
    st.divider()
    st.markdown(footer,unsafe_allow_html=True) 

