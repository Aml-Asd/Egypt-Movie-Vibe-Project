import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# --- 1. SETUP: Load all data ---
print("Loading system memory...")
movies_df = pd.read_csv("data/movies_clean.csv")
places_df = pd.read_csv("data/egypt_places.csv")

movie_vibes = np.load("data/movie_vibes.npy")
place_vibes = np.load("data/place_vibes.npy")

# --- 2. INPUT: Choose a movie ---
# Let's pick a famous one to test, e.g., "Interstellar" or the first one in your list
# You can change this index to test different movies
movie_index = 0 
selected_movie = movies_df.iloc[movie_index]

print(f"\n🎬 SELECTED MOVIE: {selected_movie['title']}")
print(f"📝 Plot: {selected_movie['overview'][:100]}...")

# --- 3. THE AI BRAIN (Cosine Similarity) ---
# Get the vibe vector for the selected movie
selected_vibe = movie_vibes[movie_index].reshape(1, -1)

# Compare this movie's vibe against ALL 200 egypt places
similarities = cosine_similarity(selected_vibe, place_vibes)

# --- 4. OUTPUT: Get Top 3 Matches ---
# Get indices of the highest scores
top_indices = similarities[0].argsort()[-3:][::-1]

print("\n🌍 RECOMMENDED PLACES IN EGYPT:")
print("="*40)

for idx in top_indices:
    place = places_df.iloc[idx]
    score = similarities[0][idx]
    
    print(f"📍 Name: {place['place_name']}")
    print(f"🏙️  City: {place['city']}")
    print(f"✨ Vibe Match: {int(score * 100)}%")
    print(f"🏨 Hotel: {place['hotels']}")
    print(f"🎯 Activities: {place['top_activities']}")
    print("-" * 40)