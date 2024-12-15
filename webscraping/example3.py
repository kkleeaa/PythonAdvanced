import requests

url="https://www.ebay.com/sch/i.html?_kw=laptop"

response=requests.get(url)

if response.status_code==200:
    print(response.text)
else:
    print(f"Failed to retireve content from{url}")