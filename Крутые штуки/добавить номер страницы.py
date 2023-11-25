
import os

from PyPDF4.pdf import PdfFileReader, PdfFileWriter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_page_pdf(num, tmp):
    c = canvas.Canvas(tmp)
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

    for i in range(1, num + 1):
        val_str = f'привет {i}'
        c.setFont('Arial', 20)
        c.drawString((210 // 2) * mm, (4) * mm, val_str)
        c.showPage()
    c.save()


def add_page_numgers(pdf_path):
    """
    Add page numbers to a pdf, save the result as a new pdf
    @param pdf_path: path to pdf
    """
    tmp = "__tmp.pdf"

    writer = PdfFileWriter()
    with open(pdf_path, "rb") as f:
        reader = PdfFileReader(f, strict=False)
        n = reader.getNumPages()

        # create new PDF with page numbers
        create_page_pdf(n, tmp)

        with open(tmp, "rb") as ftmp:
            number_pdf = PdfFileReader(ftmp)
            # iterarte pages
            for p in range(n):
                page = reader.getPage(p)
                numberLayer = number_pdf.getPage(p)
                # merge number page with actual page
                page.mergePage(numberLayer)
                writer.addPage(page)

            # write result
            if writer.getNumPages():
                newpath = pdf_path[:-4] + "_numbered.pdf"
                with open(newpath, "wb") as f:
                    writer.write(f)
        os.remove(tmp)

add_page_numgers(r'C:\Users\Sereja\Desktop\qqq\111.pdf')