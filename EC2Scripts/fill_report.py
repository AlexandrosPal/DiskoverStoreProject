import aspose.pdf as pdf
from datetime import datetime as dt
from datetime import timedelta
import sys

def fill_report():
    # Date and File variables
    dateFrom = (dt.now() - timedelta(days=7)).strftime('%Y/%m/%d')
    dateTo = dt.now().strftime('%Y/%m/%d')
    dateString = f'{dateFrom} - {dateTo}'

    file_dateFrom = (dt.now() - timedelta(days=7)).strftime('%Y%m%d')
    file_dateTo = dt.now().strftime('%Y%m%d')
    fileName = f'report_{file_dateFrom}-{file_dateTo}.pdf'

    # Files
    sys.path.append("/home/ec2-user/DiskoverProject")
    document = pdf.Document('assets/report_blueprint.pdf')
    stamp_most_sold = pdf.ImageStamp('assets/most_sold.png')
    stamp_most_orders = pdf.ImageStamp('assets/most_orders.png')
    stamp_revenues_generated = pdf.ImageStamp('assets/revenues_generated.png')
    stamp_most_busy_dates = pdf.ImageStamp('assets/most_busy_dates.png')

    # Date properties
    dateField = pdf.TextStamp(dateString)
    dateField.x_indent = 135
    dateField.y_indent = 528

    # Stamp_most_sold properties
    stamp_most_sold.x_indent = 60
    stamp_most_sold.y_indent = 255
    stamp_most_sold.width = 300
    stamp_most_sold.height = 220

    # Stamp_most_orders properties
    stamp_most_orders.x_indent = 60
    stamp_most_orders.y_indent = 10
    stamp_most_orders.width = 300
    stamp_most_orders.height = 220

    # Stamp_revenue_generated properties
    stamp_revenues_generated.x_indent = 450
    stamp_revenues_generated.y_indent = 255
    stamp_revenues_generated.width = 300
    stamp_revenues_generated.height = 220

    # Stamp_most_busy_dates properties
    stamp_most_busy_dates.x_indent = 450
    stamp_most_busy_dates.y_indent = 10
    stamp_most_busy_dates.width = 300
    stamp_most_busy_dates.height = 220

    # Page
    page = document.pages[1]

    # Add to page
    page.add_stamp(stamp_most_sold)
    page.add_stamp(stamp_most_orders)
    page.add_stamp(stamp_revenues_generated)
    page.add_stamp(stamp_most_busy_dates)
    page.add_stamp(dateField)

    # Flatten page
    page.flatten()

    # Save PDF
    document.save(f'assets/{fileName}')

    return fileName