# K-Means-Clustering

Bitcoin Price Clustering Analysis
This repository includes a Python script that applies K-means clustering to historical Bitcoin (BTC-USD) price data and displays the results. The analysis employs financial and economic approaches to detect price clusters, revealing insights into the structure of Bitcoin's price changes over time.

Overview
In this analysis, we use the K-means clustering technique to divide Bitcoin prices into various clusters based on their historical values. This method allows us to detect probable patterns and clusters in the price data, which can help us understand the volatility and behaviour of Bitcoin values.

Key Features
K-means Clustering: Categorizes Bitcoin prices into k clusters.
Center Methods: Uses K-means cluster centers and provides options for different central tendency measures (mean or median).
Standard Deviation Bands: Optionally displays standard deviation bands around cluster centers to visualize variability.
Logarithmic Price Scale: Applies a logarithmic scale to the price axis for better visualization of price distributions.

Dependencies
yfinance for downloading historical price data
numpy for numerical operations
pandas for data manipulation
sklearn for K-means clustering
matplotlib for plotting

Analysis
The script clusters comparable price moves to give a detailed perspective of Bitcoin's price behaviour. The K-means clustering method aids in discovering different regimes or clusters within historical price data, which may then be used for additional financial analysis or trading methods.

By visualising the clusters and their standard deviations, you can see how Bitcoin values fluctuate around several central locations, providing insight into price volatility and trend behaviour.
