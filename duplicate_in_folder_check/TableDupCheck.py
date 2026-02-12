# -*- coding: utf-8 -*-

'''
@author: Louw Redelinghuys


'''
import os
from datetime import datetime

#Dont Touch
cwd = os.getcwd()


cwd_tbls = cwd + '\\TABLES\\'
Input_Tables = os.listdir(cwd_tbls)
sep = ','

#Create a list of tables that needs to be cleaned              
Table_list = []
Table_names = []
for Tabl in Input_Tables:
    try:
        tdir = cwd_tbls + Tabl + '\\'
        trp = os.listdir(cwd_tbls + Tabl + '\\')
        for t in trp:
            Table_list.append([t,Tabl,tdir+t])
            Table_names.append(t)
    except:
        pass


dup_list = []
dup_count = 0
dup_dir = []
#Check for duplicates
for elem in Table_names:
    if Table_names.count(elem) > 1:
        print('Tables contain more than 1 version of ' + str(elem) +".")
        print('Please correct and rerun')
        dup_list.append(elem)
        dup_count +=1
        
for elem in dup_list:
    for Tbl in Table_list:
        if str(elem) == str(Tbl[0]):
            dup_dir.append((elem,Tbl[2]))
            
    
try: 
    os.mkdir(cwd + "\\output_logs") 
except OSError: 
    pass

now = datetime.now()
current_time = now.strftime("%H-%M-%S")

with open(cwd + "\\output_logs\\" +str(current_time) +".txt",'w') as f:
    f.write('runlog::')
    f.write("\n")
    if dup_count>1:
        f.write("WARNING: Number of duplicates in tables: " +str(dup_count))
        f.write('\n')
        f.write('There are duplicates of the following files. Please correct to ensure errors are avoided:')
        i = 0
        while i < len(dup_dir):
            f.write('\n')
            f.write(dup_dir[i][0] +' , ' + dup_dir[i][1])
            i+=1
            
    else:
        f.write('No duplicate files in Tables')
    f.close()
        
