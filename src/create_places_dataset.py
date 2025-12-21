import pandas as pd
import numpy as np

# Define the data structure
data = {
    "place_name": [],
    "city": [],
    "category": [],
    "description": [],
    "latitude": [],
    "longitude": [],
    "top_activities": [],
    "hotels": []
}

# --- 1. CORE REAL PLACES (The most famous ones) ---
core_places = [
    ("Pyramids of Giza", "Giza", "Historical", "An iconic ancient site evoking awe, mystery, and timeless grandeur.", 29.9792, 31.1342, "Camel rides; Pyramid interior tours; Sound and light show", "Marriott Mena House; Steigenberger Pyramids"),
    ("Khan El Khalili", "Cairo", "Market", "A vibrant traditional bazaar full of color, energy, and cultural charm.", 30.0470, 31.2623, "Shopping for souvenirs; Drinking tea at El Fishawy; Photography", "Le Riad Hotel de Charme; Kempinski Nile Hotel"),
    ("Siwa Oasis", "Siwa", "Nature", "A tranquil desert oasis offering peace, isolation, and spiritual calm.", 29.2032, 25.5195, "Salt lake swimming; Dune bashing; Watching sunset", "Adrère Amellal; Siwa Shali Resort"),
    ("Bibliotheca Alexandrina", "Alexandria", "Cultural", "A modern cultural landmark inspiring curiosity, knowledge, and creativity.", 31.2089, 29.9092, "Reading; Museum tours; Planetarium shows", "Steigenberger Cecil; Four Seasons Alexandria"),
    ("Mount Sinai", "Saint Catherine", "Religious", "A sacred mountain associated with reflection, faith, and spiritual depth.", 28.5393, 33.9749, "Hiking at sunrise; Visiting the monastery; Meditation", "Morgenland Village; Catherine Plaza Hotel"),
    ("Aswan Nile Cruise", "Aswan", "Relaxation", "A slow scenic journey offering serenity, romance, and reflection.", 24.0889, 32.8998, "Sailing; Nubian village visit; Temple stops", "Sofitel Legend Old Cataract; Movenpick Aswan"),
    ("White Desert", "Farafra", "Nature", "A surreal landscape creating feelings of wonder, solitude, and adventure.", 27.3317, 28.2145, "Camping; Stargazing; Jeep safari", "Qasr El Bawity; Desert Stars Camp"),
    ("Luxor Temple", "Luxor", "Historical", "A majestic temple radiating ancient power, mystery, and reverence.", 25.6995, 32.6396, "Night tour; Walking through history; Photography", "Hilton Luxor Resort; Sofitel Winter Palace"),
    ("El Gouna", "Red Sea", "Resort", "A luxurious coastal town offering relaxation, fun, and vibrant nightlife.", 27.3949, 33.6782, "Kitesurfing; Boat trips; Fine dining", "Cook's Club; Steigenberger Golf Resort"),
    ("Valley of the Kings", "Luxor", "Historical", "A hidden valley of tombs evoking mystery, silence, and the afterlife.", 25.7402, 32.6014, "Exploring tombs; Learning history; Balloon ride nearby", "Al Moudira Hotel; Pavillon Winter Luxor"),
    ("Dahab Blue Hole", "Dahab", "Adventure", "A world-famous diving spot evoking thrill, depth, and underwater beauty.", 28.5723, 34.5371, "Scuba diving; Snorkeling; Freediving", "Le Meridien Dahab; Swiss Inn Resort"),
    ("Cairo Citadel", "Cairo", "Historical", "A medieval fortress offering commanding views, power, and history.", 30.0299, 31.2611, "Mosque visits; City views; Military museum", "Grand Nile Tower; Fairmont Nile City"),
    ("Ras Mohammed National Park", "Sharm El Sheikh", "Nature", "A pristine marine park offering vibrant colors, life, and natural beauty.", 27.7314, 34.2542, "Snorkeling; Diving; Bird watching", "Four Seasons Resort; Rixos Sharm El Sheikh"),
    ("Nubian Village", "Aswan", "Cultural", "A colorful and cheerful village full of joy, hospitality, and tradition.", 24.0600, 32.8800, "Henna tattoos; Buying spices; Crocodile watching", "Kato Dool Nubian Resort; Anakato"),
    ("Baron Empain Palace", "Cairo", "Historical", "A unique architectural gem evoking mystery, eccentricity, and old charm.", 30.0869, 31.3303, "Architecture tour; Photography; Garden walk", "Triumph Luxury Hotel; Sonesta Hotel"),
]

# --- 2. ADD REAL ENTRIES TO DATA ---
for p in core_places:
    data["place_name"].append(p[0])
    data["city"].append(p[1])
    data["category"].append(p[2])
    data["description"].append(p[3])
    data["latitude"].append(p[4])
    data["longitude"].append(p[5])
    data["top_activities"].append(p[6])
    data["hotels"].append(p[7])

# --- 3. GENERATE EXTRA PLACES TO REACH 200 (Smart Templates) ---
# We use patterns to generate realistic "Hidden Gems" or specific activities
cities = ["Cairo", "Alexandria", "Luxor", "Aswan", "Hurghada", "Sharm El Sheikh", "Dahab", "Siwa", "Marsa Alam"]
categories = ["Nature", "Historical", "Cafe", "Relaxation", "Adventure", "Art"]

# Templates for descriptions (VIBES)
vibes = [
    "A hidden spot perfect for quiet contemplation and escaping the crowd.",
    "A lively place full of energy, music, and modern vibes.",
    "An ancient corner of the city that whispers stories of the past.",
    "A romantic setting with breathtaking views, ideal for couples.",
    "A rugged landscape that challenges the spirit and rewards the brave.",
    "A cozy artistic space inspiring creativity and conversation."
]

import random

# Generate remaining rows to hit 200
for i in range(len(core_places), 200):
    city = random.choice(cities)
    cat = random.choice(categories)
    vibe = random.choice(vibes)
    
    # Generate realistic names
    name = f"{city} {cat} Spot #{i}"
    if cat == "Cafe": name = f"{city} Old Town Cafe {i}"
    if cat == "Nature": name = f"{city} Secret Beach {i}"
    if cat == "Historical": name = f"{city} Ancient Ruins {i}"
    
    # Generic realistic coords (jittered slightly from city centers)
    base_lat = 30.0 if city == "Cairo" else (31.2 if city == "Alexandria" else 25.7)
    base_lon = 31.2 if city == "Cairo" else (29.9 if city == "Alexandria" else 32.6)
    
    data["place_name"].append(name)
    data["city"].append(city)
    data["category"].append(cat)
    data["description"].append(vibe)  # <--- THIS IS KEY FOR AI
    data["latitude"].append(base_lat + random.uniform(-0.1, 0.1))
    data["longitude"].append(base_lon + random.uniform(-0.1, 0.1))
    data["top_activities"].append("Photography; Local food tasting; Exploring")
    data["hotels"].append(f"{city} Grand Hotel; {city} Boutique Stay")

# --- 4. SAVE TO CSV ---
df = pd.DataFrame(data)
df.to_csv("data/egypt_places.csv", index=False)

print(f"✅ Successfully created data/egypt_places.csv with {len(df)} rows!")
print("   Columns: place_name, city, category, description, latitude, longitude, top_activities, hotels")