# 📊 Price Cluster Analysis

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange)

A Python tool that analyzes cryptocurrency price levels using K-means clustering, identifying key price zones and standard deviation bands.

## 🚀 Features

- 📈 Downloads historical cryptocurrency data via `yfinance`
- 🔍 Implements K-means clustering for price level analysis
- 📊 Visualizes price clusters with standard deviation bands
- 📉 Supports logarithmic price scaling
- ⚙️ Configurable clustering parameters

## 📋 Prerequisites

Before running the script, ensure you have Python 3.7+ installed on your system.

## 🔧 Installation

1. Clone the repository
```bash
git clone https://github.com/YavuzAkbay/k-means-clustering.git
cd k-means-clustering
```

2. Install required packages
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Basic usage with default parameters:
```python
from k-means-clustering import CryptoClusterAnalysis

analyzer = CryptoClusterAnalysis()
analyzer.load_data().fit().plot_results()
```

2. Custom analysis:
```python
analyzer = CryptoClusterAnalysis(
    ticker="ETH-USD",
    k=5,  # number of clusters
    cent_meth="K means",
    train_n=365,  # training period
    plot_band=True
)
analyzer.load_data(start="2020-01-01").fit().plot_results()
```

## ⚙️ Configuration Options

| Parameter | Description | Default |
|-----------|-------------|---------|
| ticker | Cryptocurrency symbol | "BTC-USD" |
| k | Number of clusters | 3 |
| cent_meth | Clustering method | "K means" |
| train_n | Training period (days) | 252 |
| plot_band | Show SD bands | True |

## 📊 Example Output

The script generates a visualization showing:
- Historical price data on logarithmic scale
- Cluster center lines
- Standard deviation bands for each cluster
- Customizable date range and parameters

## 🔍 Code Structure

```
crypto-cluster-analysis/
│
├── crypto_clustering.py   # Main script
├── requirements.txt      # Dependencies
├── README.md            # Documentation
└── .gitignore          # Git ignore rules
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- `yfinance` for cryptocurrency data access
- `scikit-learn` for K-means clustering implementation
- Matplotlib for visualization capabilities

## 📧 Contact

Your Name - [akbay.yavuz@gmail.com](mailto:akbay.yavuz@gmail.com)

Project Link: [https://github.com/YavuzAkbay/K-Means-Clustering](https://github.com/YavuzAkbay/K-Means-Clustering)

---
⭐️ If you found this project helpful, please consider giving it a star!
