import PyPDF2
pdf_file_obj = open('meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
print(pdf_reader.getNumPages())
page_obj = pdf_reader.getPage(0)
print(page_obj.extractText())
pdf_file_obj.close()