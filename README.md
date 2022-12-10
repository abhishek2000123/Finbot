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
