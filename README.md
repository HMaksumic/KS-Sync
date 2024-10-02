# Unit4 Business World - Sync

## How to Use

1. **Create Folders**
   - Make sure to create the `/json` and `/excel` folders before starting:
     ```bash
     mkdir json
     mkdir excel
     ```

2. **Download Latest JSON Data**
   - Go to: [Brønnøysund Register Center API](https://data.brreg.no/enhetsregisteret/oppslag/enheter)
   - Download the latest JSON data and extract it to the `/json` folder.

3. **Add Excel File**
   - Place the `UBW.xlsx` file into the `/excel` folder.

4. **Activate the Virtual Environment**
   - Use the following command to activate the virtual environment:
     ```bash
     venv/scripts/activate
     ```

5. **Run the Scripts**

   - **Step 1:** Convert Excel to JSON:
     ```bash
     python convertToJSON.py
     ```
     
   - **Step 2:** Synchronize UBW Data:
     ```bash
     python syncUBW.py
     ```

   - **Step 3:** Convert to XLSX:
     ```bash
     python convertToXLSX.py
     ```

6. **Save Synchronized Data**
   - The synchronized data will be saved as `UBW_OUTPUT.xlsx` in the `/excel` folder.
