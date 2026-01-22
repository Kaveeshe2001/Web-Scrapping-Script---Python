import pandas as pd

df = pd.read_excel('supermarket_sales.xlsx')

df = df[['Gender', 'Product line', 'Total']]
#print(df)

pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum', fill_value=0, margins=True).round(0)

pivot_table.to_excel('pivot_table_output.xlsx', 'Report', startrow=4)