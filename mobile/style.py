import streamlit as st

footer="""
<style>
  
    .image 
    { 
        padding: 5px;
        transition: transform .2s;
    }


    .image:hover {  
        transform: scale(1.5);
        transition: 0.2s;
    }
    
    .footer {
        position: relative;
        width: 100%;
        left: 0;
        bottom: 0;
        background-color: white;
        margin-top: auto;
        color: black;
        padding: 24px;
        text-align: center;
    }
</style>

<div class="footer">
<p style="font-size:  13px">Osmanbeyoglulab.com </p>
<p style="font-size:  13px">© 2023 All rights reserved. </p>
<a href="https://hillman.upmc.com/"><img class="image" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7c7pXIkFgMPVM2csVE6MenUFLEsgF5beCeMJzogkPkXPC4xEo9OTHf6nVpqsb3PvisRk&usqp=CAU"alt="github" width="60" height=45"></a>
<a href="https://www.pitt.edu/"><img class="image" src="https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/University_of_Pittsburgh_seal.svg/300px-University_of_Pittsburgh_seal.svg.png"alt="github" width="40" height="40"></a>
<a href="https://github.com/osmanbeyoglulab"><img class="image" src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="github" width="40" height="40"></a>
<a href="https://twitter.com/hosmanbeyoglu?lang=en"><img class="image" src="https://upload.wikimedia.org/wikipedia/commons/6/6f/Logo_of_Twitter.svg"alt="twitter" width="40" height="37"></a>
<a href="https://scholar.google.com/citations?user=YzCsmdgAAAAJ&hl=en&inst=7044483460239389945"><img class="image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Google_Scholar_logo.svg/512px-Google_Scholar_logo.svg.png"alt="github" width="40" height="40"></a>
<p style="font-size:  10px">&#160</p>
</div>

"""


page_style = """
    <style>
        #MainMenu {visibility: hidden;} 
        footer {visibility: hidden;} 
    </style>
"""


def define_layout(max_width, padding_top='0rem', padding_right='0rem', padding_left='0rem', padding_bottom='0rem'):

    # # add page to relative width
# max_width_str = f"max-width: {63.5}%;"
# st.markdown(f"""
#     <style>
#     .appview-container .main .block-container{{{max_width_str}}}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )   

    st.markdown(
        f"""
        <style>
            .appview-container .main .block-container{{
                max-width: {max_width};
                padding-top: {padding_top};
                padding-right: {padding_right};
                padding-left: {padding_left};
                padding-bottom: {padding_bottom};
            }}
          
        </style>
        """,
        unsafe_allow_html=True,
    )
