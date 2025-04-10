import requests
import pandas as pd
import datetime

# Base URL for the API
# API-dokumentation finns här: https://api.sgu.se/oppnadata/mineralrattigheter/ogc/features/v1/openapi?f=text%2Fhtml
base_url = "https://api.sgu.se/oppnadata/mineralrattigheter/ogc/features/v1"

# Fetch all collections
collections_response = requests.get(f"{base_url}/collections")
collections = collections_response.json()

# Get todays date for file name
today = datetime.datetime.today().strftime('%d-%m-%Y')


# Create a Pandas Excel writer using XlsxWriter as the engine
with pd.ExcelWriter(f'Mineralrättigheter {today}.xlsx', engine='xlsxwriter') as writer:
    # Iterate over collections and fetch items
    for collection in collections['collections']:
        collection_id = collection['id']
        items_response = requests.get(f"{base_url}/collections/{collection_id}/items")
        items = items_response.json()
        
        # Convert items to DataFrame
        df = pd.json_normalize(items['features'])

        # Remove columns that are not needed for the final output
        # Want to keep any  of these? Simply remove from the list in df.drop.
        df = df.drop(['type', 'geometry_name', 'geometry.type','properties.geom_area', 'properties.geom_length', 'geometry.coordinates'], axis=1, errors='ignore')
        
        # Convert column names to string and replace properties. with nothing (cleans up column names)
        df.columns = df.columns.astype(str)
        df.columns = df.columns.str.replace(r'^properties\.', '', regex=True)
        
        # Capitalize each word. Neat!
        df.columns = df.columns.str.title()


        sheet_name = collection_id
        # Clean up Excel sheet names based on list of corrections:
        corrections = [("bearbetningskoncessioner", "BBK"), ("ut", "UT"), ("industrimineral-", ""), ("-", " "), ("forfallna", "förfallna"), ("forbud", "förbud"), ("ansokta", "ansökta")]
        for old, new in corrections:
            sheet_name = sheet_name.replace(old, new)
        
        df.to_excel(writer, sheet_name[:30], index=False)

print(f"Data has been successfully written to Mineralrättigheter {today}.xlsx")