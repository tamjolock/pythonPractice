import datetime

today = datetime.datetime.now()

""" tm = today.timestamp()

print(f"{tm}, {type(tm)}") """

mydate = datetime.date(2023,1,1)

# print(f"{mydate}, {type(mydate)}") 
# tm = today.timestamp()

mydatestr = datetime.datetime.strftime(mydate,"%년-%월-%일")

print(f"{mydatestr}, {type(mydatestr)}") 
