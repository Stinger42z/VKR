import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert_pdf_to_txt(path, char_margin, line_margin):
    resource_manager = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams(char_margin = char_margin, line_margin = line_margin)
    device = TextConverter(resource_manager, retstr, codec = codec, laparams = laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(resource_manager, device)
    password = ""
    maxpages = 0
    caching = True
    check_extractable = False
    pagenos = set()
    j = 1
    for page in PDFPage.get_pages(fp, pagenos, maxpages = maxpages,
                                  password = password,
                                  caching = caching,
                                  check_extractable = check_extractable):
        try:
            interpreter.process_page(page)
        except:
            print(j)
            print(page)

        j += 1

    fp.close()
    device.close()
    text = retstr.getvalue()
    retstr.close()

    return text