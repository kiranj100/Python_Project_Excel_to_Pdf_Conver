import pandas as pd
# this is for show all files in folders to set path
import glob
import openpyxl
from fpdf import FPDF
# this is special for file path library
from pathlib import Path

file_path = glob.glob("Invoices/*.xlsx")
# print(file_path)

for second_file in file_path:
    # pandas used read_excel to read .excel files
    df = pd.read_excel(second_file, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()

    # stem give us this 10001-2023.1.18 output and cut the .extension like .xlsx
    filename = Path(second_file).stem

        # it's give the list like['10001,'2023.1.18'] and zero position is 10001
    #invoice_No = filename.split("-")[0]

    # This is normal way
    # Date = filename.split("-")[1]

    # python distribute value accordingly to variables
    invoice_no, Date = filename.split("-")

    pdf.set_font(family="Times", style="B", size=18)
    pdf.cell(w=0, h=8, txt=f"Invoice No.{invoice_no}", ln=1)

    pdf.set_font(family="Times", style="B", size=18)
    pdf.cell(w=0, h=8, txt=f"Date: {Date}")



    # files name is this 10001-2023.1.18
    pdf.output(f"PDFS/{filename}.pdf")


