# 文件名: python/Generate_EQPT_TYPE/test_eqpt_generator.py

import pytest
import pandas as pd
from io import StringIO
import os
import sys

# 导入你的主程序脚本中的函数
sys.path.append('..') # Add parent directory to path to find the module
from Generate_EQPT_TYPE.generate_eqpt_type import process_data

# Create a mock CSV file to be used in tests
@pytest.fixture
def mock_csv_file(tmp_path):
    csv_content = """EQUIPMENT_ID
TP-1234
TS-5678
t93a-9012
t93k-3456
UNK-0000
"""
    input_file = tmp_path / "mock_data.csv"
    input_file.write_text(csv_content)
    return str(input_file)

# Test function to check if the 'EQPT_TYPE' column is correctly generated
def test_eqpt_type_generation(mock_csv_file):
    # Define output file path
    output_path = mock_csv_file.replace('.csv', '_EQPT_TYPE.csv')
    
    # Run the main processing function
    process_data(mock_csv_file, 'csv')
    
    # Check if the output file was created
    assert os.path.exists(output_path)
    
    # Read the output file and check its content
    df_output = pd.read_csv(output_path)
    
    assert 'EQPT_TYPE' in df_output.columns
    assert list(df_output['EQPT_TYPE']) == ['EXA', 'SS', 'EXA', 'SS', None]
    
    # Clean up the created file
    os.remove(output_path)

# Test case for a file with a different name
def test_another_file_name_csv(mock_csv_file, tmp_path):
    output_path = os.path.join(tmp_path, "mock_data_EQPT_TYPE.csv")
    
    process_data(mock_csv_file, 'csv')
    
    assert os.path.exists(output_path)
    os.remove(output_path)

# Test case for a missing 'EQUIPMENT_ID' column
def test_missing_column(tmp_path):
    csv_content = """SOME_OTHER_ID
1234
5678
"""
    input_file = tmp_path / "bad_data.csv"
    input_file.write_text(csv_content)
    
    # We expect the function to exit due to the error, so we test for a SystemExit exception
    with pytest.raises(SystemExit):
        process_data(str(input_file), 'csv')

# Test case for a non-existent file
def test_non_existent_file():
    with pytest.raises(SystemExit):
        process_data('non_existent.csv', 'csv')