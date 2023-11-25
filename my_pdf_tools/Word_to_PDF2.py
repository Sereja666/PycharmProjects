from borb.pdf.canvas.color.color import HexColor
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF
from decimal import Decimal


from docx2pdf import convert
import docx2pdf


def docx_pdf():
    convert(rf'C:\Users\Sereja\Desktop\pdf\ЧТН_663_01_21_2_НП_500_000_ИГИ_ПЗ_Корректировка_.docx', rf'C:\Users\Sereja\Desktop\pdf\1111111.pdf')


def conc2():
    import aspose.words as aw

    # Load word document
    doc = aw.Document(rf'C:\Users\Sereja\Desktop\pdf\ЧТН_663_01_21_2_НП_500_000_ИГИ_ПЗ_Корректировка_21_05_2022.doc')

    # Save as PDF
    doc.save(rf'C:\Users\Sereja\Desktop\pdf\11111111.pdf')

def concatenate_two_documents():
    # Прочитайте первый PDF-файл
    with open(rf'1.pdf', "rb") as pdf_file_handle:
        input_pdf_001 = PDF.loads(pdf_file_handle)

    # Прочитайте второй PDF-файл
    with open(rf'2.pdf', "rb") as pdf_file_handle:
        input_pdf_002 = PDF.loads(pdf_file_handle)

    # Создайте новый PDF-файл, объединив два входных файла
    output_document = Document()
    output_document.append_document(input_pdf_001)
    output_document.append_document(input_pdf_002)

    # Написать PDF
    with open(rf'Big.pdf', "wb") as pdf_out_handle:
        PDF.dumps(pdf_out_handle, output_document)




concatenate_two_documents()