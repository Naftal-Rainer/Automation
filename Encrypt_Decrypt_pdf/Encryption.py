from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileReader

result = PdfFileWriter()

file = PdfFileReader('Magazine.pdf')

length = file.numPages

for i in range(length):
    pages = file.getPage(i)
    result.addPage(pages)
    
password = 'pam&Lab890'

result.encrypt(password)

with open('Magazines.pdf','wb') as f:
    result.write(f)