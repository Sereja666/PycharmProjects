import os
import time

from PIL import Image

file_pdf = r'C:\PyTest\passport.jpg'
# file_txt = r'C:\PyTest\passport.txt'
def scan(r):
    path_kern = r'C:\Program Files (x86)\ABBYY FineReader 15'
    # /optionsFile batch.options.xml
    # command = r'cd "{kern_path}" & "FineCmd.exe" "{pdf}" /lang Mixed /out "{txt}" /quit'
    file_txt = f'C:\\PyTest\\passport_{r}.txt'
    command = f'cd "{path_kern}" & "FineCmd.exe" "{file_pdf}" /lang Mixed /optionsFile "C:\\Users\\Sereja\\Documents\\pasport\\batch.options.xml" /out "{file_txt}" /quit'
    os.system(command.format(kern_path=path_kern, pdf=file_pdf, txt=file_txt))

# with open(file_txt, encoding='utf-8') as ft:
#     for i in ft:
#         print(i)

def rotate(r):
    im = Image.open(file_pdf)
    im_rotate = im.rotate(r, expand=True)
    im_rotate.save(file_pdf, quality=95)
    im.close()

r = 0
i = 0
while i <= 4:
    scan(r)
    time.sleep(2)
    rotate(r)
    r += 90
    i+=1