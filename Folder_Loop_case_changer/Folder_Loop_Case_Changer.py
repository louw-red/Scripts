# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:48:17 2023

@author: Louw Redelinghuys

Purpose of this tool is to standardise table name structure. 

The options are:
    
1. Extension lower case
2. Extension upper case
3. Full name lower case (includes ext)
4. Full name upper case (includes ext)
5. First Letter Upper case, res lower case (includes ext)
6. First Letter Upper case, res lower case (excludes ext)
"""

############################################### INPUTS #####################################################


directory_path = r"C:\Users\X470118\OneDrive - Old Mutual\Desktop\GIT Repo\MP_2021"
case_option = 5 # Change this to the desired case_option


############################################## IMPORTS #####################################################


import os 

#############################################  FUNCTIONS ###################################################

def rename_files(directory, case_option):
    for dirpath,_,filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
           
            if os.path.isfile(filepath):
                # Split the filename into base and extension
                base, ext = os.path.splitext(filename)
        
                # Perform renaming based on case_option
                if case_option == 1:
                    new_ext = ext.lower()
                elif case_option == 2:
                    new_ext = ext.upper()
                elif case_option == 3:
                    new_base = base.lower()
                    new_ext = ext.lower()
                elif case_option == 4:
                    new_base = base.upper()
                    new_ext = ext.upper()
                elif case_option == 5:
                    new_base = base.capitalize()
                    new_ext = ext.capitalize()
                    new_ext = ext[0] + ext[1:].capitalize()
                elif case_option == 6:
                    new_base = base.capitalize()
                    new_ext = ext.lower()

                # Construct the new filename
                if case_option in [1, 2]:
                    new_filename = f"{base}{new_ext}"
                else:
                    new_filename = f"{new_base}{new_ext}"
        
        
                new_filepath = os.path.join(dirpath,new_filename)
                
                try:
                    os.rename(filepath, new_filepath) 
                except:
                    if filepath != new_filepath and os.path.exists(new_filepath):
                      print(f"Skipping {filename},file with new name already exists.")

                
               
        
                # Rename the file
               # os.rename(filepath, os.path.join(directory, new_filename))


############################################# EXECUTION ####################################################


rename_files(directory_path, case_option)


