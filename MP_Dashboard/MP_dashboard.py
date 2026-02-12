# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 12:14:41 2025

@author: Louw Redelinghuys
"""

import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def clean_and_read_file(filepath):
    """
    Cleans the file by:
    - Finding header (first line with "!" in first column)
    - Keeping only rows starting with "*"
    - Skipping footer content (non-decodable or invalid)
    """
    lines = []
    with open(filepath, 'rb') as file:
        for raw_line in file:
            try:
                line = raw_line.decode('utf-8').strip()
                if line.startswith("!") or line.startswith("*"):
                    lines.append(line)
            except UnicodeDecodeError:
                # Skip problematic footer lines
                continue

    # Find header
    header_line = None
    for i, line in enumerate(lines):
        if line.startswith("!"):
            header_line = i
            break

    if header_line is None:
        raise ValueError(f"No header found in {filepath}")
    
    header = lines[header_line].lstrip("!").split(",")
    data = [line.lstrip("*").split(",") for line in lines[header_line+1:] if line.startswith("*")]
    
    df = pd.DataFrame(data, columns=header)
    return df

def summarize_multiple_columns(folder_path, columns_to_summarize, file_extension, output_path):
    workbook = Workbook()
    workbook.remove(workbook.active)  # Safely remove default 'Sheet'

    for column_name in columns_to_summarize:
        summary_data = []
        all_values_set = set()

        for file in os.listdir(folder_path):
            if file.lower().endswith(file_extension.lower()):
                full_path = os.path.join(folder_path, file)
                try:
                    df = clean_and_read_file(full_path)
                    if column_name in df.columns:
                        value_counts = df[column_name].value_counts(dropna=False).to_dict()
                        all_values_set.update(value_counts.keys())
                        row = {'Filename': file}
                        for val, count in value_counts.items():
                            row[f"{column_name} = {val}"] = count
                        summary_data.append(row)
                    else:
                        print(f"Column '{column_name}' not found in {file}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")

        # Build DataFrame and align columns
        all_columns = [f"{column_name} = {val}" for val in sorted(all_values_set)]
        df_summary = pd.DataFrame(summary_data)
        df_summary = df_summary[['Filename'] + [col for col in all_columns if col in df_summary.columns]]
        df_summary = df_summary.fillna(0).astype({col: 'int' for col in df_summary.columns if col != 'Filename'})

        # Create new sheet
        ws = workbook.create_sheet(title=column_name)
        for row in dataframe_to_rows(df_summary, index=False, header=True):
            ws.append(row)

    # Save Excel
    workbook.save(output_path)
    print(f"Summary saved to {output_path}")

# === Example Usage ===
if __name__ == "__main__":
    folder = r"c:\input_folder"
    columns = ["COMM_MODEL","STATUS_1"]  # Add as many columns as you want
    extension = ".rpt"  # or ".csv"
    output_file = r"Output_Summary.xlsx"

    summarize_multiple_columns(folder, columns, extension, output_file)
