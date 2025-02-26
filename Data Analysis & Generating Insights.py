import pandas as pd

# Load the data
data = pd.read_csv(r'C:\Users\Capaciti\Documents\Digital_Innovators\Data+\Lesson13_14\Our Sales_transactions.csv')

# Overview of the data
print(data.shape)  # (20, 9)
print(data.dtypes)

# Summary statistics
total_sales = data['Total_Sale'].sum()
average_sale = data['Total_Sale'].mean()
total_quantity = data['Quantity'].sum()

print(f'Total Sales: {total_sales}')
print(f'Average Sale: {average_sale}')
print(f'Total Quantity Sold: {total_quantity}')

# Sales by product
sales_by_product = data.groupby('Product').agg({'Total_Sale': 'sum', 'Quantity': 'sum'}).reset_index()
print(sales_by_product)

# Convert 'Date' to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Sales over time
sales_over_time = data.groupby('Date')['Total_Sale'].sum().reset_index()
print(sales_over_time)

