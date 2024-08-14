import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, LogFormatter

# Define the inputs
k = 3  # number of clusters
cent_meth = "K means"  # cluster method (K means or K median)
train_n = 252  # number of bars back to train on
plot_band = True  # show standard deviation bands

# Load the price data
ticker = "BTC-USD"
data = yf.download(ticker, start="2019-01-01", end="2022-02-26")
close_prices = data["Close"]

# Define the functions
def euc_dist(p, q):
    return np.sqrt((p - q) ** 2)

def center_method(arry, method):
    if method == "K means":
        return np.mean(arry)
    else:
        return np.median(arry)

def sd_method(arry, mu, ddof=0):
    if cent_meth == "K means":
        return np.std(arry, ddof=ddof)
    else:
        return np.sqrt(np.sum((arry - mu) ** 2) / (len(arry) - ddof))

def vector_params(k, *arrays):
    mus = []
    sds = []
    ns = []
    for arr in arrays:
        mu = center_method(arr, cent_meth)
        sd = sd_method(arr, mu)
        n = len(arr)
        mus.append(mu)
        sds.append(sd)
        ns.append(n)
    return mus, sds, ns

# Perform K-means clustering
kmeans = KMeans(n_clusters=k)
kmeans.fit(close_prices[-train_n:].values.reshape(-1, 1))

# Get the cluster centers and standard deviations
mus, sds, ns = vector_params(k, *[kmeans.cluster_centers_.flatten() for _ in range(k)])

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(close_prices, label="Close Prices")
plt.yscale('log')  # Apply logarithmic scale to the y-axis

# Plot the cluster centers as horizontal lines
for i in range(k):
    plt.axhline(y=mus[i], color='r', linestyle='--', label=f"Cluster {i+1}")

    if plot_band:
        plt.axhline(y=mus[i] + sds[i], color='g', linestyle='--', label=f"Cluster {i+1} + SD")
        plt.axhline(y=mus[i] - sds[i], color='b', linestyle='--', label=f"Cluster {i+1} - SD")

# Customizing y-axis ticks
plt.gca().yaxis.set_major_locator(LogLocator(base=10.0, numticks=10))
plt.gca().yaxis.set_major_formatter(LogFormatter(labelOnlyBase=False))

plt.legend()
plt.title('Bitcoin Price with Cluster Centers (Log Scale)')
plt.xlabel('Date')
plt.ylabel('Price (Log Scale)')
plt.grid(True, which="both", ls="--")
plt.show()
