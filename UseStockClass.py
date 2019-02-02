from StockClass import Stock as Stock

aapl = Stock("","","","","")

aapl.name    = "Apple, Inc."
aapl.price   = "121.31"
aapl.country = "United States"
aapl.ranking = "AAA"
aapl.size    = "100"


print("------------------------")
print("      Stock Info")
print("------------------------")
aapl.stock_info()

print("------------------------")
print("       Buy Stock")
print("------------------------")
aapl.buy_stock(10,"aapl","100")

print("------------------------")
print("    Sell Stock fail")
print("------------------------")
aapl.sell_stock(100,"aapl","100")

print("------------------------")
print("      Sell Stock")
print("------------------------")
aapl.sell_stock(9,"aapl","100")
