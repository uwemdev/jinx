Solana (SOL) Price & RSI Tracker
This project tracks the real-time price of Solana (SOL) and calculates the Relative Strength Index (RSI) based on the 4-hour chart using data from Binance. The tracker updates every 30 minutes and provides valuable information for making informed trading decisions.

## Features
Fetches the current price of Solana (SOL) every 30 minutes.
Calculates the RSI using the most recent 4-hour candlestick data from Binance.
Displays the current SOL price and RSI value in the terminal.

## Technologies Used
  Python: Programming language for scripting.
  ccxt: Library to interact with cryptocurrency exchanges.
  requests: For fetching data from APIs.
  numpy: For calculating the RSI.
  GitHub Codespaces: Cloud-based development environment.

## Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/solana-price-tracker.git
cd solana-price-tracker
pip install ccxt requests beautifulsoup4 numpy
python tracker.py
