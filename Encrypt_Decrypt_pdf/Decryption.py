from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileReader

result = PdfFileWriter()

file = PdfFileReader('Magazines.pdf')

    
password = 'pam&Lab890'

if file.isEncrypted:
    file.decrypt(password)
        
    for i in range(31):
        pages = file.getPage(i)
        result.addPage(pages)
        
    with open('Magazines1.pdf','wb') as f:
        result.write(f)
    
    print('File decrypted successfully')
    
else:
    
    print('File is not encrypted')