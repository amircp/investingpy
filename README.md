
# Investing.com Financial Historical Data Retriever

Tired of "403 Error Retry later" error from InvestPy package. Decided to create this tiny script that uses Selenium WebDriver to retrieve the last 30 days of any financial Instrument.

You can get any of the listing from Investing.com from Futures, Indices, Stocks and Currencies.



## Installation and Use

Just clone this repostiory

```
git clone 
```  

In your code editor:

```python
from investingpy import get_investing_last30days_data
df = get_investing_last30days_data("microsoft-corp", TickerType.STOCK)
print(df.head())
```

and then we get the Microsoft Historical data frame:




## Authors

- [@Bursatilboy](https://www.twitter.com/Bursatilboy)

