import argparse    
import pandas as pd    
    
# Create a parser object    
parser = argparse.ArgumentParser(description='Process IOD data and output to CSV or Excel.')    
    
# Add command line arguments    
parser.add_argument('input_csv', type=str, help='Path to the input CSV file.')    
parser.add_argument('output_format', type=str, choices=['csv', 'excel'], help='Output format (csv or excel).')    
    
# Parse command line arguments    
args = parser.parse_args()    
    
# CSV file path    
input_csv_path = args.input_csv    
    
# Read the CSV file    
try:    
    df = pd.read_csv(input_csv_path)    
except FileNotFoundError:    
    # Output error when file does not exist    
    print(f"Error: File {input_csv_path} does not exist.")    
    exit()    
    
# Ensure 'EQUIPMENT_ID' column exists    
if 'EQUIPMENT_ID' not in df.columns:    
    # Output error when 'EQUIPMENT_ID' column does not exist    
    print("Error: 'EQUIPMENT_ID' column does not exist in the CSV file.")    
    exit()    
    
# Define a function to set the value of the EQPT_TYPE column    
def set_eqpt_type(EQUIPMENT_ID):    
    if 'TP' in EQUIPMENT_ID or 't93a' in EQUIPMENT_ID:    
        return 'EXA'    
    elif 'TS' in EQUIPMENT_ID or 't93k' in EQUIPMENT_ID or 'TZ' in EQUIPMENT_ID or 'TC' in EQUIPMENT_ID:
        return 'SS'    
    else:    
        return None  # Or return an empty string '', or another default value    
    
# Apply the function to the 'EQUIPMENT_ID' column to create a new 'EQPT_TYPE' column    
df['EQUIPMENT_ID'] = df['EQUIPMENT_ID'].astype(str)  
df['EQPT_TYPE'] = df['EQUIPMENT_ID'].apply(set_eqpt_type)

    
# Save the results based on the output format    
if args.output_format == 'csv':    
    # Output to CSV file    
    output_csv_path = f"{input_csv_path.rsplit('.', 1)[0]}_EQPT_TYPE.csv"    
    try:    
        df.to_csv(output_csv_path, index=False)    
        # Output message indicating successful save    
        print(f"Processing completed. CSV output saved to '{output_csv_path}'.")    
    except Exception as e:    
        # Output error when saving CSV file fails    
        print(f"Error: {e}")    
        print("Failed to save CSV file.")    
elif args.output_format == 'excel':    
    # Output to Excel file    
    output_excel_path = f"{input_csv_path.rsplit('.', 1)[0]}_EQPT_TYPE.xlsx"    
    try:    
        df.to_excel(output_excel_path, index=False)    
        # Output message indicating successful save    
        print(f"Processing completed. Excel output saved to '{output_excel_path}'.")    
    except Exception as e:    
        # Output error when saving Excel file fails    
        print(f"Error: {e}")    
        print("Failed to save Excel file.")