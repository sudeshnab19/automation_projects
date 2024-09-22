# Read 'Retail_crosstab' sql resultset from Learning database via python using venv

import psycopg2             # Module needed to connect to DB
from openpyxl import Workbook   # Module needed to import excel workbook
from openpyxl.chart import BarChart, Reference
import pandas as pd             # Module needed to read the data

# create workbook
wb = Workbook()
# grab the active worksheet
ws = wb.active

connection = psycopg2.connect(database="Learning", user="postgres", password="password", host="localhost", port=5432) # connection established

cursor = connection.cursor()
column_names=['Cost_center','risk', 
            'risk_category', 
            'po_num', 
            'po_owner', 
            'vendor_num', 
            'po_amount_usd',
            'forecast_amount_usd',
            'invoice_to_date_usd',
            'accrual']                          # column names defined

cursor.execute(f"""select 
               {column_names[0]},
               {column_names[1]},
               {column_names[2]},
               {column_names[3]},
               {column_names[4]},
               {column_names[5]},
               {column_names[6]},
               {column_names[7]},
               {column_names[8]}
    ,(po_amount_usd-forecast_amount_usd) as {column_names[9]}
from
    purchaseorder;""")
          
ws.append(column_names)         # append the column names in the worksheet

# Fetch all rows from database
records = cursor.fetchall()
print("reading data from db..")
for record in records:
    ws.append(record)           # append each rows in the worksheet

connection.close()              # close connection post read

# Create Chart
chart = BarChart()
chart.title = "POs by risk category"
chart.x_axis.title = "forecast_amount_usd"
chart.y_axis.title = "risk_category"

# Add data to the chart
data = Reference(ws, min_col=1, max_col=10, min_row=2, max_row=9)
print("creating charts..")
chart.add_data(data)

# Add the chart to the worksheet
ws.add_chart(chart, "M2")
print("saving excel..")
wb.save("artifacts/purchase_project.xlsx")

