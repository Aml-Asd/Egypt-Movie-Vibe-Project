import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

# 1. Load your new 200-place dataset
print("Loading Egypt places...")
df = pd.read_csv("data/egypt_places.csv")

# 2. Load the SAME AI model used for movies
# (Must be the same model, or the match won't work!)
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating vibe embeddings for places...")

# 3. Convert 'description' text to numbers
# We use the description column because that contains the "vibe" words
embeddings = model.encode(
    df["description"].tolist(),
    show_progress_bar=True
)

# 4. Save the mathematical vibes
np.save("data/place_vibes.npy", embeddings)

print(f"✅ Success! Generated embeddings for {len(df)} places.")
print("Saved to data/place_vibes.npy")