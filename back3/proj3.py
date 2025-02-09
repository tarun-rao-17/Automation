import PyPDF2
import os
import sys
merger=PyPDF2.PdfMerger()

for file in os.listdir():
    if file.endswith('.pdf'):
        merger.append(file)
    merger.write('merged.pdf')