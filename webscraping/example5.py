import requests
import pandas as pd

# Fake Store API endpoint
url = "https://fakestoreapi.com/products"

# Fetch product data from the API
response = requests.get(url)
if response.status_code == 200:
    products = response.json()
else:
    products = []

# Create a DataFrame from the products
df = pd.DataFrame(products)

# Save to CSV
df.to_csv("fake_store_products.csv", index=False)
print("Data saved to 'fake_store_products.csv'")