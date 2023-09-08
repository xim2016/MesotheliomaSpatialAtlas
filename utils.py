import pandas as pd
import numpy as np
import streamlit as st
import os
import base64
import plotly.express as px

# @st.cache_data
# def convert_ID():
#     imgID_to_coreID = dict()
#     coreID_to_imgID = dict()
#     df = load_metadata()
#     for idx in df.index:
#         imgID, coreID = df.loc[idx, ['level2_name', 'Annotation ID']]
#         imgID_to_coreID[imgID] = coreID
#         coreID_to_imgID[coreID] = imgID
#     return(imgID_to_coreID, coreID_to_imgID)   

def get_orderedList(opt):
    list_order = { 
        "Institute": ["All", "Pitt", "RPCI", "Penn"],
        "Classification":["All", "Malignant", "Benign" , "Not Specified"],
        "CaseType":["All",  "Pleural",  "Peritoneal",  "Other"  ],
        "subtype":["All", "Epithelioid","Biphasic", "Papillary","Sarcomatoid", "Desmoplastic","Benign Fibrous","Fibrocystic" ,"Multicystic", "Not specified" ],
        "Gender":["All", "Male", "Female", "Unknown"],
        "Race":["All", "White", "Black", "Asian", "American Indian Aleutian Eskimo", "Unknown"],
        "DiagnosisAge":["All", "81-90", "71-80", "61-70", "51-60", "41-50", "31-40" ],
        "AsbestosExposure":["All","Yes", "No", "Unknown"],
        "smoking":["All","Non-smoker","Current smoker",  "Previous smoker" ,"Smoker (current or previous)",  "Unknown" ] , 
        "Grade":["All", "High","Intermediate","Low",  "Not Specified"]         
    }
    return list_order[opt]

# def get_orderedList(opt):
#     list_order = { 
#         "Institute": [ "Pitt", "RPCI", "Penn"],
#         "Classification":[ "Malignant", "Benign" , "Not Specified"],
#         "CaseType":[  "Pleural",  "Peritoneal",  "Other"  ],
#         "subtype":["Epithelioid","Biphasic", "Papillary","Sarcomatoid", "Desmoplastic","Benign Fibrous","Fibrocystic" ,"Multicystic", "Not specified" ],
#         "Gender":["Male", "Female", "Unknown"],
#         "Race":["White", "Black", "Asian", "American Indian Aleutian Eskimo", "Unknown"],
#         "DiagnosisAge":["81-90", "71-80", "61-70", "51-60", "41-50", "31-40" ],
#         "AsbestosExposure":["Yes", "No", "Unknown"],
#         "smoking":["Non-smoker","Current smoker",  "Previous smoker" ,"Smoker (current or previous)",  "Unknown" ] , 
#         "Grade":["High","Intermediate","Low",  "Not Specified"]         
#     }
#     return list_order[opt]
    
def name_coverter(opt):
    converter = {"NMVB2_MESO":"RPCI"
        
    }
    return(name_coverter[opt])

@st.cache_data
def load_metadata():
    df =  pd.read_csv("./data/mapping_nameCLeaned_wImgID.csv")
    return(df)

@st.cache_data
def load_coreFeature():
    df = pd.read_csv("./data/core_features_allMarkers_withIntensity_alCores_forWebPortal.csv", index_col=0)
    return(df)

def get_coreStatistic(coreID, marker):
    df = load_coreFeature()
    count1 = df.loc[coreID, "cell count 1"]
    count2 = df.loc[coreID, "cell count 2"] 
    if f"{marker} percent" in df.columns:
        percent = df.loc[coreID, f"{marker} percent"]
        return('{0:.2%}'.format(percent), count1, count1)
    else:
        return("N/A", count1, count2)

def load_coreImages(path_img_logo, image_names, core_ids, core_ids2):

        
    images = []
    showedImage_names = []
    showedCore_ids = []
    showedCore_ids2 = []

    for i in range(len(image_names)) :
        
        image_name = image_names[i]
        core_id = core_ids[i]
        core_id2 = core_ids2[i]

        file = f"{path_img_logo}/{image_name}.png"

        if not os.path.exists(file):
            # st.write(f"{image_name} file not exist")
            continue

        showedImage_names.append(image_name)
        showedCore_ids.append(core_id)
        showedCore_ids2.append(core_id2)
        
        with open(file, "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
            images.append(f"data:image/jpeg;base64,{encoded}")

            
    return(images, showedImage_names, showedCore_ids, showedCore_ids2)       
            
def get_imageNames(cs1, cs2, c1_IDs, c2_IDs):
    
    df = load_metadata()
    
    for i in range(5):
        if cs1[i] != "All":
            df = df.loc[df[c1_IDs[i]] == cs1[i], :]
    for i in range(5):
        if cs2[i] != "All":
            df = df.loc[df[c2_IDs[i]] == cs2[i], :]

    # will combine all core images and names as institure_coreid
    image_names = df.loc[:, "level2_name"]
    core_ids = df.loc[:, "Annotation ID"]
    core_ids2 = df.loc[:, "Annotation2"]
    #core ID use level2_name, others, use Anntoation ID

    return([image_names, core_ids, core_ids2])
    
    
    
def show_plotly_image(img_file, height=750):
 
    img = np.array(img_file.convert('RGB'))
    fig = px.imshow(img, binary_string=True)
    fig.update_xaxes(showgrid=False, showticklabels=False)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    fig.update_layout(height=height,
                      newshape_line_color='cyan',
                      dragmode='drawopenpath')
    config = {'displayModeBar': True,
              'displaylogo': False,
              'toImageButtonOptions': { 'height': None, 'width': None, 
                                       'filename': 'core_img',},
               'modeBarButtonsToRemove': ['zoom', 'resetScale'],
               'modeBarButtonsToAdd': ['drawline',
                                        'drawopenpath',
                                        'drawclosedpath',
                                        'drawcircle',
                                        'drawrect',
                                        'eraseshape'
                                       ]}
    st.plotly_chart(fig, use_container_width=True, height=height, config=config)
    
    
def get_core_feature(c1_IDs, c2_IDs, core_id):
   
    df = load_metadata()
    
    fetu1 = dict()
    for i in range(5):
        fetu1[i] = df.loc[df['Annotation ID'] == core_id, c1_IDs[i]].values[0]
    fetu2 = dict()
    for i in range(5):
        fetu2[i] = df.loc[df['Annotation ID'] == core_id, c2_IDs[i]].values[0]
    
    fetu_plus = dict()
    fetu_plus["Survival period"] =  df.loc[df['Annotation ID'] == core_id, "SurvivalPeriod"].values[0] + " months"
        
    return(fetu1, fetu2, fetu_plus)

def customize_sidebar(color = "#000000"):
    st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #F5F5F5;
        color: {color};
        font-size: 15px;
    }
    </style>
    """, unsafe_allow_html=True)
    
def generat_logo_images():
    from PIL import Image
    import os
    import pandas as pd
    df = pd.read_csv("./data/mapping_nameCLeaned_wImgID.csv")
    image_list = df['level2_name'].dropna()
    
    path_img_big_all = "./data/core_image/H&E_level2_all"
    path_img_big = "./data/core_image/H&E_level2"
    path_img_logo =  "./data/core_image/H&E_logo"

    notFound = []
    for file in image_list:
        pathfile = f"{path_img_big_all}/{file}.png"
        if not os.path.isfile(pathfile):
            notFound.append(file)
            continue
        im = Image.open(pathfile)
        im.save(f"{path_img_big}/{file}.png")
        
        im = im.resize((100,100), Image.LANCZOS)
        im.save(f"{path_img_logo}/{file}.png")
    print(notFound)


def get_screen_width_height():
    #Import the required libraries

    import tkinter 
    #Create an instance of tkinter frame
    win= tkinter.Tk()

    #Set the geometry of frame
    win.geometry("650x250")

    #Get the current screen width and height
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    #Print the screen size
    print("Screen width:", screen_width)
    print("Screen height:", screen_height)