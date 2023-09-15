import datetime
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn import covariance, cluster
import yfinance as yf

# Input file containing company symbols
input_file = 'company_symbol_mapping.json'

# Load the company symbol map
with open(input_file, 'r') as f:
    company_symbols_map = json.load(f)

symbols, names = np.array(list(company_symbols_map.items())).T

# Load the historical stock quotes
start_date = datetime.datetime(2019, 1, 1)
end_date = datetime.datetime(2021, 1, 1)  # Extend the date range for more data

# Initialize lists to store opening and closing quotes
opening_quotes = []
closing_quotes = []

for symbol in symbols:
    try:
        # Fetch historical data for the symbol
        df = yf.Ticker(symbol).history(start=start_date, end=end_date)

        # Check if data is available
        if not df.empty:
            # Extract opening and closing quotes
            opening_quotes.append(df['Open'].values)
            closing_quotes.append(df['Close'].values)
    except Exception as e:
        print(f"Error fetching data for symbol {symbol}: {e}")

# Convert lists to NumPy arrays
opening_quotes = np.array(opening_quotes)
closing_quotes = np.array(closing_quotes)

# Compute differences between opening and closing quotes
quotes_diff = closing_quotes - opening_quotes

# Replace NaN values with zeros
quotes_diff = np.nan_to_num(quotes_diff)

# Compute the standard deviation, excluding columns with zero standard deviation
std_dev = np.std(quotes_diff, axis=0)
std_dev[std_dev == 0] = 1.0  # Replace zero standard deviation with 1.0

# Normalize the data by dividing by the standard deviation
X = quotes_diff / std_dev

# Transpose X for clustering
X = X.T

# Create a graph model
edge_model = covariance.GraphicalLassoCV()

# Train the model
with np.errstate(invalid='ignore'):
    edge_model.fit(X)

# Build clustering model using Affinity Propagation model
_, labels = cluster.affinity_propagation(edge_model.covariance_)
num_labels = labels.max()

# Print the results of clustering
for i in range(num_labels + 1):
    cluster_symbols = symbols[labels == i]
    cluster_names = [company_symbols_map[symbol] for symbol in cluster_symbols]
    print(f"Cluster {i + 1}: {', '.join(cluster_names)}")
