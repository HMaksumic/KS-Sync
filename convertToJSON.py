import pandas as pd
import json
import numpy as np

def excel_to_json(excel_file_path, output_json_path, sheet_name='Leverandørliste_'):
    # Load the Excel file and the specific sheet
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    # Convert the DataFrame to a list of dictionaries
    json_data = df.to_dict(orient='records')

    # Additional fields to be added
    additional_fields = [
        'registrertIMvaregisteret',
        'konkurs',
        'underAvvikling',
        'underTvangsavviklingEllerTvangsopplosning'
    ]

    # Replace NaN values with None and add additional fields
    for item in json_data:
        for key, value in item.items():
            if isinstance(value, float) and np.isnan(value):
                item[key] = None
        
        # Add additional fields with null value if they don't exist
        for field in additional_fields:
            if field not in item:
                item[field] = None

    # Write the JSON data to a .json file
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

    print(f"Data successfully written to {output_json_path}")

excel_file_path = 'excel/UBW.xlsx'
output_json_path = 'json/UBW.json'
excel_to_json(excel_file_path, output_json_path)