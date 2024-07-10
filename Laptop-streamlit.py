import streamlit as st 
import pandas as pd
import numpy as np 
import pickle 

with open('laptops-csv.pkl',"rb")as f:
 model=pickle.load(f)

Brand=st.number_input("Enter Brand",min_value=0,max_value=8)
Processor=st.selectbox("Enter Processor:",["Core i5",
                                        "Core i3",
                                "Ryzen 5 Hexa Core",
                                "Core i7", 
                                "Ryzen 7 Octa Core",
                                "Other",
                                "Celeron Dual Core",
                                "Ryzen 3 Quad Core" ])

Operating_system=st.selectbox("Enter Operating_system:",[ 'Windows 11 Home',
        'Mac OS Big Sur', 
         'DOS', 
        'Mac OS Monterey',
        'Chrome',
        'Windows 10', 
        'Windows 10 Home',
        'Prime OS',
       'Windows 11 Pro', 
       'Ubuntu', 
       'Windows 10 Pro', 
       'macOS Ventura',
       'macOS Sonoma', 
       'Mac OS Mojave'    ])

Touch_Screen=st.selectbox("Enter Touch_Screen",['Yes','No'])

RAM= st.number_input("Enter RAM")
Storage=st.number_input("Enter Storage")
Screen_Size = st.number_input("Enter Screen_Size")

Processor_dic={'Core i5':2,
            "Core i3":3,
            "Ryzen 5 Hexa Core":5,                    
            "Core i7":1, 
            "Ryzen 7 Octa Core":4,
            "Other":8,
            "Celeron Dual Core":7,
           "Ryzen 3 Quad Core":6 }

Operating_system_dic={"Windows 11 Home":1,
"Windows 10 Home ":3,    
"Chrome ":6,            
"Windows 10": 7,      
"DOS":10,           
"Mac OS Monterey":5,                                                                                                 
"Windows 11 Pro": 2,
"Mac OS Big Sur ": 5 , 
"Windows 10 Pro ":4, 
"Prime OS ": 8,          
"Ubuntu":9,            
"macOS Ventura": 5, 
"macOS Sonoma ":5,       
"Mac OS Mojave ":5}

Touch_screen_dic={'Yes':1,'No':0}

if st.button("Calculate Laptop Price"):
    st.header(model.predict([[Brand,Processor_dic[Processor],Operating_system_dic[Operating_system],
                              Touch_Screen_dic[Touch_Screen],RAM,Storage,Screen_Size]]))