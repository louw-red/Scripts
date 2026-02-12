# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:03:39 2023

@author: Louw Redelinghuys
"""

import os
import xlwings as xw

def refresh_workbooks_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):  # Make sure it's an Excel file
            file_path = os.path.join(folder_path, filename)
            try:
                app = xw.App(visible=False)  # Open Excel in the background (hidden)
                workbook = xw.Book(file_path)
                workbook.app.api.Calculate()  # Calculate all formulas
                workbook.save()
                workbook.close()
                app.quit()  # Close the Excel application
                print(f"{filename} refreshed successfully.")
            except Exception as e:
                print(f"Error refreshing {filename}: {str(e)}")

# Replace 'folder_path' with the path to your folder containing the workbooks.
folder_path = r'\\omrprtp01\ra\Deliveries\Valn\2023\2023-06\Reporting\Valuation\Analysis\Additional disclosure template\Input\Print Preview Disclosures'
refresh_workbooks_in_folder(folder_path)
