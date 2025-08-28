# IOD Data Processing Script

This Python script processes IOD (Input/Output Data) files by categorizing equipment types based on equipment IDs and outputs the results in CSV or Excel format.

## Features

- Automatically detects equipment type from equipment ID
- Handles file not found and missing column errors
- Outputs processed data in CSV or Excel format
- Preserves original filename while adding `_EQPT_TYPE` suffix to output files

## Requirements

- Python 3.6+
- pandas (`pip install pandas`)
- openpyxl (for Excel output, `pip install openpyxl`)

## Installation

```
pip install pandas openpyxl
```

## Usage

### Basic Command

```
python process_iod.py <input_csv_path> <output_format>
```

### Parameters

| Parameter        | Description                | Valid Values        |
| :--------------- | :------------------------- | :------------------ |
| `input_csv_path` | Path to the input CSV file | Any valid file path |
| `output_format`  | Desired output format      | `csv` or `excel`    |

### Examples

Process data and output as CSV:

```
python process_iod.py equipment_data.csv csv
```

Process data and output as Excel:

```
python process_iod.py /path/to/data.csv excel
```

## Equipment Type Mapping Logic

The script categorizes equipment based on the following rules:

| Equipment ID Contains       | EQPT_TYPE |
| :-------------------------- | :-------- |
| 'TP' or 't93a'              | EXA       |
| 'TS', 't93k', 'TZ', or 'TC' | SS        |
| Other values                | `None`    |

## Output Files

The script generates output files in the same directory as the input file with modified names:

- **CSV output**: `[original_filename]_EQPT_TYPE.csv`
- **Excel output**: `[original_filename]_EQPT_TYPE.xlsx`

## Error Handling

The script will exit with descriptive error messages for:

- Missing input file
- Missing 'EQUIPMENT_ID' column in input file
- File permission issues during save operations

## Sample Success Messages

- CSV output:
  `Processing completed. CSV output saved to 'equipment_data_EQPT_TYPE.csv'.`
- Excel output:
  `Processing completed. Excel output saved to 'equipment_data_EQPT_TYPE.xlsx'.`