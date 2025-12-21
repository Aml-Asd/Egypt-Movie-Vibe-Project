import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Egypt Movie Vibe Recommender",
    page_icon="🎬",
    layout="wide"
)

# --- 1. LOAD DATA (Cached for speed) ---
@st.cache_data
def load_data():
    movies = pd.read_csv("data/movies_clean.csv")
    places = pd.read_csv("data/egypt_places.csv")
    movie_vibes = np.load("data/movie_vibes.npy")
    place_vibes = np.load("data/place_vibes.npy")
    return movies, places, movie_vibes, place_vibes

try:
    movies_df, places_df, movie_vibes, place_vibes = load_data()
    data_loaded = True
except Exception as e:
    st.error(f"Error loading data: {e}")
    data_loaded = False

# --- 2. SIDEBAR (Project Info) ---
with st.sidebar:
    st.header("🇪🇬 About")
    st.write("This AI system matches the **emotional vibe** of a movie to real places in Egypt.")
    st.markdown("---")
    st.write("**Technologies:**")
    st.code("Python\nStreamlit\nBERT Embeddings\nCosine Similarity")
    st.markdown("---")
    st.write("Created for Academic Project")

# --- 3. MAIN INTERFACE ---
st.title("🎬 Egypt by Movie Vibe")
st.subheader("Watch a movie, live the feeling in Egypt.")

if data_loaded:
    # --- USER INPUT ---
    # We use a selectbox so the user can't type a movie we don't have
    movie_list = movies_df['title'].tolist()
    selected_movie_name = st.selectbox("👇 Select a movie you love:", movie_list)

    if st.button("Find My Egypt Vibe 🚀"):
        
        # A. Find the Movie Index
        movie_idx = movies_df[movies_df['title'] == selected_movie_name].index[0]
        
        # B. Get the Vibe Vector
        selected_vibe = movie_vibes[movie_idx].reshape(1, -1)
        
        # C. Compare with ALL Places (The AI Part)
        similarities = cosine_similarity(selected_vibe, place_vibes)[0]
        
        # D. Get Top 5 Recommendations
        # We sort the scores and get the top 5 indices
        top_indices = similarities.argsort()[-5:][::-1]
        
        st.markdown("### 🌍 We recommend you visit:")
        
        # E. Display Results
        for i, idx in enumerate(top_indices):
            place = places_df.iloc[idx]
            score = similarities[idx]
            
            # Create a nice card layout
            with st.container():
                st.markdown("---")
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"## {i+1}. {place['place_name']}")
                    st.markdown(f"**📍 City:** {place['city']} | **Category:** {place['category']}")
                    st.write(f"_{place['description']}_")
                    
                    st.markdown(f"**🏨 Where to Stay:** `{place['hotels']}`")
                    st.markdown(f"**🎯 Best Activities:** `{place['top_activities']}`")
                
                with col2:
                    st.metric(label="Vibe Match", value=f"{int(score*100)}%")
                    # Small Map for this specific location
                    map_data = pd.DataFrame({
                        'lat': [place['latitude']],
                        'lon': [place['longitude']]
                    })
                    st.map(map_data, zoom=10, size=200)

else:
    st.warning("Please ensure you have generated the data files in Step 4 and 5.")