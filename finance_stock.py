import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import matplotlib
matplotlib.use('TkAgg')  # Replace 'TkAgg' with your preferred backend

# Define the stock ticker symbols for top cement companies in India
tickers = {
    'UltraTech Cement': 'ULTRACEMCO.NS',
    'Ambuja Cements': 'AMBUJACEM.NS',
    'ACC': 'ACC.NS',
    'Shree Cement': 'SHREECEM.NS',
    'Dalmia Bharat': 'DALMIABHA.NS'
}

# Prompt the user to enter the time period for the data
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Download stock data for each company
stock_data = {company: yf.download(ticker, start=start_date, end=end_date) for company, ticker in tickers.items()}

# Create a DataFrame to hold the closing prices
closing_prices = pd.DataFrame({company: data['Close'] for company, data in stock_data.items()})
closing_prices.to_csv('closing_prices.csv', index=True)


# Plotting options

# 1. Line plot of closing prices for all companies with available data
plt.figure(figsize=(14, 7))
closing_prices.plot(ax=plt.gca())
plt.title('Stock Prices of Top Cement Companies in India - Closing Prices')
plt.xlabel('Date')
plt.ylabel('Stock Price (INR)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plotting line graph of closing prices for all companies with available data
plt.figure(figsize=(14, 7))
for company in closing_prices.columns:
    plt.plot(closing_prices.index, closing_prices[company], label=company)

plt.title('Stock Prices of Top Cement Companies in India - Closing Prices')
plt.xlabel('Date')
plt.ylabel('Stock Price (INR)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# 2. Candlestick chart (OHLC) for Shree Cement (if data available)
if 'Shree Cement' in stock_data:
    plt.figure(figsize=(14, 7))
    shree_cement_data = stock_data['Shree Cement']
    shree_cement_data.reset_index(inplace=True)
    shree_cement_data['Date'] = shree_cement_data['Date'].map(mdates.date2num)
    ax = plt.subplot()
    candlestick_ohlc(ax, shree_cement_data.values, width=0.6, colorup='g', colordown='r')
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.title('Shree Cement Candlestick Chart')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 3. Volume and closing price plot for UltraTech Cement (if data available)
if 'UltraTech Cement' in stock_data:
    plt.figure(figsize=(14, 10))
    
    # Subplot 1: Closing Prices
    plt.subplot(2, 1, 1)
    ultratech_data = stock_data['UltraTech Cement']
    plt.plot(ultratech_data['Close'], label='Close Price', color='blue')
    plt.title('UltraTech Cement Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Stock Price (INR)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    
    # Subplot 2: Volume
    plt.subplot(2, 1, 2)
    plt.bar(ultratech_data.index, ultratech_data['Volume'], color='purple')
    plt.title('UltraTech Cement Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.xticks(rotation=45)
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# 4. Moving averages plot for Ambuja Cements (if data available)
if 'Ambuja Cements' in stock_data:
    plt.figure(figsize=(14, 7))
    
    ambuja_data = stock_data['Ambuja Cements']
    plt.plot(ambuja_data['Close'], label='Close Price', color='blue')
    plt.plot(ambuja_data['Close'].rolling(window=50).mean(), label='50-Day Moving Average', linestyle='--', color='orange')
    plt.plot(ambuja_data['Close'].rolling(window=200).mean(), label='200-Day Moving Average', linestyle='--', color='green')
    
    plt.title('Ambuja Cements Closing Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Stock Price (INR)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()