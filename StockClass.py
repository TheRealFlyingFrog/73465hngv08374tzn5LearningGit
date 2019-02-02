import datetime

class Stock():

    owned = 0
    shares = 100

    def __init__(self,name,price,country,ranking,size):
        self.name    = name
        self.price   = price
        self.country = country
        self.ranking = ranking
        self.size    = size

    def stock_info(self):
        print("Name:    {0}".format(self.name))
        print("Price:   {0}".format(self.price))
        print("Country: {0}".format(self.country))
        print("Ranking: {0}".format(self.ranking))
        print("Size:    {0}".format(self.size))

    def buy_stock(self,shares,name,price):
        #get current date and time
        now = datetime.datetime.now()

        self.owned = shares
        print("You bought {0} Shares of {1} at {2} - {3}".format(str(shares),name,price,str(now) ))
        
    def sell_stock(self,shares,name,price):
        #get current date and time
        now = datetime.datetime.now()
        
        if (shares > self.owned):
            print("You dont own that many shares.")
        else:
            print("You sold {0} Shares of {1} at {2} - {3}".format(shares,name,price,str(now) ))
            print("You have {0} left".format(int(self.owned)-int(shares)))
            


