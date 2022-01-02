### Importing libraries and data
# Import required modules.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# These settings produce nice plots in a Jupyter notebook.
plt.style.use('fivethirtyeight')
%matplotlib inline

# Read in the data.
stock_data = pd.read_csv('datasets/stock_data.csv', parse_dates=['Date'],
                        index_col='Date').dropna()
benchmark_data = pd.read_csv('datasets/benchmark_data.csv', parse_dates=['Date'],
                            index_col='Date').dropna()


### Exploratory data analysis - Part 1
# Display summary for stock_data.
print('Stocks\n')
print(stock_data.info())
print(stock_data.head())

# Display summary for benchmark_data.
print('\nBenchmarks\n')
print(benchmark_data.info())
print(benchmark_data.head())


### Exploratory data analysis - Part 2
# Visualize the stock_data.
stock_data.plot(subplots=True, title='Stock Data')

# Summarize the stock_data.
stock_data.describe()


### Exploratory data analysis - Part 3
# Plot the benchmark_data.
benchmark_data.plot(title='S&P 500')

# Summarize the benchmark_data.
benchmark_data.describe()


### Calculating inputs for the Sharpe Ratio: Daily stock returns
# Calculate daily stock_data returns.
stock_returns = stock_data.pct_change()

# Plot the daily returns.
stock_returns.plot()

# Summarize the daily returns.
stock_returns.describe()


### Calculating inputs for the Sharpe Ratio: Daily S&P 500 returns
# Calculate daily benchmark_data returns.
sp_returns = benchmark_data['S&P 500'].pct_change()

# Plot the daily returns.
sp_returns.plot()

# Summarize the daily returns.
sp_returns.describe()


### Calculating excess returns for Amazon and Facebook vs. S&P 500
# Calculate the difference in daily returns.
excess_returns = stock_returns.sub(sp_returns, axis=0)

# Plot the excess_returns.
excess_returns.plot()

# Summarize the excess_returns.
excess_returns.describe()


### The Sharpe Ratio: The average difference in daily returns stocks vs. S&P 500
# Calculate the mean of excess_returns.
avg_excess_return = excess_returns.mean()

# Plot avg_excess_returns.
avg_excess_return.plot.bar(title='Mean of Return Difference')


### The Sharpe Ratio: Standard deviation of the return difference
# Calculate the standard deviations.
sd_excess_return = excess_returns.std()

# Plot the standard deviations.
sd_excess_return.plot.bar(title='Standard Deviation of the Return Difference')


### The Sharpe Ratio: Ratio of average and standard deviation of excess returns
# Calculate the daily sharpe ratio.
daily_sharpe_ratio = avg_excess_return.div(sd_excess_return)

# Annualize the sharpe ratio.
annual_factor = np.sqrt(252)
annual_sharpe_ratio = daily_sharpe_ratio.mul(annual_factor)

# Plot the annualized sharpe ratio.
annual_sharpe_ratio.plot.bar(title='Annualized Sharpe Ratio: Stocks vs S&P 500')


### Conclusion
# While both Amazon and Facebook stocks have similar standard deviations, Amazon
# receives a higher Sharpe Ratio due to comparatively higher reward for a given
# unit of risk in the observed time period.
buy_amazon = True
