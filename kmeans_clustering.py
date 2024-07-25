import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

# Change the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the dataset
file_path = 'Online Retail.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Display basic information about the dataset
print("\nBasic information about the dataset:")
print(df.info())

# Display summary statistics of the dataset
print("\nSummary statistics of the dataset:")
print(df.describe())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Fill missing values for the sake of this example
df['CustomerID'].fillna(0, inplace=True)

# Calculate the total amount spent by each customer
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
customer_df = df.groupby('CustomerID').agg({'TotalAmount': 'sum', 'InvoiceNo': 'count'}).reset_index()
customer_df.columns = ['CustomerID', 'TotalAmount', 'PurchaseFrequency']

# Normalize the data
scaler = StandardScaler()
customer_df[['TotalAmount', 'PurchaseFrequency']] = scaler.fit_transform(customer_df[['TotalAmount', 'PurchaseFrequency']])

# Display the first few rows of the normalized customer DataFrame
print("\nFirst few rows of the normalized customer DataFrame:")
print(customer_df.head())

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
customer_df['Cluster'] = kmeans.fit_predict(customer_df[['TotalAmount', 'PurchaseFrequency']])

# Display the first few rows of the customer DataFrame with cluster labels
print("\nFirst few rows of the customer DataFrame with cluster labels:")
print(customer_df.head())

# Save the resulting DataFrame to an Excel file
customer_df.to_excel('Customer_Clusters.xlsx', index=False)
print("Customer_Clusters.xlsx file has been saved in the PRODIGY_ML_02 directory.")
