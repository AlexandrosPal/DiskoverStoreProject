from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from datetime import datetime as dt
from datetime import timedelta

def add_image_to_existing_pdf():
    dateFrom = (dt.now() - timedelta(days=7)).strftime('%Y/%m/%d')
    dateTo = dt.now().strftime('%Y/%m/%d')
    dateString = f'{dateFrom} - {dateTo}'

    file_dateFrom = (dt.now() - timedelta(days=7)).strftime('%Y%m%d')
    file_dateTo = dt.now().strftime('%Y%m%d')
    fileName = f'report_{file_dateFrom}-{file_dateTo}.pdf'

    pdf = canvas.Canvas(f'/DiskoverProject/assets/{fileName}', pagesize=landscape(A4))

    tl_image = '/DiskoverProject/assets/most_sold.png'
    tr_image = '/DiskoverProject/assets/most_orders.png'
    bl_image = '/DiskoverProject/assets/revenues_generated.png'
    br_image = '/DiskoverProject/assets/most_busy_dates.png'

    image_width = 270
    image_height = 200

    x_indent = 50
 
    # Title
    pdf.setFont('Helvetica', 20)
    pdf.drawString(x_indent, 550, 'Diskover Disk Store Report')
    pdf.setFont('Helvetica', 14)
    pdf.drawString(x_indent, 530, 'Time period:')

    pdf.drawString(133, 529.5, dateString)

    # Top left
    pdf.drawString(x_indent, 490, 'Most sold products:')
    pdf.drawImage(tl_image, x_indent, 480-image_height, width=image_width, height=image_height)

    # Top right
    pdf.drawString(450, 490, 'Most sold products:')
    pdf.drawImage(tr_image, 450, 480-image_height, width=image_width, height=image_height)

    # Bottom left
    pdf.drawString(x_indent, 250, 'Most sold products:')
    pdf.drawImage(bl_image, x_indent, 240-image_height, width=image_width, height=image_height)

    # Bottom right
    pdf.drawString(450, 250, 'Most sold products:')
    pdf.drawImage(br_image, 450, 240-image_height, width=image_width, height=image_height)


    pdf.save()
        

add_image_to_existing_pdf()
