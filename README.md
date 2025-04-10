Script to fetch the latest available info from the SGU Mineralrättigheter API (https://api.sgu.se/oppnadata/mineralrattigheter/ogc/features/v1/openapi?f=text%2Fhtml) and produce an Excel sheet.

Needs Python 3 with libraries Pandas and XLSXWriter installed. 

Script removes columns by default, you can change this in the code on line 30. The script also does some cleaning up of the column names and sheet names, such as changing long names to abbreviations (ex: bearbetningskoncession to BBK), this is needed due to Excels limit on 31 characters in sheet names. Some swedish words in the sheet names are also modified to include proper åäö characters, such as replacing forfallna with förfallna.

An example of running this script from Windows CMD: python "C:\Users\Linnar\Documents\SGU MRR API to Excel.py"

This will produce an Excel file named Mineralrättigheter DD-MM-YYYY.xlsx in the Documents directory.
