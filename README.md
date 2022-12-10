# Finbot
Rasa version:3.1

CMPE 252 Final Rasa Project

Abhishek Sathyanarayanan

SJSU ID-016683186

## Converstion flow

User input-> Hi

```sh
bot:-  Hi My name is Finbot.Your companion and partner in the financial world.I can perform the following operations
       - Get price of stock
       - Add stock to portfolio
       - Get financial indicators for a stock
       - Perform forex conversion
       - Check portfolio
```
Asking Stock price of a company

User input->What is the stock price of Walmart

```sh
bot:-The price is 145.31
```

Technical indicators for the above stock.The bot provides the RSI for the stock. It also gives you an option of giving a birief overview of the metric depending on your choice

user input->Give me some technical indicators for the stock

```sh
I can provide the Relative strength Index Measure of the stock would you like me to provide a brief overview of the metric
```

If user enters yes

```sh
User input->Yes

Bot:-The relative strength index (RSI) measures the price momentum of a stock or other security. The basic idea behind the RSI is to measure how quickly traders are bidding the price of the security up or down. The RSI plots this result on a scale of 0 to 100.Readings below 30 generally indicate that the stock is oversold, while readings above 70 indicate that it is overbought. Traders will often place this RSI chart below the price chart for the security, so they can compare its recent momentum against its market price.

The Relative Strength Index (RSI) metric for Walmart stock is 44.11
```

If the user says no

```sh
User input->No
Bot:-The Relative Strength Index (RSI) metric for Walmart stock is 44.11
```

Get to know about the company before buying the stock

User input:-What does this company do

```sh
bot:-America's largest retailer by sales, Walmart operated over 10,500 stores under 46 banners at the end of fiscal 2022, selling a variety of general merchandise and grocery items. Its home market accounted for 82% of sales in fiscal 2022, with Mexico and Central America (6%) and Canada (4%) its largest external markets. In the United States at the namesake banner, around 56% of sales come from grocery, 32% from general merchandise, and 11% from health and wellness items. The company operates several e-commerce properties apart from its eponymous site, including Flipkart and shoes.com (it also owns a roughly 10% stake in Chinese online retailer JD.com). Combined, e-commerce accounted for about 13% of fiscal 2022 sales.
```

Buy the stock and add it to portfolio.The transaction gets stored in the portfolio Database

```sh
User input:-I want to buy this stock

Bot:-How much stock would you like to buy

User input:-23

Bot:-Would you like to confirm the purchase of 23 stocks of Walmart

User:-Yes

Bot:-The transaction has been logged
```

View the stocks that you have added to your portfolio

User input:-Show me my portfolio

```sh
Walmart,WMT,23
```

Perform Forex Conversions

User input:-Convert 100 USD to INR

```sh
The price is 8246.3
```
We can also perform chain forex conversion here we will convert 100 USD to INR and INR to GBP


```sh
User input:-Convert 100 USD to INR

Bot:-The price is 8246.3

User input:-Convert it to GBP

Bot:-The price is 81.634

```
Get weather info in your area

User input:-How is the weather

```sh
Bot:-The temperature is 51.4 degre
```
