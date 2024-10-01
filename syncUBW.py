import json

def update_ubw_data(ubw_file_path, enheter_alle_file_path, output_file_path):
    # Read UBW data
    with open(ubw_file_path, 'r', encoding='utf-8') as file:
        ubw_data = json.load(file)

    # Read Enheter Alle data
    with open(enheter_alle_file_path, 'r', encoding='utf-8') as file:
        enheter_alle_data = json.load(file)

    # Create a dictionary for quick lookup of Enheter Alle data
    enheter_alle_dict = {item['organisasjonsnummer']: item for item in enheter_alle_data}

    # Fields to update (UBW field name: Enheter Alle field name)
    fields_to_update = {
        'registrertIMvaregisteret': 'registrertIMvaregisteret',
        'konkurs': 'konkurs',
        'underAvvikling': 'underAvvikling',
        'underTvangsavviklingEllerTvangsopplosning': 'underTvangsavviklingEllerTvangsopplosning',
        'Navn': 'navn'
    }

    # Update UBW data
    for ubw_item in ubw_data:
        org_num = ubw_item.get('Org.nummer')
        if org_num in enheter_alle_dict:
            enheter_item = enheter_alle_dict[org_num]
            for ubw_field, enheter_field in fields_to_update.items():
                if enheter_field in enheter_item:
                    ubw_item[ubw_field] = enheter_item[enheter_field]

    # Write updated UBW data to output file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(ubw_data, file, indent=4, ensure_ascii=False)

    print(f"Updated data written to {output_file_path}")

ubw_file_path = 'json/UBW.json'
enheter_alle_file_path = 'json/enheter_alle.json'
output_file_path = 'json/UBW_updated.json'
update_ubw_data(ubw_file_path, enheter_alle_file_path, output_file_path)