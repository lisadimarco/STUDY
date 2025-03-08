import pandas as pd

# Load inventory data
inventory = pd.read_csv('inventory.csv')

# Select first 10 rows for Staten Island location
staten_island = inventory.head(10)

# Get product descriptions for Staten Island
product_request = staten_island.product_description

# Select seeds from Brooklyn location
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

# Add in_stock column
inventory['in_stock'] = inventory.apply(lambda row: True if row.quantity > 0 else False, axis = 1)

# Calculate total value of inventory
inventory['total_value'] = inventory.price * inventory.quantity

# Combine product type and description
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
