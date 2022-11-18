import requests

url = "https://yummly2.p.rapidapi.com/feeds/auto-complete"

querystring = {"q":"cookie"}

headers = {
	"X-RapidAPI-Key": "bd3adcf9d4msh6039b415026aa9dp14de35jsn843f232228bb",
	"X-RapidAPI-Host": "yummly2.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)