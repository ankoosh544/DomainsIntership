import requests

url = "https://zozor54-whois-lookup-v1.p.rapidapi.com/"

querystring = {"format":"json","domain":"123.it"}

headers = {
    'x-rapidapi-host': "zozor54-whois-lookup-v1.p.rapidapi.com",
    'x-rapidapi-key': "0980325a57msh9cd865ebced10f1p172dc8jsnfb43cf846e57"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)