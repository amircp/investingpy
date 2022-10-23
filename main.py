from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd


class TickerType:
    COMMODITY = "commodities"
    CURRENCY = "currencies"
    STOCK = "equities"
    INDEX = "indices"


def get_investing_last30days_data(ticker: str, asset_type: str):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.execute_cdp_cmd("Page.setBypassCSP", {"enabled": True})

    driver.get(f"https://www.investing.com/{asset_type}/{ticker}-historical-data")

    source = driver.page_source
    driver.close()

    soup = BeautifulSoup(source, "lxml")
    table = soup.find('table', {"data-test": "historical-data-table"})
    table_body = table.find('tbody')
    split_rows = table_body.find_all("tr")
    data = []

    for row in split_rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values

    df = pd.DataFrame(data)
    df.rename(columns={0: "Date", 1: "Price", 2: "Open", 3: "High", 4: "Low", 5: "Volume", 6: "Change"}, inplace=True)

    return df


df = get_investing_last30days_data("microsoft-corp", TickerType.STOCK)
print(df.head())
