from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

def add_text_to_pdf(input_pdf_path, output_pdf_path, data, x, y):
    # Load the existing PDF
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Iterate over each page in the PDF
    # for page_num in range(len(reader.pages)):
        # Get the current page
    page = reader.pages[0]
    # import pdb; pdb.set_trace()
    # TextPaint mTextPaint=new TextPaint();
    # Create a new PDF canvas
    c = canvas.Canvas(f"page{0}.pdf")
    # c.setFillColorRGB(0.6,0.4,0)
    c.setFillColorRGB(0.7,0,0)  #pink
    # c.setFillColorRGB(0.8,0.2,0.3)
    font_size = 10
    c.setFont("Helvetica-Bold", font_size)
    # c.setFont("Times-Roman", font_size)
    y -= font_size + 1
    x += 12
    # Draw the existing page onto the canvas
    # import pdb; pdb.set_trace()
    media_box = page.mediabox
    c.setPageSize((media_box.right, media_box.top))
    name =data['Column3'] + ' ' + data['Name of Family']
    # if len(name) > 34:
    #     name1 = name.split('kumar')
    # if len(name) > 25:
    #     i = name[24:].find(' ')
    #     name1 = name[:i]
    #     name2 = name[i:]
    inx = name.find(' ',23,-1)
    if inx != -1:
        c.drawString(x, y, name[:inx])
        y -= font_size + 1
        c.drawString(x, y, name[inx+1:])
    else:
        c.drawString(x, y, name)

    # c.setFillColorRGB(0.12,0.12,0.07)
    # c.setFillColorRGB(1,0.2,0.2)
    if data['Single/Family'] != '':
        y -= font_size + 5
        c.drawString(x, y, data['Single/Family'])
    if data['member for wedding']!='':
        y -= font_size + 5
        c.drawString(x, y, data['member for wedding'])

    if data['Place'] != '':
        y -= font_size + 5
        c.drawString(x, y, data['Place'])
    if data['member for dinner']!='':
        y -= font_size + 5
        c.drawString(x, y, data['member for dinner'])

    c.showPage()
    c.save()

    # Merge the modified page with the original PDF
    modified_page = PdfReader(f"page{0}.pdf").pages[0]
    page.merge_page(modified_page)
    writer.add_page(page)

    for p1 in reader.pages[1:]:
        writer.add_page(p1)

    # Write the modified PDF to a new file
    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

    print("Text added to the PDF successfully!")

# # Call the function and pass the file paths, text, and coordinates
# input_pdf_path = "D:\Sakshi\weddinginvitation\input\wedding_invitation.pdf"    # Replace with the actual path of the input PDF
# output_pdf_path = "output.pdf"  # Replace with the desired output path
# additional_text = "Additional"     # Replace with the text to be added
# # text_x = 153                            # Replace with the desired X coordinate
# # text_y = 127                           # Replace with the desired Y coordinate
# text_x =  12                           # Replace with the desired X coordinate
# text_y = 12                          # Replace with the desired Y coordinate

# add_text_to_pdf(input_pdf_path, output_pdf_path, additional_text, text_x, text_y)
