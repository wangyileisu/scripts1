# 文件名: python/Generate_EQPT_TYPE/generate_eqpt_type.py

import argparse
import pandas as pd
import sys

def process_data(input_csv_path, output_format):
    # Read the CSV file
    try:
        df = pd.read_csv(input_csv_path)
    except FileNotFoundError:
        print(f"Error: File {input_csv_path} does not exist.")
        sys.exit(1)

    # Ensure 'EQUIPMENT_ID' column exists
    if 'EQUIPMENT_ID' not in df.columns:
        print("Error: 'EQUIPMENT_ID' column does not exist in the CSV file.")
        sys.exit(1)

    # Define a function to set the value of the EQPT_TYPE column
    def set_eqpt_type(EQUIPMENT_ID):
        if 'TP' in str(EQUIPMENT_ID) or 't93a' in str(EQUIPMENT_ID):
            return 'EXA'
        elif 'TS' in str(EQUIPMENT_ID) or 't93k' in str(EQUIPMENT_ID) or 'TZ' in str(EQUIPMENT_ID) or 'TC' in str(EQUIPMENT_ID):
            return 'SS'
        else:
            return None

    # Apply the function to the 'EQUIPMENT_ID' column to create a new 'EQPT_TYPE' column
    df['EQUIPMENT_ID'] = df['EQUIPMENT_ID'].astype(str)
    df['EQPT_TYPE'] = df['EQUIPMENT_ID'].apply(set_eqpt_type)
    
    # Save the results based on the output format
    if output_format == 'csv':
        # Output to CSV file
        output_csv_path = f"{input_csv_path.rsplit('.', 1)[0]}_EQPT_TYPE.csv"
        try:
            df.to_csv(output_csv_path, index=False)
            print(f"Processing completed. CSV output saved to '{output_csv_path}'.")
        except Exception as e:
            print(f"Error saving CSV: {e}")
            sys.exit(1)
    elif output_format == 'excel':
        # Output to Excel file
        output_excel_path = f"{input_csv_path.rsplit('.', 1)[0]}_EQPT_TYPE.xlsx"
        try:
            df.to_excel(output_excel_path, index=False)
            print(f"Processing completed. Excel output saved to '{output_excel_path}'.")
        except Exception as e:
            print(f"Error saving Excel: {e}")
            sys.exit(1)

if __name__ == '__main__':
    # Create a parser object
    parser = argparse.ArgumentParser(description='Process IOD data and output to CSV or Excel.')

    # Add command line arguments
    parser.add_argument('input_csv', type=str, help='Path to the input CSV file.')
    parser.add_argument('output_format', type=str, choices=['csv', 'excel'], help='Output format (csv or excel).')

    # Parse command line arguments
    args = parser.parse_args()

    # Call the main processing function
    process_data(args.input_csv, args.output_format)