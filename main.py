import PyPDF2
import os

merger = PyPDF2.PdfMerger()

file_list = os.listdir("pdf")
file_list.sort()

for file in file_list:
    if ".pdf" in file:
        merger.append(f'pdf/{file}')

merger.write("merged.pdf")

