a = Portafolio(186)

print(a.Price("2021/11/04"))

print(a.Price("2019/11/04"))

print(a.Profit("2021/11/04","2019/11/04"))

print(a.CumulativeReturn("2021/11/04","2019/11/04"))

print(a.AnnualizedReturn("2021/11/04","2019/11/04"), a.DateDiff("2021/11/04","2019/11/04"))
