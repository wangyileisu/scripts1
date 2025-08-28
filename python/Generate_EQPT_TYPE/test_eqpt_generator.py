# 文件名: python/Generate_EQPT_TYPE/test_eqpt_generator.py

import pytest
import pandas as pd
import numpy as np
import os
import sys

# 导入你的主程序脚本中的函数
# 假设你的主程序脚本已经按照之前的建议修改过，将核心逻辑放在函数中
# 并将命令行参数解析部分放在 if __name__ == "__main__": 块中
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from python.Generate_EQPT_TYPE.generate_eqpt_type import process_data

# 创建一个用于测试的模拟 CSV 文件夹
# pytest 会自动为我们创建和清理这个临时文件夹
@pytest.fixture
def temp_dir_with_files(tmp_path):
    # 创建一个模拟的输入 CSV 文件
    csv_content = """EQUIPMENT_ID
TP-1234
TS-5678
t93a-9012
t93k-3456
UNK-0000
"""
    input_file = tmp_path / "data_sample.csv"
    input_file.write_text(csv_content)
    return str(input_file)

# 测试核心处理逻辑
def test_process_data_generates_correct_output(temp_dir_with_files):
    input_path = temp_dir_with_files
    output_path = temp_dir_with_files.replace('.csv', '_EQPT_TYPE.csv')

    # 调用核心处理函数，不依赖于命令行参数
    process_data(input_path, 'csv')

    # 验证输出文件是否存在
    assert os.path.exists(output_path)

    # 读取输出文件并验证内容
    df_output = pd.read_csv(output_path)

    assert 'EQPT_TYPE' in df_output.columns
    assert list(df_output['EQPT_TYPE']) == ['EXA', 'SS', 'EXA', 'SS', np.nan]

    # 清理文件
    os.remove(output_path)

# 测试文件不存在时的行为
def test_process_data_handles_file_not_found():
    with pytest.raises(SystemExit):
        process_data('non_existent.csv', 'csv')
