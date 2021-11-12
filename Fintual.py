#%%
import requests
import datetime
from dateutil import parser

class Portafolio:
    def __init__(self, stock):
        self.stock = stock

    def Price(self,date):
        self.date = date
        response = requests.get(
        f"https://fintual.cl/api/real_assets/{self.stock}/days",
        params= {'date': self.date}
        )
        return response.json()['data'][0]['attributes']['price']    
        
    def Profit(self, date1, date2):
        self.date1 = date1
        self.date2 = date2
        return self.Price(date1) - self.Price(date2)

    def CumulativeReturn(self, date1, date2):
        self.date1 = date1
        self.date2 = date2
        return (self.Price(date1) - self.Price(date2)) / self.Price(date2) 

    def AnnualizedReturn(self, date1, date2):
        self.date1 = date1
        self.date2 = date2
        return (1 + self.CumulativeReturn(date1,date2))**(365/self.DateDiff(date1,date2)) - 1

    def DateDiff(self, date1, date2):
        self.date1 = date1
        self.date2 = date2
        return (parser.parse(date1) - parser.parse(date2)).days


a = Portafolio(186)

print(a.Price("2021/11/04"))

print(a.Price("2019/11/04"))

print(a.Profit("2021/11/04","2019/11/04"))

print(a.CumulativeReturn("2021/11/04","2019/11/04"))

print(a.AnnualizedReturn("2021/11/04","2019/11/04"), a.DateDiff("2021/11/04","2019/11/04"))
