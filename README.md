# Currency_Web_Scraping Description:

Currency Comparison Calculation and Exchange Rates Stability Analysis from [X-Rates](https://www.x-rates.com) Website of 54 available currencies.

The main objectives of the project were as follows:

* Scrape currency exchange rates from the X-Rates website. 
* Currency converter:
Perform currency comparison calculations for various currency pairs by scraping the online calculator on [X-Rates](https://www.x-rates.com) website
* Analyze the stability of exchange rates in a specified time frame.
* Analyze the exchange rate of currencies and visualize the top rates at the current time.

You will find the project report in the  [Web Scrapping Project.pdf](https://github.com/mikasso01/Currency_Web_Scraping/blob/main/Web%20Scrapping%20Project.pdf)  with all the needed details:

* [Overall process.py](https://github.com/mikasso01/Currency_Web_Scraping/blob/main/Overall%20process.py) : The user interface where we can call all the 3 main functionalities.
* [currency_converter.py](https://github.com/mikasso01/Currency_Web_Scraping/blob/main/currency_converter.py) : A currency converter: convert a currency to another selected currency. It shows also the rate of exchange and the result.
* [rate.py](https://github.com/mikasso01/Currency_Web_Scraping/blob/main/rate.py) : Its main functionality is to scrap the content of the table of a
selected exchange currency rate compared to all other available currencies. The output will be two tables: you can choose the Top 10 exchange currency rate or show all available exchange currency rate.
* [yearly_rate.py](https://github.com/mikasso01/Currency_Web_Scraping/blob/main/yearly_rate.py) : This tool scrap the list of the yearly exchange rate of a given currency (the currency we want to convert) to the currency that we want to convert to in a given year (the user can choose the years between 2013 and our actual year.)

