from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from datetime import datetime as dt
from datetime import timedelta



def fill_report(bucket):
    dateFrom = (dt.now() - timedelta(days=7)).strftime('%Y/%m/%d')
    dateTo = dt.now().strftime('%Y/%m/%d')
    dateString = f'{dateFrom} - {dateTo}'

    file_dateFrom = (dt.now() - timedelta(days=7)).strftime('%Y%m%d')
    file_dateTo = dt.now().strftime('%Y%m%d')
    if bucket == 'archive':
        fileName = f'report_{file_dateFrom}-{file_dateTo}.pdf'
    else:
        fileName = "Sales_Report.pdf"
    pdf = canvas.Canvas(f'/home/ec2-user/DiskoverProject/assets/{fileName}', pagesize=landscape(A4))

    tl_image = '/home/ec2-user/DiskoverProject/assets/most_sold.png'
    tr_image = '/home/ec2-user/DiskoverProject/assets/most_orders.png'
    bl_image = '/home/ec2-user/DiskoverProject/assets/revenues_generated.png'
    br_image = '/home/ec2-user/DiskoverProject/assets/most_busy_dates.png'

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

    return fileName

print(fill_report('live'))
