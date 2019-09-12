import requests
r = requests.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/AAPL")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2= requests.post(url= url, data= data)