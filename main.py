# create an app from fastapi
from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()


@app.get("/")
async def root():
    """This is the root of the API"""
    return {"message": "Need recipe ideas?"}


@app.get("/recipe/{recipe}")
async def get_recipe(recipe: str):
    """This is the root of the API"""
    url = "https://tasty.p.rapidapi.com/recipes/auto-complete"
    querystring = {"prefix": recipe}
    api_key = "bd3adcf9d4msh6039b415026aa9dp14de35jsn843f232228bb"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "tasty.p.rapidapi.com",
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring, timeout=5
    )
    print(response.text)
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
