from openpyxl import load_workbook
from openpyxl.styles import Font

# Load workbook and select sheet
wb = load_workbook('pivot_table_output.xlsx')
sheet = wb['Report']

sheet['A1'] = "Supermarket Sales Report"
sheet['A2'] = "January"
sheet['A1'].font = Font(name='Arial', size=20, bold=True)
sheet['A2'].font = Font(name='Arial', size=14, italic=True)

wb.save('report_january.xlsx')    