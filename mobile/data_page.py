import os
import streamlit as st
from st_clickable_images import clickable_images
from PIL import Image
from mobile.utils import get_orderedList, get_imageNames, load_HEImages, load_coreImages, show_plotly_image, get_core_feature, get_coreStatistic
from mobile.style import define_layout



def disable_other_checkboxes(*other_checkboxes_keys):
    # if current one is trun to false, reset it to true
    if st.session_state[other_checkboxes_keys[-1]] == False:
        st.session_state[other_checkboxes_keys[-1]] = True
        
    for checkbox_key in other_checkboxes_keys[:-1]:
        st.session_state[checkbox_key] = False
        
def get_current_checkedBox(options):
    key = list(options.keys())[list(options.values()).index(True)]
    return (key)      
        
def data_page():
    
    
    max_width = '80%'
    padding_top = '2rem'
    padding_right = '0rem'
    padding_left = '0rem'
    padding_bottom = '0rem'
    define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
    
    st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: white;
        }
    #     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
    #     width: 300px;
    # }
    # [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
    #     width: 300px;
    #     margin-left: -100px;
    # }
    </style>
    """, unsafe_allow_html=True)

    PATH_IMG_TMA = "./data/core_image"
    
    PATH_IMG_HE = "./data/core_image/H&E_level1"  
    path_img_logo = "./data/core_image/H&E_logo" 

    c1_IDs = ["Institute", "Classification","CaseType","subtype", "Grade"]
    c1_names = ["Institute", "Classification","Case type","Subtype", "Tumor grade"]
    # c1 = st.columns([3,3,3,3,3])
    cs1 = dict()
    for i in range(5):
        cs1[i] = st.selectbox(
                    c1_names[i],
                    get_orderedList(c1_IDs[i]),
                    key = c1_IDs[i]
                )
    

    c2_IDs = ["Gender", "DiagnosisAge","AsbestosExposure","Race", "smoking"]
    c2_names = ["Gender", "Diagnosis age","Asbestos exposure","Race", "Smoking"]
    # c2 = st.columns([3,3,3,3,3])
    cs2 = dict()
    for i in range(5):
        cs2[i] = st.selectbox(
                    c2_names[i],
                    get_orderedList(c2_IDs[i]),
                    key = c2_IDs[i]
                )
        
   
    
    #H&E use image_names , others use core_ids as image names
    image_names, core_ids, core_ids2 = get_imageNames(cs1, cs2, c1_IDs,c2_IDs)
    
    images, showedImage_names, showedCore_ids, showedCore_ids2 = load_HEImages(path_img_logo , list(image_names), list(core_ids), list(core_ids2))

    if len(images) == 0 :
        st.write("No core for current selection.")

    else:
        st.markdown("#### Please select a core.", True)

        clicked = clickable_images(
            images, 
            div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
            img_style={"margin": "5px", "height": "40px"},
        )

        if clicked != -1: 
            
            
            coreinfo = f'<p style="color:#5f6060; background-color:#e9f2fc; font-size: 12px; font-weight: bold;text-align: center;  padding-top: 6px; padding-bottom: 6px;border-radius: 10px; ">Core {showedImage_names[clicked]} is selected</p>'  #sans-serif   Soin Sans Pro
            st.markdown( coreinfo,  unsafe_allow_html=True) 
            
            st.markdown( '<p style="font-family:sans-serif; color:#002e8c; font-size: 22px;  font-weight: bold">Core feature</p>',  unsafe_allow_html=True) 
            core_id = showedCore_ids[clicked]
            fetu1, fetu2, fetu_plus = get_core_feature(c1_IDs, c2_IDs, core_id)
            for i in range(5):
                st.markdown(f"**{c1_names[i]}** : {fetu1[i]}", True)
            for i in range(5):
                st.markdown(f"**{c2_names[i]}** : {fetu2[i]}", True)
                # st.markdown(f"**:black[{c2_names[i]}]** : {fetu2[i]}", True) 
            for item in fetu_plus.keys():
                st.markdown(f"**{item}** : {fetu_plus[item]}", True)   

            # percent, count1, count2 = get_coreStatistic(core_id, option)
            # if option in vargs1:
            #     count = count1
            # else:
            #     count = count2
            # st.markdown(f"**Number of cells** : {count}", True) 
            # st.markdown(f"**{option} percentage** : {percent}", True)
            # 
            #          
            
            vargs0 = ["H&E"]
            vargs1 = ["(Panel-Marker) mIF", "(Panel-Marker) CD4", "(Panel-Marker) CD8", "(Panel-Marker) CD20", "(Panel-Marker) CD68", "(Panel-Marker) FOXP3", "(Panel-Marker) panCK"]
            vargs2 = ["(Panel-Protein) mIF ", "(Panel-Protein) CD56", "(Panel-Protein) CD11c", "(Panel-Protein) BAP1","(Panel-Protein) NF2", "(Panel-Protein) MTAP","(Panel-Protein) LAG3"] 
            vargs = vargs0 +  vargs1 + vargs2   

            option2dir = {"H&E": f"{PATH_IMG_HE}",
                        "(Panel-Marker) mIF": f"{PATH_IMG_TMA}/panel1/multi",
                        "(Panel-Marker) CD4": f"{PATH_IMG_TMA}/panel1/CD4",
                        "(Panel-Marker) CD8": f"{PATH_IMG_TMA}/panel1/CD8",
                        "(Panel-Marker) CD20": f"{PATH_IMG_TMA}/panel1/CD20",
                        "(Panel-Marker) CD68": f"{PATH_IMG_TMA}/panel1/CD68",
                        "(Panel-Marker) FOXP3": f"{PATH_IMG_TMA}/panel1/FOXP3",
                        "(Panel-Marker) panCK": f"{PATH_IMG_TMA}/panel1/panCK",
                        "(Panel-Protein) mIF ": f"{PATH_IMG_TMA}/panel2/multi2",
                        "(Panel-Protein) CD56": f"{PATH_IMG_TMA}/panel2/CD56",
                        "(Panel-Protein) CD11c": f"{PATH_IMG_TMA}/panel2/CD11c",
                        "(Panel-Protein) BAP1": f"{PATH_IMG_TMA}/panel2/BAP1",
                        "(Panel-Protein) NF2": f"{PATH_IMG_TMA}/panel2/NF2",
                        "(Panel-Protein) MTAP": f"{PATH_IMG_TMA}/panel2/MTAP",
                        "(Panel-Protein) LAG3": f"{PATH_IMG_TMA}/panel2/LAG3"
            }


            
            #zoom in

            st.markdown("#### Select a channel to zoom in.", True)

            # image chanel views
            # st.markdown( '<p style="font-family:sans-serif; color:#002e8c; font-size: 22px;  font-weight: bold">All image channels</p>',  unsafe_allow_html=True) 
            chanel_images = load_coreImages(showedImage_names[clicked],showedCore_ids[clicked],showedCore_ids2[clicked] )
            ls_images = list(chanel_images.values())

            # for i in range(15):
            #     st.markdown(ls_images[i], unsafe_allow_html=True)
            #     st.write(vargs[i])

            
            options = dict()
            i = 0
            for key in vargs0:
                st.markdown(ls_images[i], unsafe_allow_html=True)
                i = i + 1
                options[key] = st.checkbox(
                label = key,
                value=True,
                key=key,
                on_change=disable_other_checkboxes,
                args=( list(set(vargs) - set([key])) +[key] ),
            )
            # st.markdown("###### Panel-marker")
            
            for key in vargs1:
                st.markdown(ls_images[i], unsafe_allow_html=True)
                i = i + 1
                options[key] = st.checkbox(
                key,
                key=key,
                on_change=disable_other_checkboxes,
                args=( list(set(vargs) - set([key])) +[key] ),
            )
            # st.markdown("###### Panel-protein")
           
            for key in vargs2:
                st.markdown(ls_images[i], unsafe_allow_html=True)
                i = i + 1
                options[key] = st.checkbox(
                key,
                key=key,
                on_change=disable_other_checkboxes,
                args=( list(set(vargs) - set([key])) +[key] ),
            )

            # captions = [ " ", "Marker", "Marker", "Marker", "Marker",  "Marker", "Marker", "Marker", "Protein", "Protein", "Protein", "Protein", "Protein", "Protein", "Protein"]
            # option = st.radio("Select image type", key="visibility", options=vargs,  horizontal=True)
                
                # rd = st.radio("", ("H&E","", "mIF", "mIF ", "CD4", "CD8", "CD56", "CD68", "CD11c", "FOXP3","CD20", "BAP1","NF2", "MTAP","LAG3" ))
            
           

            option = get_current_checkedBox(options)

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
                show_plotly_image(imgfile, 400)
            else:
                # st.markdown("#")
                info = '<p style="font-size: 16px; font-weight: bold;text-align: center">Image datas is not available for this core.</p>'  #sans-serif   Soin Sans Pro
                st.markdown(info, unsafe_allow_html=True)

            if option != "H&E":
                # st.divider()
                st.markdown("**DAPI in :blue[blue color]**")

            

        
