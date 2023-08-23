import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog


def select_pdf_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF  Files","*.pdf")])
    return file_paths


def select_output_location():
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=[("PDF Files", "*.pdf")])
    return output_path

def merge_pdfs(pdfs_files, output_path):
    merger = PyPDF2.PdfMerger()

    for file in pdfs_files:
            merger.append(file)

    with open(output_path, "wb") as output_file:
        merger.write(output_file)

    print("PDFs merged successfully!")

def main():
    root = tk.Tk()
    root.withdraw()

    pdf_files = select_pdf_files()
    if not pdf_files:
        print("No PDFs selected.")
        return
    output_path = select_output_location()
    if not output_path:
        print("No output path selected.")
        return
    merge_pdfs(pdf_files,output_path)


if __name__ == "__main__":
    main()