# Machine Learning Trading Algorithm for Gold

## Overview
A machine learning-based trading bot that uses Support Vector Machine (SVM) classification to predict and trade the GLD ETF. The algorithm identifies market patterns to make directional predictions for either long or short positions.

 [Watch the Implementation Tutorial by Matt Macarty ](https://www.youtube.com/watch?v=l6nE7oDywOY)

## Features
- Pattern recognition using Support Vector Machine (SVM)
- Automated trading execution
- Real-time market data processing
- Support for both long and short positions
- Integration with GLD ETF trading

## Prerequisites
- Python environment (virtualenv or conda recommended)
- Lumibot library (`pip install lumibot`)
- Brokerage account (Alpaca, Interactive Brokers, or Tradier)
- Market data provider access (Yahoo Finance or Polygon)

## Setup Instructions

### 1. Environment Configuration
1. Create and activate a Python virtual environment
2. Install dependencies:
   ```bash
   pip install lumibot
   ```
### 2. Configuration
Create a `.env` file with the following:
- Brokerage API credentials
- Data provider keys
- Logging preferences
- Backtesting parameters

### 3. Implementation

The core strategy is implemented as a Lumibot Strategy class:

```python
from lumibot.strategies import Strategy

class ML(Strategy):
    def on_trading_iteration(self):
        # 1. Market data acquisition
        # 2. Signal generation
        # 3. Order execution
        order = self.create_order(option.symbol, 1, "buy")
        self.submit_order(order)
```

### 4. Backtesting
- Use Lumibot's backtesting framework with PolygonDataBacktesting
- Analyze performance metrics:
  - Annualized returns
  - Sharpe ratio
  - Maximum drawdown
  - Win rate
- Visualize results through equity curves and trade distribution analysis

### 5. Strategy Refinement
- Monitor and analyze backtesting results
- Fine-tune parameters
- Implement robust risk management
- Validate against overfitting

## Risk Management
- Position sizing rules
- Stop-loss implementation
- Portfolio diversification
- Risk-reward ratio monitoring

## Important Notes
- Ensure high-quality market data
- Implement proper risk management
- Regularly validate and adjust the strategy
- Monitor system performance

## Disclaimer
This project is for educational purposes only. Trading involves substantial risk of loss and is not suitable for all investors. Past performance of backtests does not guarantee future results.

## License
MIT License 2025