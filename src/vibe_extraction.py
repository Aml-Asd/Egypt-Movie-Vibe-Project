import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

# Load movie data
df = pd.read_csv("data/movies_1000.csv")

# Remove empty overviews (just in case)
df = df[df["overview"].notna()]

# Load NLP model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating vibe embeddings...")

# Convert overview text to vectors
embeddings = model.encode(
    df["overview"].tolist(),
    show_progress_bar=True
)

# Save vectors
np.save("data/movie_vibes.npy", embeddings)

# Save clean movie info
df.to_csv("data/movies_clean.csv", index=False)

print("✅ Vibe embeddings saved")
