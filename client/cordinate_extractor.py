from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

def extract_cordinate(file_path:str, text_to_find:str):
    fp = open(file_path, 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)
    cor_x = 0
    cor_y = 0

    interpreter.process_page(list(pages)[0])
    layout = device.get_result()
    for lobj in layout:
        if isinstance(lobj, LTTextBox):
            x, y, text = lobj.bbox[0], lobj.bbox[1], lobj.get_text()
            if text.strip() == text_to_find:
                # import pdb; pdb.set_trace()
                cor_x = x + ((lobj.bbox[2]-x)/len(text_to_find))*2
                cor_y = y -2
                break
    return cor_x, cor_y
