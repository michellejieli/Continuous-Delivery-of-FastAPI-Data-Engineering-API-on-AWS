import requests

url = "https://tasty.p.rapidapi.com/recipes/auto-complete"

querystring = {"prefix": "avocado"}

headers = {
    "X-RapidAPI-Key": "bd3adcf9d4msh6039b415026aa9dp14de35jsn843f232228bb",
    "X-RapidAPI-Host": "tasty.p.rapidapi.com",
}

response = requests.request("GET", url, headers=headers, params=querystring, timeout=15)


data = response.json()
print(data)
