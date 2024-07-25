# PRODIGY_ML_02: Customer Segmentation using K-means Clustering

## Overview

This project aims to perform customer segmentation using K-means clustering on the Online Retail dataset. The objective is to group customers based on their purchasing behavior, which can help businesses understand their customer base better and tailor marketing strategies accordingly.

## Dataset

The dataset used for this project is the "Online Retail" dataset, which contains transactional data from a UK-based online retail store. The dataset includes the following columns:
- **InvoiceNo**: Invoice number (unique identifier for each transaction)
- **StockCode**: Product code (unique identifier for each product)
- **Description**: Product description
- **Quantity**: The quantity of each product per transaction
- **InvoiceDate**: Date and time of the transaction
- **UnitPrice**: Unit price of each product
- **CustomerID**: Unique identifier for each customer
- **Country**: Country of the customer

## Steps to Complete the Task

### 1. Data Preprocessing

1. **Load the Dataset**:
   The dataset is loaded into a pandas DataFrame for further analysis.

2. **Handle Missing Values**:
   Missing values in the `CustomerID` and `Description` columns are addressed by dropping the rows with missing `CustomerID` values.

3. **Calculate RFM Metrics**:
   - **Recency**: Days since the last purchase.
   - **Frequency**: Total number of purchases.
   - **Monetary**: Total amount spent.

4. **Normalize the Data**:
   The RFM metrics are normalized to bring them to a common scale for clustering.

### 2. K-means Clustering

1. **Determine the Optimal Number of Clusters**:
   The Elbow method is used to determine the optimal number of clusters by plotting the within-cluster sum of squares (WCSS) against the number of clusters.

2. **Apply K-means Clustering**:
   K-means clustering is applied to segment customers into groups.

### 3. Save the Results

The resulting clusters are saved to an Excel file named `Customer_Clusters.xlsx` for further analysis.

## Code

The main script for this project is `kmeans_clustering.py`, which performs the entire process from loading the dataset to saving the clustering results.

### Running the Script

To run the script, use the following command in your terminal:
python kmeans_clustering.py

Results
The clustering results are saved in the Customer_Clusters.xlsx file, which contains the following columns:

CustomerID: Unique identifier for each customer.
TotalAmount: The total amount spent by each customer.
PurchaseFrequency: The frequency of purchases made by each customer.
Cluster: The cluster label assigned to each customer by the K-means clustering algorithm.

Conclusion
This project demonstrates the application of K-means clustering for customer segmentation. By understanding the different segments of customers, businesses can tailor their marketing strategies to better meet the needs of each group.

Repository Structure
kmeans_clustering.py: Main script for the project.
Online Retail.xlsx: Dataset used for the project.
Customer_Clusters.xlsx: Output file containing the clustering results.


Author
Laleeth Sachin Naik S P

License
This project is licensed under the MIT License - see the LICENSE file for details.
