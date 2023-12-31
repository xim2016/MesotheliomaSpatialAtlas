
import streamlit as st
from st_clickable_images import clickable_images
from PIL import Image
from utils import get_orderedList, get_imageNames, load_HEImages, load_coreImages, show_plotly_image, get_core_feature, get_coreStatistic
from style import define_layout
import os


def disable_other_checkboxes(*other_checkboxes_keys):
    # if current one is trun to false, reset it to true
    if st.session_state[other_checkboxes_keys[-1]] == False:
        st.session_state[other_checkboxes_keys[-1]] = True
        
    for checkbox_key in other_checkboxes_keys[:-1]:
        st.session_state[checkbox_key] = False
        
def get_current_checkedBox(options):
    key = list(options.keys())[list(options.values()).index(True)]
    return (key)      


def data_page2():
    
    
    max_width = '100%'
    padding_top = '2.5rem'
    padding_right = '0rem'
    padding_left = '0rem'
    padding_bottom = '0rem'
    define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
    
    st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: white;
        }
    </style>
    """, unsafe_allow_html=True)

    PATH_IMG_TMA = "./data/core_image"
    
    PATH_IMG_HE = "./data/core_image/H&E_level1"
    path_img_HE_logo = "./data/core_image/H&E_logo" 

    PATH_IMG_panel1 = "./data/core_image/H&E_level1"  
    PATH_IMG_panel1_logo = "./data/core_image/panel1_logo4" 

    PATH_IMG_panel2 = "./data/core_image/H&E_level1"  
    PATH_IMG_panel2_logo = "./data/core_image/panel1_logo4" 

    c1_IDs = ["Institute", "Classification","CaseType","subtype", "Grade"]
    c1_names = ["Institute", "Classification","Case type","Subtype", "Tumor grade"]
    c1 = st.columns([3,3,3,3,3])
    cs1 = dict()
    for i in range(5):
        cs1[i] = c1[i].selectbox(
                    c1_names[i],
                    get_orderedList(c1_IDs[i]),
                    key = c1_IDs[i]
                )
    

    c2_IDs = ["Gender", "DiagnosisAge","AsbestosExposure","Race", "smoking"]
    c2_names = ["Gender", "Diagnosis age","Asbestos exposure","Race", "Smoking"]
    c2 = st.columns([3,3,3,3,3])
    cs2 = dict()
    for i in range(5):
        cs2[i] = c2[i].selectbox(
                    c2_names[i],
                    get_orderedList(c2_IDs[i]),
                    key = c2_IDs[i]
                )
        
    with st.sidebar:
        st.markdown("### Choose the core of interest", True)
        #H&E use image_names , others use core_ids as image names
        image_names, core_ids, core_ids2 = get_imageNames(cs1, cs2, c1_IDs,c2_IDs)
        
        
        
        images, showedImage_names, showedCore_ids, showedCore_ids2 = load_HEImages(path_img_HE_logo , list(image_names), list(core_ids), list(core_ids2))


        with st.empty():
            if len(images) > 0 :
                clicked = clickable_images(
                    images, 
                    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                    img_style={"margin": "10px", "height": "70px"},
                )
            else:
                st.write("No core for current selection.")


      
    
    # st.markdown("#### Image type")
    
    st.divider()

    vargs0 = ["H&E"]
    vargs1 = ["Multi", "CD4", "CD8", "CD20", "CD68", "FOXP3", "panCK"]
    vargs2 = ["Multi ", "CD56", "CD11c", "BAP1","NF2", "MTAP","LAG3"] 
    vargs = vargs0 +  vargs1 + vargs2   
    
    option2dir = {"H&E": f"{PATH_IMG_HE}",
                "Multi": f"{PATH_IMG_TMA}/panel1/multi",
                "CD4": f"{PATH_IMG_TMA}/panel1/CD4",
                "CD8": f"{PATH_IMG_TMA}/panel1/CD8",
                "CD20": f"{PATH_IMG_TMA}/panel1/CD20",
                "CD68": f"{PATH_IMG_TMA}/panel1/CD68",
                "FOXP3": f"{PATH_IMG_TMA}/panel1/FOXP3",
                "panCK": f"{PATH_IMG_TMA}/panel1/panCK",
                "Multi ": f"{PATH_IMG_TMA}/panel2/multi2",
                "CD56": f"{PATH_IMG_TMA}/panel2/CD56",
                "CD11c": f"{PATH_IMG_TMA}/panel2/CD11c",
                "BAP1": f"{PATH_IMG_TMA}/panel2/BAP1",
                "NF2": f"{PATH_IMG_TMA}/panel2/NF2",
                "MTAP": f"{PATH_IMG_TMA}/panel2/MTAP",
                "LAG3": f"{PATH_IMG_TMA}/panel2/LAG3"
    }
    
    
    # if clicked == -1: clicked = 0
    
    # images = load_coreImages(showedImage_names[clicked],showedCore_ids[clicked],showedCore_ids2[clicked] )
    # ls_images = list(images.values())
    
    # clicked_chanel = clickable_images(
    #                     ls_images, 
    #                     div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    #                     img_style={"margin": "2px", "height": "70px"},
    #                     key = i,
    #                 )
    # st.markdown( '<p style="font-size: 14px;  font-weight: bold; text-align: center"> &#160 &#160 &#160      H&E      &#160 &#160 &#160 &#160 &#160     Multi  &#160 &#160 &#160 &#160 &#160   CD4    &#160 &#160 &#160 &#160 &#160     CD8     &#160 &#160 &#160 &#160 &#160     CD20  &#160 &#160 &#160 &#160 &#160       CD68    &#160 &#160 &#160          FOXP3     &#160 &#160 &#160 &#160 panCK \
    #             &#160 &#160 &#160 &#160 &#160     Multi  &#160 &#160 &#160 &#160    CD56    &#160 &#160 &#160     CD11c     &#160 &#160 &#160 &#160 &#160     MAP1  &#160 &#160 &#160 &#160       NF2    &#160 &#160 &#160 &#160 &#160          MTAP     &#160 &#160 &#160 &#160     LAG3</p>',  unsafe_allow_html=True) 
    
    def disable_other_checkboxes(*other_checkboxes_keys):
        # if current one is trun to false, reset it to true
        if st.session_state[other_checkboxes_keys[-1]] == False:
            st.session_state[other_checkboxes_keys[-1]] = True
            
        for checkbox_key in other_checkboxes_keys[:-1]:
            st.session_state[checkbox_key] = False



    # clab = st.columns([1,7,7])
    
    # clab[1].markdown( '<p style="font-size: 14px;  font-weight: bold"> Panel-Marker </p>',  unsafe_allow_html=True) 
    # clab[2].markdown(' <p style="font-size: 14px;  font-weight: bold"> Panel-Protein </p>',  unsafe_allow_html=True)


    # cimg = st.columns(15)
    # clicked_ct = {}
    # option = ""
    # for i in range(15):
    #     with cimg[i]:
    #         clicked_ct[i] = clickable_images(
    #                         ls_images[i:i+1], 
    #                         div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    #                         img_style={"margin": "2px", "height": "70px"},
    #                         key = i,
    #         )
            
    #         st.markdown( f"<p style='font-size: 14px;  font-weight: normal; text-align: center'>{vargs[i]}</p>",  unsafe_allow_html=True) 

    # if clicked == -1: clicked = 0

    images = load_coreImages(showedImage_names[clicked],showedCore_ids[clicked],showedCore_ids2[clicked] )
    ls_images = list(images.values())
    st.markdown( '<p style="font-size: 14px;  font-weight: bold; text-align: center">     Panel-Marker   &#160 &#160 &#160  &#160 &#160 &#160 &#160   &#160 &#160 &#160 &#160 &#160   &#160 &#160 &#160 &#160 &#160  &#160 &#160 &#160 &#160 &#160  &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160  &#160 &#160 &#160  &#160   &#160 &#160 &#160 &#160   &#160 &#160 &#160 &#160   &#160 &#160 &#160 &#160  \
                &#160 &#160 &#160 &#160 &#160  &#160 &#160  Panel-Protein &#160  &#160   &#160 &#160 &#160 &#160  &#160 &#160 &#160 &#160 &#160 &#160 &#160  &#160 &#160 &#160 &#160 &#160  &#160 &#160 &#160 &#160  &#160 &#160 &#160 &#160 &#160 &#160 &#160 &#160  &#160 &#160 &#160 &#160  &#160  &#160 &#160 &#160 &#160   &#160 &#160 &#160 &#160 &#160 </p>',  unsafe_allow_html=True) 
   
    clicked_chanel = clickable_images(
                        ls_images, 
                        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                        img_style={"margin": "2px", "height": "70px"},
                        key = "chanels",
                    )
    st.markdown( '<p style="font-size: 14px;  font-weight: bold; text-align: center">      H&E      &#160 &#160 &#160 &#160 &#160     Multi  &#160 &#160 &#160 &#160 &#160   CD4    &#160 &#160 &#160 &#160 &#160     CD8     &#160 &#160 &#160 &#160 &#160     CD20  &#160 &#160 &#160 &#160 &#160        CD68    &#160 &#160 &#160  &#160           FOXP3     &#160 &#160 &#160 &#160   panCK \
                &#160 &#160 &#160 &#160 &#160     Multi  &#160 &#160 &#160 &#160    CD56    &#160 &#160 &#160 &#160    CD11c     &#160 &#160 &#160 &#160     BAP1  &#160 &#160 &#160 &#160  &#160       NF2    &#160 &#160 &#160 &#160 &#160         MTAP     &#160 &#160 &#160 &#160   LAG3</p>',  unsafe_allow_html=True) 
   
    st.divider()

    if clicked_chanel == -1:
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        info = '<p style="font-size: 16px; font-weight: bold;text-align: center">Please choose an image type to view</p>'  #sans-serif   Soin Sans Pro
        st.markdown(info, True)
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        
    else:
        c1, c2,_,c3 = st.columns([1.2, 7,0.5,2.5])

    # if clicked_chanel == -1:
    #     clicked_chanel = 0

        option = vargs[clicked_chanel]
        with c1:
            
            if clicked_chanel != -1:
                st.markdown("##")
                st.markdown("##")
                panel = ""
                if clicked_chanel >0 and clicked_chanel <= 7:
                    panel = "Panel-Marker"
                if clicked_chanel >7:
                    panel = "Panel-Protein"

                                
                st.markdown( f'<p style="font-family:sans-serif; color:#002e8c; font-size: 22px;  font-weight: bold; text-aligh: left">{option}</p>',  unsafe_allow_html=True) 
                if panel != "" :
                    st.markdown( f'<p style="font-family:sans-serif;  font-size: 14px;  font-weight: bold; text-aligh: left">({panel})</p>',  unsafe_allow_html=True) 

            
            # vargs0 = ["H&E"]
            # vargs1 = ["Composite", "CD4", "CD8", "CD20", "CD68", "FOXP3", "panCK"]
            # vargs2 = ["Composite ", "CD56", "CD11c", "BAP1","NF2", "MTAP","LAG3"] 
            # vargs = vargs0 +  vargs1 + vargs2   
            
            # option2dir = {"H&E": f"{PATH_IMG_HE}",
            #             "Composite": f"{PATH_IMG_TMA}/panel1/multi",
            #             "CD4": f"{PATH_IMG_TMA}/panel1/CD4",
            #             "CD8": f"{PATH_IMG_TMA}/panel1/CD8",
            #             "CD20": f"{PATH_IMG_TMA}/panel1/CD20",
            #             "CD68": f"{PATH_IMG_TMA}/panel1/CD68",
            #             "FOXP3": f"{PATH_IMG_TMA}/panel1/FOXP3",
            #             "panCK": f"{PATH_IMG_TMA}/panel1/panCK",
            #             "Composite ": f"{PATH_IMG_TMA}/panel2/multi2",
            #             "CD56": f"{PATH_IMG_TMA}/panel2/CD56",
            #             "CD11c": f"{PATH_IMG_TMA}/panel2/CD11c",
            #             "BAP1": f"{PATH_IMG_TMA}/panel2/BAP1",
            #             "NF2": f"{PATH_IMG_TMA}/panel2/NF2",
            #             "MTAP": f"{PATH_IMG_TMA}/panel2/MTAP",
            #             "LAG3": f"{PATH_IMG_TMA}/panel2/LAG3"
            # }


            # options = dict()
            # for key in vargs0:
            #     options[key] = st.checkbox(
            #     key,
            #     value=True,
            #     key=key,
            #     on_change=disable_other_checkboxes,
            #     args=( list(set(vargs) - set([key])) +[key] ),
            # )
            # # st.markdown("###### Panel-marker")
            # for key in vargs1:
            #     options[key] = st.checkbox(
            #     key,
            #     key=key,
            #     on_change=disable_other_checkboxes,
            #     args=( list(set(vargs) - set([key])) +[key] ),
            # )
            # # st.markdown("###### Panel-protein")
            # for key in vargs2:
            #     options[key] = st.checkbox(
            #     key,
            #     key=key,
            #     on_change=disable_other_checkboxes,
            #     args=( list(set(vargs) - set([key])) +[key] ),
            # )

            
            # # rd = st.radio("", ("H&E","", "Composite", "Composite ", "CD4", "CD8", "CD56", "CD68", "CD11c", "FOXP3","CD20", "BAP1","NF2", "MTAP","LAG3" ))

        with c2:

            if clicked_chanel == -1 :
                st.markdown("#")
                st.markdown("#")
                st.markdown("#")
                st.markdown("#")
                
                info = '<p style="font-size: 16px; font-weight: bold;text-align: center">Please choose an image type to view.</p>'  #sans-serif   Soin Sans Pro
                st.markdown(info, unsafe_allow_html=True)
                st.markdown("#")
                st.markdown("#")
                st.markdown("#")
                st.markdown("#")
            else:

                option  = vargs[clicked_chanel]               
                
                # option = get_current_checkedBox(options)

                dir = option2dir[option]
            
                if option == "H&E":
                    filename = f"{showedImage_names[clicked]}.jpg"
                elif option in vargs1 :   
                    filename = f"{showedCore_ids[clicked]}_composite_image.tif"
                else:
                    filename = f"{showedCore_ids2[clicked]}_composite_image.tif"
                    
                # st.write(showedImage_names[clicked])
                # st.write(showedCore_ids[clicked])
                # st.write(showedCore_ids2[clicked])
                if os.path.exists(f"{dir}/{filename}"):
                    imgfile =  Image.open(f"{dir}/{filename}")
                    show_plotly_image(imgfile, 750)
                else:
                    st.markdown("#")
                    info = '<p style="font-size: 16px; font-weight: bold;text-align: center">Image datas is not available for this core.</p>'  #sans-serif   Soin Sans Pro
                    st.markdown(info, unsafe_allow_html=True)


            
                # st.image(imgfile)

        with c3:
            if clicked_chanel != -1 : 
                st.markdown("##")
                st.markdown("##")
                st.markdown( '<p style="font-family:sans-serif; color:#002e8c; font-size: 22px;  font-weight: bold">Core feature</p>',  unsafe_allow_html=True) 
                st.write("")
                st.write("")    
                if clicked == -1: clicked = 0

                core_id = showedCore_ids[clicked]
                fetu1, fetu2, fetu_plus = get_core_feature(c1_IDs, c2_IDs, core_id)
                for i in range(5):
                    st.markdown(f"**{c1_names[i]}** : {fetu1[i]}", True)
                for i in range(5):
                    st.markdown(f"**{c2_names[i]}** : {fetu2[i]}", True)
                    # st.markdown(f"**:black[{c2_names[i]}]** : {fetu2[i]}", True) 
                for item in fetu_plus.keys():
                    st.markdown(f"**{item}** : {fetu_plus[item]}", True)   

                percent, count1, count2 = get_coreStatistic(core_id, option)
                if option in vargs1:
                    count = count1
                else:
                    count = count2
                st.markdown(f"**Number of cells** : {count}", True) 
                st.markdown(f"**{option} percentage** : {percent}", True)  


    