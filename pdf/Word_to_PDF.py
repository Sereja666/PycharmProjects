import sys
import os
import comtypes.client


files = os.listdir(r'C:\Users\Sereja\Desktop\Новая папка')


for file in files:
    if 'docx' in file:
        wdFormatPDF = 17
        a = rf'C:\Users\Sereja\Desktop\Новая папка\{file}'
        in_file = a
        pdfname = file.replace('docx', 'pdf')
        out_file = rf'C:\Users\Sereja\Desktop\pdf\{pdfname}'

        word = comtypes.client.CreateObject('Word.Application')
        word.Visible = False
        doc = word.Documents.Open(in_file)
        doc.SaveAs(out_file, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
    else:
        wdFormatPDF = 17
        in_file = rf'C:\Users\Sereja\Desktop\Новая папка\{file}'
        pdfname = file.replace('doc', 'pdf')
        out_file = rf'C:\Users\Sereja\Desktop\pdf\{pdfname}'

        word = comtypes.client.CreateObject('Word.Application')
        word.Visible = False
        doc = word.Documents.Open(in_file)
        doc.SaveAs(out_file, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()