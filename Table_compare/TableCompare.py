# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 14:49:04 2022

@author: Louw Redelinghuys
"""
import os
from datetime import datetime


#inputs
folderpath1 = "TABLES1\\"
folderpath2 = "TABLES2\\"

#Dont Touch
cwd = os.getcwd()
outlog = cwd + "\\Table Compare Output logs"

try: 
    os.mkdir(outlog) 
except OSError: 
    pass

now = datetime.now()
current_time = now.strftime("%H-%M-%S")

def FileDiffCheck(file1,file2,filez):
    # Open File in Read Mode
    file_1 = open(file1, 'r')
    file_2 = open(file2, 'r')
    
    with open(outlog + '\\' + str(current_time)+'.txt','a') as f:
        f.write('\n')
        f.write("Comparing files: \n" + " @ " + file1 +"\n" + " # " + file2)
 
        file_1_line = file_1.readline()
        file_2_line = file_2.readline()
 
        # Use as a COunter
        line_no = 1
        
 
        f.write('\n')
        f.write("Differences in:" + filez)
        f.write('\n')
        while file_1_line != '' or file_2_line != '':
 
            # Removing whitespaces
            file_1_line = file_1_line.rstrip()
            file_2_line = file_2_line.rstrip()
 
            # Compare the lines from both file
            if file_1_line != file_2_line:
       
                # otherwise output the line on file1 and use @ sign
                if file_1_line == '':
                    f.write("@" + "Line-%d" % line_no + file_1_line)
                    f.write('\n')
                else:
                    f.write("@-" + "Line-%d" % line_no + file_1_line)
                    f.write('\n')             
                # otherwise output the line on file2 and use # sign
                if file_2_line == '':
                    f.write("#" + "Line-%d" % line_no + file_2_line)
                    f.write('\n')
                else:
                    f.write("#+" + "Line-%d" % line_no + file_2_line)
                    f.write('\n')                    
                                                            
            # Read the next line from the file
            file_1_line = file_1.readline()
            file_2_line = file_2.readline()
 
            line_no += 1
 
        file_1.close()
        file_2.close()    
        f.close()

for subdir, dirs, files in os.walk(folderpath1):
    for diri in dirs:
        print(diri)
        for subdir1,dirs1,files1 in os.walk(folderpath1 + diri):
            for file in files1:
                try:
                    FileDiffCheck(folderpath1 + diri + '\\' + file,folderpath2 + diri + '\\' + file,file)
                except:
                    with open(outlog + '\\' + str(current_time)+'.txt','a') as f:
                        f.write('\n')
                        f.write("Cannot find equivalent file for: " + file)

