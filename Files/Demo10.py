import PyPDF2 as pdf
try:
    f = open("NAC.pdf","rb")
    pf = pdf.PdfFileReader(f)
    print(pf.getDocumentInfo())
    print(pf.getNumPages())
    po = pf.getPage(3)
    text = po.extractText()
    print(text)
except FileNotFoundError:
    print("File not Found")