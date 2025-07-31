
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path as pt

filepaths = glob.glob('invoices/*.xlsx')


for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    filename = pt(filepath).stem
    invoicen, date = filename.split('-')

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice #{invoicen}', ln=1)

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Date: {date}')

    pdf.output(f"PDFs/{filename}.pdf")
