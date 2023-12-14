import glob
from fpdf import FPDF
from pathlib import Path

files = glob.glob("Text_Files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for file_content in files:
    # Add a page to PDF documents for each text file
    pdf.add_page()

    # Get the file without Extension
    # and convert into title case e.g (=for example Cat)
    file_name = Path(file_content).stem
    pdf_names = file_name.title()

    # Add the Name of PDF
    pdf.set_font(family="Times", style="B", size=20)
    pdf.cell(w=50, h=10, txt=pdf_names, ln=1)

    # Get the Content of Each text file
    with open(file_content, 'r') as file:
        content = file.read()

    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=6, txt=content)

# Produce the pdf
pdf.output("result.pdf")
