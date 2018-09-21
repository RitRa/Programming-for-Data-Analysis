import datetime as d

today = d.datetime.today()
dayofweek = today.weekday()


if dayofweek == 1:
    print("It's Tuesday!")
else:
    print("Unfortunately, It's not Tuesday")
