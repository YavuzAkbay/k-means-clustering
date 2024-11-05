import yfinance as yf
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, LogFormatter

class CryptoClusterAnalysis:
    def __init__(self, ticker="BTC-USD", k=3, cent_meth="K means", train_n=252, plot_band=True):
        """
        Initialize the Crypto Cluster Analysis.
        
        Parameters:
        - ticker (str): Cryptocurrency ticker symbol
        - k (int): Number of clusters
        - cent_meth (str): Clustering method ("K means" or "K median")
        - train_n (int): Number of bars for training
        - plot_band (bool): Whether to show standard deviation bands
        """
        self.ticker = ticker
        self.k = k
        self.cent_meth = cent_meth
        self.train_n = train_n
        self.plot_band = plot_band
        self.close_prices = None
        self.kmeans = None
        
    @staticmethod
    def euc_dist(p, q):
        """Calculate Euclidean distance between two points."""
        return np.sqrt((p - q) ** 2)
    
    def center_method(self, arry):
        """Calculate center based on specified method."""
        if self.cent_meth == "K means":
            return np.mean(arry)
        return np.median(arry)
    
    def sd_method(self, arry, mu, ddof=0):
        """Calculate standard deviation based on specified method."""
        if self.cent_meth == "K means":
            return np.std(arry, ddof=ddof)
        return np.sqrt(np.sum((arry - mu) ** 2) / (len(arry) - ddof))
    
    def vector_params(self, *arrays):
        """Calculate parameters for each cluster."""
        mus = []
        sds = []
        ns = []
        for arr in arrays:
            mu = self.center_method(arr)
            sd = self.sd_method(arr, mu)
            n = len(arr)
            mus.append(mu)
            sds.append(sd)
            ns.append(n)
        return mus, sds, ns
    
    def load_data(self, start="2024-01-01", end="2024-11-04"):
        """Load price data from Yahoo Finance."""
        data = yf.download(self.ticker, start=start, end=end)
        self.close_prices = data["Close"]
        return self
    
    def fit(self):
        """Perform K-means clustering on the data."""
        self.kmeans = KMeans(n_clusters=self.k)
        self.kmeans.fit(self.close_prices[-self.train_n:].values.reshape(-1, 1))
        return self
    
    def plot_results(self):
        """Plot the results with cluster centers and bands."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.close_prices, label="Close Prices")
        plt.yscale('log')
        
        # Get cluster parameters
        mus, sds, ns = self.vector_params(*[self.kmeans.cluster_centers_.flatten() 
                                          for _ in range(self.k)])
        
        # Plot cluster centers and bands
        for i in range(self.k):
            plt.axhline(y=mus[i], color='r', linestyle='--', 
                       label=f"Cluster {i+1}")
            if self.plot_band:
                plt.axhline(y=mus[i] + sds[i], color='g', linestyle='--', 
                          label=f"Cluster {i+1} + SD")
                plt.axhline(y=mus[i] - sds[i], color='b', linestyle='--', 
                          label=f"Cluster {i+1} - SD")
        
        # Customize plot
        plt.gca().yaxis.set_major_locator(LogLocator(base=10.0, numticks=10))
        plt.gca().yaxis.set_major_formatter(LogFormatter(labelOnlyBase=False))
        plt.legend()
        plt.title(f'{self.ticker} Price with Cluster Centers (Log Scale)')
        plt.xlabel('Date')
        plt.ylabel('Price (Log Scale)')
        plt.grid(True, which="both", ls="--")
        plt.show()

if __name__ == "__main__":
    # Example usage
    analyzer = CryptoClusterAnalysis(
        ticker="BTC-USD",
        k=3,
        cent_meth="K means",
        train_n=252,
        plot_band=True
    )
    
    analyzer.load_data().fit().plot_results()