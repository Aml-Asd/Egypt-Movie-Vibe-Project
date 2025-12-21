import requests
import pandas as pd
from config import API_KEY

movies = []

TOTAL_PAGES = 50   # 50 pages × 20 movies = 1000 movies

for page in range(1, TOTAL_PAGES + 1):
    print(f"Fetching page {page}...")

    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
    response = requests.get(url).json()

    for item in response.get("results", []):
        movies.append({
            "movie_id": item["id"],
            "title": item["title"],
            "overview": item["overview"],
            "genre_ids": item["genre_ids"],
            "popularity": item["popularity"]
        })

df = pd.DataFrame(movies)
df.to_csv("data/movies_1000.csv", index=False)

print("✅ Saved movies_1000.csv")
