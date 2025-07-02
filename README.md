# Dynamic Crack Spread Analysis & Forecasting

## 🛢️ Advanced Quantitative Analysis for Gasoline Trading

This repository contains a comprehensive Python-based analysis framework for gasoline crack spread trading, designed to identify systematic trading opportunities through statistical modeling, regime detection, and predictive analytics.

---

## 📊 Project Overview

Crack spreads represent the fundamental economic driver of gasoline trading, measuring the profit margin refineries earn by processing crude oil into gasoline. This project applies advanced quantitative techniques to analyze crack spread dynamics, identify mean reversion patterns, and develop systematic trading signals.

### Key Value Propositions
- **Statistical Arbitrage Identification**: Quantify mean reversion opportunities in 3-2-1 crack spreads
- **Regime-Aware Modeling**: Adapt trading strategies to different market volatility environments  
- **Risk-Adjusted Performance**: Generate trading signals with robust risk management frameworks
- **Real-Time Analysis**: Automated data pipeline for continuous market monitoring

---

## 🎯 Analysis Objectives

1. **Crack Spread Dynamics**: Analyze historical relationships between gasoline and crude oil prices
2. **Mean Reversion Modeling**: Identify statistical arbitrage opportunities using time series analysis
3. **Volatility Regime Detection**: Implement Hidden Markov Models to detect market state changes
4. **Predictive Modeling**: Develop forecasting models for crack spread direction and magnitude
5. **Trading Strategy Development**: Create systematic entry/exit signals with performance backtesting

---

## 🔧 Technical Methodology

### Data Sources
- **EIA (Energy Information Administration)**: Gasoline and crude oil pricing, inventory data
- **NYMEX/CME**: RBOB gasoline and WTI crude oil futures
- **CFTC**: Commitments of Traders positioning data
- **API**: Weekly petroleum inventory reports

### Analytical Framework
```
📈 Data Pipeline → Statistical Analysis → Modeling → Strategy Development → Backtesting
```

### Key Technologies
- **Python 3.9+**: Core analysis environment
- **pandas/numpy**: Data manipulation and numerical computing
- **scipy/statsmodels**: Statistical analysis and time series modeling
- **scikit-learn**: Machine learning and regime detection
- **plotly/matplotlib**: Interactive visualization and reporting
- **requests/APIs**: Automated data collection

---

## 📁 Project Structure

```
Dynamic-Crack-Spread-Analysis-Forecasting/
│
├── data/
│   ├── raw/                    # Raw data from APIs
│   ├── processed/              # Cleaned and transformed datasets
│   └── external/               # External reference data
│
├── src/
│   ├── data_collection/        # API interfaces and data fetching
│   ├── analysis/               # Statistical analysis modules
│   ├── modeling/               # Predictive models and regime detection
│   ├── trading/                # Strategy development and backtesting
│   └── visualization/          # Plotting and dashboard creation
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_crack_spread_analysis.ipynb
│   ├── 03_regime_detection.ipynb
│   ├── 04_predictive_modeling.ipynb
│   └── 05_trading_strategy.ipynb
│
├── reports/
│   ├── executive_summary.md
│   ├── technical_analysis.html
│   └── trading_performance.pdf
│
├── tests/                      # Unit tests and validation
├── config/                     # Configuration files and API keys
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- EIA API key (free registration at https://www.eia.gov/opendata/)
- Git for version control

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/TBaby95/Dynamic-Crack-Spread-Analysis-Forecasting.git
   cd Dynamic-Crack-Spread-Analysis-Forecasting
   ```

2. **Create virtual environment**
   ```bash
   python -m venv crack_spread_env
   source crack_spread_env/bin/activate  # On Windows: crack_spread_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API access**
   ```bash
   cp config/config_template.yaml config/config.yaml
   # Add your EIA API key to config.yaml
   ```

### Quick Start
```python
from src.data_collection import EIADataFetcher
from src.analysis import CrackSpreadAnalyzer

# Initialize data fetcher
fetcher = EIADataFetcher(api_key='your_eia_key')

# Collect recent data
gasoline_data = fetcher.get_gasoline_prices()
crude_data = fetcher.get_crude_prices()

# Analyze crack spreads
analyzer = CrackSpreadAnalyzer()
crack_spreads = analyzer.calculate_321_crack_spread(gasoline_data, crude_data)
analysis_results = analyzer.run_mean_reversion_analysis(crack_spreads)
```

---

## 📈 Key Features

### 1. **Real-Time Data Pipeline**
- Automated EIA API integration
- Daily data updates and validation
- Historical data backtesting capability

### 2. **Statistical Analysis Engine**
- Crack spread calculation (3-2-1 and other ratios)
- Mean reversion testing with Augmented Dickey-Fuller
- Rolling correlation and volatility analysis
- Seasonal decomposition and trend analysis

### 3. **Regime Detection System**
- Hidden Markov Models for volatility regime identification
- Dynamic parameter estimation
- Regime-conditional strategy adjustment

### 4. **Predictive Modeling**
- ARIMA/GARCH models for time series forecasting
- Vector Error Correction for cointegration analysis
- Machine learning ensemble methods
- Monte Carlo simulation for scenario analysis

### 5. **Trading Strategy Framework**
- Systematic signal generation
- Risk-adjusted position sizing
- Performance attribution analysis
- Comprehensive backtesting with transaction costs

---

## 📊 Sample Results Preview

### Key Findings (Example)
- **Mean Reversion Frequency**: 73% probability of reversion within 5 trading days when crack spreads exceed 2 standard deviations
- **Optimal Entry Threshold**: Statistical significance at 1.8 standard deviation levels
- **Risk-Adjusted Returns**: Sharpe ratio of 1.4 with maximum drawdown of 8.2%
- **Seasonal Patterns**: Strong summer driving season premium averaging $0.12/gallon

### Performance Metrics
```
Strategy Performance (2019-2024)
├── Total Return: 18.4%
├── Annualized Sharpe: 1.4
├── Maximum Drawdown: -8.2%
├── Win Rate: 67%
└── Average Trade Duration: 3.2 days
```

---

## 📚 Documentation

- **[Technical Analysis Report](reports/technical_analysis.html)**: Detailed statistical methodology
- **[Executive Summary](reports/executive_summary.md)**: Key findings and trading recommendations
- **[API Documentation](docs/api_reference.md)**: Code reference and examples
- **[Strategy Performance](reports/trading_performance.pdf)**: Backtesting results and risk metrics

---

## 🔍 Usage Examples

### Basic Crack Spread Analysis
```python
# Load and analyze crack spread data
from src.analysis import CrackSpreadAnalyzer

analyzer = CrackSpreadAnalyzer()
spreads = analyzer.load_historical_data('2019-01-01', '2024-01-01')
results = analyzer.mean_reversion_analysis(spreads)
analyzer.plot_analysis_results(results)
```

### Regime Detection
```python
# Identify market regimes
from src.modeling import RegimeDetector

detector = RegimeDetector()
regimes = detector.fit_hmm_model(spreads, n_states=2)
detector.plot_regime_probabilities(regimes)
```

### Strategy Backtesting
```python
# Backtest trading strategy
from src.trading import CrackSpreadStrategy

strategy = CrackSpreadStrategy()
performance = strategy.backtest(spreads, start_date='2019-01-01')
strategy.generate_performance_report(performance)
```

---

## 🤝 Contributing

This project is designed for educational and professional demonstration purposes. For suggestions or improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**[Your Name]**  
Email: [your.email@domain.com]  
LinkedIn: [Your LinkedIn Profile]  
Portfolio: [Your Portfolio Website]

---

## 🏷️ Tags

`gasoline-trading` `crack-spreads` `quantitative-analysis` `python` `time-series` `trading-strategy` `energy-markets` `statistical-arbitrage` `regime-detection` `backtesting`

---

*This project demonstrates advanced quantitative analysis capabilities for institutional gasoline trading applications. All analysis is based on publicly available market data and academic research methodologies.*