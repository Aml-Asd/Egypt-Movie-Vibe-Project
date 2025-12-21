import requests
from config import API_KEY

url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"
response = requests.get(url)

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("Success! First movie title:")
    print(data["results"][0]["title"])
else:
    print("Something went wrong")
