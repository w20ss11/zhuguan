from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader, PdfFileWriter

pdfs = ['1.pdf', '2.pdf', '3.pdf', '4.pdf']

merger = PdfFileMerger()

# for pdf in pdfs:
    # #print(pdf)
    # #pdfFileReader = PdfFileReader(pdf)
    # #print(pdfFileReader.getPage(0).mediaBox)
    # merger.append(open(pdf, 'rb'))
# with open('result.pdf', 'wb') as fout:
    # merger.write(fout)

output = PdfFileWriter()
for pdf in pdfs:#per pdf
    pdfFileReader = PdfFileReader(pdf)
    pages = []
    for i in range(pdfFileReader.getNumPages()):
        page = pdfFileReader.getPage(i)
        page.scaleTo(width=9, height=11.0)
        output.addPage(page)
outDoc = open('testOutput.pdf', 'wb')
output.write(outDoc)
outDoc.close()