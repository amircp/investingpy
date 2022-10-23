
# Investing.com Financial Historical Data Retriever

Tired of "403 Error Retry later" error from InvestPy package. Decided to create this tiny script that uses Selenium WebDriver to retrieve the last 30 days of any financial Instrument.

You can get any of the listing from Investing.com from Futures, Indices, Stocks and Currencies.



## Installation and Use

Just clone this repostiory

```
git clone git@github.com:amircp/investingpy.git
pip install -r requirements.txt
```  

In your code editor:

```python
from investingpy import get_investing_last30days_data
df = get_investing_last30days_data("microsoft-corp", "equities")
print(df.head())
```

and then we get the Microsoft Historical data frame:

<img width="523" alt="Captura de Pantalla 2022-10-22 a la(s) 20 10 31" src="https://user-images.githubusercontent.com/495849/197368427-93df6c81-2e16-4f0a-8fc4-55b58634fbf7.png">


## Notes
Some times the response could last a few large seconds due to investing.com blocking requests while selenium driver keeps waiting for them (they need to timeout).

## TO-DO
This script parsing this table could lead to create a new package to replace the InvestPy Package that currently is not working. 

- Create the capability to select date ranges from table
- Add some architecture using classes
- Convert to a Package and submit to Pypi

## Author

- [@Bursatilboy](https://www.twitter.com/Bursatilboy)

