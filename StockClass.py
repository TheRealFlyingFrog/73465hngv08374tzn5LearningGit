import datetime

class Stock():

    __owned = 0
    __shares = 100
    __time = datetime.datetime.now()

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
        self.__owned = shares
        print("You bought {0} Shares of {1} at {2} - {3}".format(str(shares),name,price,str(self.__time) ))
        
    def sell_stock(self,shares,name,price):
        if (shares > self.__owned):
            print("You dont own that many shares.")
        else:
            print("You sold {0} Shares of {1} at {2} - {3}".format(shares,name,price,str(self.__time) ))
            print("You have {0} left".format(str(self.__owned-shares)))
            


