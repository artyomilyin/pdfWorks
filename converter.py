from fpdf import FPDF
from PyPDF2 import PdfFileMerger
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')
pdf.cell(60, 10, 'Powered by FPDF.', 0, 1, 'C')
pdf.cell(60, 10, 'Powered by FPDF.', 0, 1, 'C')
pdf.cell(60, 10, 'Powered by FPDF.', 0, 1, 'C')
pdf.output('output/'
           'tuto1.pdf', 'F')
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello 2 World!')
pdf.cell(60, 10, 'Powered by 2 FPDF.', 0, 1, 'C')
pdf.cell(60, 10, 'Powered by 2 FPDF.', 0, 1, 'C')
pdf.cell(60, 10, 'Powered by 2 FPDF.', 0, 1, 'C')
pdf.output('output/'
           'tuto2.pdf', 'F')

merger = PdfFileMerger()
input1 = open('output/tuto1.pdf', 'rb')
input2 = open('output/tuto2.pdf', 'rb')
merger.append(input1)
merger.append(input2)
merger.write(open('output/global.pdf', 'wb'))
