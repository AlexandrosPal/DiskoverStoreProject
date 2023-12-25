from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def add_image_to_existing_pdf(input_pdf, output_pdf, image_path, x, y, width, height):
    pdf = canvas.Canvas(input_pdf, pagesize=landscape(A4))
    
    pdf.setFont('Helvetica', 20)
    pdf.drawString(30, 550, 'Diskover Disk Store Report')
    pdf.setFont('Helvetica', 14)
    pdf.drawString(30, 530, 'Time period:')
    pdf.drawImage(image_path, 0, 0, width=100, height=100)

    pdf.save()
        

add_image_to_existing_pdf('/DiskoverProject/assets/haha.pdf', 'report20231217-20231224.pdf', '/DiskoverProject/assets/most_sold.png', 60, 255, 200, 220)
