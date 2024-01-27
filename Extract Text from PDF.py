import fitz # To extract Text from PDF File
# import tabula # To extract Tables from PDF File
import os

# Extracting Texts from PDF
# file_path = "Files\\SenPDFText.pdf"

if os.path.exists(file_path):
 with fitz.open(file_path) as pdf:
  for page in pdf:
        print(page.get_text())
else:
    print(f"Error: File not found at path '{file_path}'. Make sure the file exists.")

# Extracting Tables from PDF
# table = tabula.read_pdf("Files\\SenPDFTable.pdf",pages=1)
# print(table)
