# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:00:04 2022

@author: Louw Redelinghuys

TIP: Run on a folder with ONLY the RPTs you want to extract.                                        
                                               
                                               
"""

import csv
import re
import os
import pandas as pd

########################################################################################################################
#                                                   INPUTS
########################################################################################################################

Run_type = "OPN" #Used to label folder. Only affects the next 3 lines

Folder_To_Check = "input folder"+"\\"+ Run_type + "\\"

Folder_output = "output folder" +"\\"+ Run_type

Folder_summary_output = "output folder" + Run_type

description = "_LFRC_BEL_&_COMPONENTS_AND_RA_REP" #Optional to label the output data file. Can leave as "" otherwise.

Extracted_fields = ['LFRC_BEL'
                      , 'LFRC_BEL_COMPONENTS_I17(1)'
                      , 'LFRC_BEL_COMPONENTS_I17(10)'
                      , 'LFRC_BEL_COMPONENTS_I17(11)'
                      , 'LFRC_BEL_COMPONENTS_I17(12)'
                      , 'LFRC_BEL_COMPONENTS_I17(13)'
                      , 'LFRC_BEL_COMPONENTS_I17(14)'
                      , 'LFRC_BEL_COMPONENTS_I17(15)'
                      , 'LFRC_BEL_COMPONENTS_I17(16)'
                      , 'LFRC_BEL_COMPONENTS_I17(17)'
                      , 'LFRC_BEL_COMPONENTS_I17(18)'
                      , 'LFRC_BEL_COMPONENTS_I17(19)'
                      , 'LFRC_BEL_COMPONENTS_I17(2)'
                      , 'LFRC_BEL_COMPONENTS_I17(20)'
                      , 'LFRC_BEL_COMPONENTS_I17(21)'
                      , 'LFRC_BEL_COMPONENTS_I17(22)'
                      , 'LFRC_BEL_COMPONENTS_I17(23)'
                      , 'LFRC_BEL_COMPONENTS_I17(24)'
                      , 'LFRC_BEL_COMPONENTS_I17(25)'
                      , 'LFRC_BEL_COMPONENTS_I17(26)'
                      , 'LFRC_BEL_COMPONENTS_I17(27)'
                      , 'LFRC_BEL_COMPONENTS_I17(28)'
                      , 'LFRC_BEL_COMPONENTS_I17(29)'
                      , 'LFRC_BEL_COMPONENTS_I17(3)'
                      , 'LFRC_BEL_COMPONENTS_I17(30)'
                      , 'LFRC_BEL_COMPONENTS_I17(31)'
                      , 'LFRC_BEL_COMPONENTS_I17(32)'
                      , 'LFRC_BEL_COMPONENTS_I17(33)'
                      , 'LFRC_BEL_COMPONENTS_I17(34)'
                      , 'LFRC_BEL_COMPONENTS_I17(4)'
                      , 'LFRC_BEL_COMPONENTS_I17(5)'
                      , 'LFRC_BEL_COMPONENTS_I17(6)'
                      , 'LFRC_BEL_COMPONENTS_I17(7)'
                      , 'LFRC_BEL_COMPONENTS_I17(8)'
                      , 'LFRC_BEL_COMPONENTS_I17(9)'
                      , 'IFRS17_GROUP_PROFIT'
                      , 'LFRC_RA']

########################################################################################################################
#                                    ### Field Extract Templates ####
########################################################################################################################
# These are not used and are provided as templates for extracts

Extract_fields_BEL = ['LFRC_BEL'
                      , 'LFRC_BEL_COMPONENTS_I17(1)'
                      , 'LFRC_BEL_COMPONENTS_I17(10)'
                      , 'LFRC_BEL_COMPONENTS_I17(11)'
                      , 'LFRC_BEL_COMPONENTS_I17(12)'
                      , 'LFRC_BEL_COMPONENTS_I17(13)'
                      , 'LFRC_BEL_COMPONENTS_I17(14)'
                      , 'LFRC_BEL_COMPONENTS_I17(15)'
                      , 'LFRC_BEL_COMPONENTS_I17(16)'
                      , 'LFRC_BEL_COMPONENTS_I17(17)'
                      , 'LFRC_BEL_COMPONENTS_I17(18)'
                      , 'LFRC_BEL_COMPONENTS_I17(19)'
                      , 'LFRC_BEL_COMPONENTS_I17(2)'
                      , 'LFRC_BEL_COMPONENTS_I17(20)'
                      , 'LFRC_BEL_COMPONENTS_I17(21)'
                      , 'LFRC_BEL_COMPONENTS_I17(22)'
                      , 'LFRC_BEL_COMPONENTS_I17(23)'
                      , 'LFRC_BEL_COMPONENTS_I17(24)'
                      , 'LFRC_BEL_COMPONENTS_I17(25)'
                      , 'LFRC_BEL_COMPONENTS_I17(26)'
                      , 'LFRC_BEL_COMPONENTS_I17(27)'
                      , 'LFRC_BEL_COMPONENTS_I17(28)'
                      , 'LFRC_BEL_COMPONENTS_I17(29)'
                      , 'LFRC_BEL_COMPONENTS_I17(3)'
                      , 'LFRC_BEL_COMPONENTS_I17(30)'
                      , 'LFRC_BEL_COMPONENTS_I17(31)'
                      , 'LFRC_BEL_COMPONENTS_I17(32)'
                      , 'LFRC_BEL_COMPONENTS_I17(33)'
                      , 'LFRC_BEL_COMPONENTS_I17(34)'
                      , 'LFRC_BEL_COMPONENTS_I17(4)'
                      , 'LFRC_BEL_COMPONENTS_I17(5)'
                      , 'LFRC_BEL_COMPONENTS_I17(6)'
                      , 'LFRC_BEL_COMPONENTS_I17(7)'
                      , 'LFRC_BEL_COMPONENTS_I17(8)'
                      , 'LFRC_BEL_COMPONENTS_I17(9)']


Extract_fields_RA = ['LFRC_RA'
                      , 'LFRC_RA_COMPONENTS_I17(1)'
                      , 'LFRC_RA_COMPONENTS_I17(10)'
                      , 'LFRC_RA_COMPONENTS_I17(11)'
                      , 'LFRC_RA_COMPONENTS_I17(12)'
                      , 'LFRC_RA_COMPONENTS_I17(13)'
                      , 'LFRC_RA_COMPONENTS_I17(14)'
                      , 'LFRC_RA_COMPONENTS_I17(15)'
                      , 'LFRC_RA_COMPONENTS_I17(16)'
                      , 'LFRC_RA_COMPONENTS_I17(17)'
                      , 'LFRC_RA_COMPONENTS_I17(18)'
                      , 'LFRC_RA_COMPONENTS_I17(19)'
                      , 'LFRC_RA_COMPONENTS_I17(2)'
                      , 'LFRC_RA_COMPONENTS_I17(20)'
                      , 'LFRC_RA_COMPONENTS_I17(21)'
                      , 'LFRC_RA_COMPONENTS_I17(22)'
                      , 'LFRC_RA_COMPONENTS_I17(23)'
                      , 'LFRC_RA_COMPONENTS_I17(24)'
                      , 'LFRC_RA_COMPONENTS_I17(25)'
                      , 'LFRC_RA_COMPONENTS_I17(26)'
                      , 'LFRC_RA_COMPONENTS_I17(27)'
                      , 'LFRC_RA_COMPONENTS_I17(28)'
                      , 'LFRC_RA_COMPONENTS_I17(29)'
                      , 'LFRC_RA_COMPONENTS_I17(3)'
                      , 'LFRC_RA_COMPONENTS_I17(30)'
                      , 'LFRC_RA_COMPONENTS_I17(31)'
                      , 'LFRC_RA_COMPONENTS_I17(32)'
                      , 'LFRC_RA_COMPONENTS_I17(33)'
                      , 'LFRC_RA_COMPONENTS_I17(34)'
                      , 'LFRC_RA_COMPONENTS_I17(4)'
                      , 'LFRC_RA_COMPONENTS_I17(5)'
                      , 'LFRC_RA_COMPONENTS_I17(6)'
                      , 'LFRC_RA_COMPONENTS_I17(7)'
                      , 'LFRC_RA_COMPONENTS_I17(8)'
                      , 'LFRC_RA_COMPONENTS_I17(9)']

########################################################################################################################
#                                                     Constants
########################################################################################################################
sep = ','
Headerstrings = ''

########################################################################################################################
#                                                     Functions
########################################################################################################################


#Creates a dictionary of the positions of the columns being extracted
def headerfinder(headers,arg_extract_columns):
    my_header_dict = dict()
    for arg in arg_extract_columns:
        my_header_dict[headers.index(arg)] = arg 
    return my_header_dict

#Writes a file. Takes the output file name, the info to write and whether or not the line being passed is a header
def fileWrite(output_file_name,info,header = 1):        
    with open(output_file_name,'a') as f:
        if header == 1:
            f.write("\n")
        if type(info) == list:      
            for i in info:
                f.write(i)
                f.write(',')
        else:
            f.write(info)
            
#Extracts info to be written: Takes extract fields, row and a header string (to pass into the headerfinder function)
def DataExtract(row,extract_fields,Headline):
    HeaderDict = headerfinder(Headline,extract_fields)
    output = []
    for e in extract_fields:        
        output.append(row[list(HeaderDict.keys())[list(HeaderDict.values()).index(e)]])
        outputSTR = sep.join(map(str, output))
    return str(outputSTR)
    
        
# Function doing the heavy lifting of opening the source file location and writing it to a new location
def file_IO(input_file_name,output_file_name,extract_fields):
    try:
        os.remove(output_file_name)
    except:
        pass
    
    if input_file_name.endswith(".rpt") and not input_file_name.endswith(".12.rpt"):
        with open(input_file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            header_line = 999
            line_count = 0
            for row in csv_reader:
                if '&' in row:
                    line_count += 1
                if '!' in row:               
                    header_line=line_count
                    Headerstrings = row
                    fileWrite(output_file_name, extract_fields,header = 0)
                    line_count += 1
                else:   
                    if line_count > header_line:
                        if '&' not in row:
                            line_count += 1
                            DataExtractInRow = DataExtract(row, extract_fields,Headerstrings)
                            fileWrite(output_file_name,DataExtractInRow,header = 1)
                    else:                
                        line_count += 1
            print(f'Processed {line_count} lines.')

#Runs the FileIO for every file in the directory. Creates output directory
def FolderIO(folder_input_path,folder_output_path,extract_fields,dir_list):
       
    try: 
        os.mkdir(Folder_output) 
    except OSError: 
        pass
    for i in dir_list:
        file_IO(folder_input_path + i,folder_output_path + "\\"+i + description,extract_fields)


#Acts as a check on final created files. Sums individual output files and produces a summary
def SumCheck(folder_input_path,folder_output_path,extract_fields,dir_list):
    
    Trim_dir_list = os.listdir(folder_input_path) 

    try: 
        os.mkdir(Folder_summary_output) 
    except OSError: 
        pass
    try:
        os.remove(folder_output_path)
    except:
        pass
    
    with open(folder_output_path, 'a') as f:
        f.write('Product,')
        line = sep.join(map(str, extract_fields))
        f.write(line)
        f.write("\n")

        j = 0
        while j < len(dir_list):
            i = 0
            while i < len(Trim_dir_list):
                stringi = str(Trim_dir_list[i])
                dir_listj = str(dir_list[j])
                if stringi == dir_listj + str(description):
                    df = pd.read_csv(folder_input_path +"\\"+ dir_listj + description,delimiter = ',')
                    f.write(dir_list[j])
                    f.write(",")
                    for e in extract_fields:
                        try:    
                            df[e] = df[e].astype('float')
                            sumdf = df[e].sum()
                            f.write(str(sumdf))
                        except:
                            f.write("Cannot Sum string")
                        f.write(",")
                    f.write("\n")
                i += 1 
            j += 1
            
    

########################################################################################################################
#
#                                                   CODE EXECUTION
#
########################################################################################################################       

dir_list = os.listdir(Folder_To_Check) 

# "Folder In Out": Takes input folder and output folder and then strips out the extracted fields.
FolderIO(Folder_To_Check,Folder_output,Extracted_fields,dir_list)


########################################################################################################################
# This section is specifically for the RA replication check. 
########################################################################################################################

"""
#Added for Sumcheck
Extracted_fields.append("LAPSE_COMPONENT")
Extracted_fields.append("EXPENSE_COMPONENT")
Extracted_fields.append("MORTALITY_COMPONENT")
Extracted_fields.append("MORBIDITY_COMPONENT")
Extracted_fields.append("MORTALITY+MORBIDITY_COMPONENT")
Extracted_fields.append("Replicated_RA")
"""

def Rpt_Manipulation_function(df,product):
    
    """
    #RA Replication Calculation
    RA_table = "RiskAdjustment_Table.csv"
    df_RA = pd.read_csv(RA_table, index_col="Product")   
    
    premiums = "LFRC_BEL_COMPONENTS_I17(1)"
    lapse_grace = "LFRC_BEL_COMPONENTS_I17(2)"
    component4 = "LFRC_BEL_COMPONENTS_I17(4)"
    component6 = "LFRC_BEL_COMPONENTS_I17(6)"
    expenses = "LFRC_BEL_COMPONENTS_I17(7)"
    risk_benefits = "LFRC_BEL_COMPONENTS_I17(13)"
    component14 = "LFRC_BEL_COMPONENTS_I17(14)"

    df["LAPSE_COMPONENT"] = abs(df[premiums]+df[lapse_grace]+df[component4]+df[component6]+df[expenses]+df[risk_benefits]+df[component14])
    df["EXPENSE_COMPONENT"] = abs(df[expenses])
    df["MORTALITY_COMPONENT"] = abs(df[risk_benefits])
    df["MORBIDITY_COMPONENT"] = abs(df[risk_benefits])
    df["MORTALITY+MORBIDITY_COMPONENT"] = abs(df[risk_benefits])
   
    df["Replicated_RA"]= df["LAPSE_COMPONENT"]*float(df_RA.at[product,'Lapse driver'])+df["EXPENSE_COMPONENT"]*float(df_RA.at[product,'Expense driver'])+df["MORTALITY_COMPONENT"]*float(df_RA.at[product,'Mortality driver'])+df["MORBIDITY_COMPONENT"]*float(df_RA.at[product,'Morbidity driver'])+df["MORTALITY+MORBIDITY_COMPONENT"]*float(df_RA.at[product,'Mortality+Morbidity driver'])

    """
    
    return df

def df_quick_change(input_file_path):
    change_list = os.listdir(input_file_path)
    for i in change_list:
        extension = re.search('.rpt',i)
        product = i[0:extension.span()[0]]
        df = pd.read_csv(input_file_path + i,delimiter = ',',index_col=[0])        
        
        ###### The piece below runs the function that alters the Data   #########
        New_df = Rpt_Manipulation_function(df,product)
        New_df.to_csv(input_file_path + i)


Sum_check_input = Folder_output

df_quick_change(Folder_output + "\\")


# End of RA Replication specific code
#######################################################################################################################

#Checks the sums of all the individual files and produces a log
SumCheck(Sum_check_input,Folder_summary_output+"\\"+description+"_SUMMARY.txt",Extracted_fields,dir_list)






