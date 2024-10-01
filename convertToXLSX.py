import pandas as pd
import json

# Step 1: Read the JSON file
with open('json/UBW_updated.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Step 2: Convert JSON data to pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Write DataFrame to an Excel file
df.to_excel('excel/UBW_OUTPUT.xlsx', index=False)

print("Conversion complete. The Excel file has been saved as 'UBW_OUTPUT.xlsx'.")