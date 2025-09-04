import yfinance as yf
from datetime import date
import datetime

stock_abbr = ["aapl", "abnb", "adbe", "amc", "amd", "amzn", "arm", "avgo", "ba", "baba", "bac", "blnk", "cmg", "cost", "crm", "crox",
          "dash", "dell", "dis", "docu", "duol", "etsy", "gm", "gme", "goog", "gs", "hd", "ibm", "intc", "jnj", "jpm", "low",
          "lulu", "mchp", "mcd", "meli", "meta", "mrna", "ms", "msft", "nflx", "nke", "nvda", "nvts", "orcl", "panw", "pfe",
          "pins", "pltr", "pony", "pypl", "qcom", "qubt", "rng", "sofi", "tmus", "tsla", "tsm", "txn", "ual", "uber", "wfc",
          "wmt", "zm"]

stock_names = ["Apple Inc", "Airbnb Inc", "Adobe Inc", "AMC Entertainment Holdings Inc", "Advanced Micro Devices Inc",
               "Amazon.com Inc", "Arm Holdings PLC", "Broadcom Inc", "Boeing Co", "Alibaba Group Holding Ltd",
               "Bank of America Corp", "Blink Charging Co", "Chipotle Mexican Grill Inc", "Costco Wholesale Corp",
               "Salesforce Inc", "Crocs Inc", "DoorDash Inc", "Dell Technologies Inc", "Walt Disney Co", "DocuSign Inc",
               "Duolingo Inc", "ETSY Inc", "General Motors Co", "GameStop Corp", "Alphabet Class C", "Goldman Sachs Group Inc",
               "Home Depot Inc", "International Business Machines Corp", "Intel Corp", "Johnson & Johnson", "JPMorgan Chase & Co",
               "Lowe's Companies Inc", "Lululemon Athletica Inc", "Microchip Technology Inc", "McDonald's Corp", "MercadoLibreInc",
               "Meta Platforms Inc", "Moderna Inc", "Morgan Stanley", "Microsoft Corp", "Netflic Inc", "Nike Inc", "NVDIA Corp",
               "Navitas Semiconductor Corp", "Oracle Corp", "Palo Alto Networks Inc", "Pfizer Inc", "Pinterest Inc",
               "Palantir Technologies Inc", "Pony AI Inc", "PayPal Holdings Inc", "Qualcomm Inc", "Quantum Computing Inc",
               "RingCentral Inc", "SoFi Technologies Inc", "T-Mobile US Inc", "Tesla Inc", "Taiwan Semiconductor Manufacturing Co Ltd",
               "Texas Instruments Inc", "United Airlines Holdings Inc", "Uber Technologies Inc", "Wells Fargo & Co",
               "Walmart Inc", "Zoom Communications Inc"]

for abbreviation, name in zip(stock_abbr, stock_names):
    stock = yf.Ticker(abbreviation)
    historical = stock.history(period="1d", interval="1m")
    print(name + " " + str(date.today()) + " Open: " + str(stock.info["regularMarketOpen"]))

    if datetime.datetime.now().hour >= 16:
        print(name + " " + str(date.today()) + " Close: " + str(historical['Close'][0]))
    else:
        print(name + " " + str(date.today()) + " Now: " + str(stock.info["currentPrice"]))
        

#apple = yf.Ticker("aapl")
#apple_historical = apple.history(period="1d", interval="1m")
#print(apple_historical)