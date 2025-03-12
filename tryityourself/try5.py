import folium
import pandas as pd
import requests
import os
import json  # Import json to load GeoJSON

# --- Step 1: Download Recent Earthquake Data ---
earthquake_file = 'earthquakes.geojson'

# If the GeoJSON file for recent earthquakes does not exist, download it
if not os.path.exists(earthquake_file):
    print("Earthquake data file not found, downloading...")
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"  # 1-day dataset
    response = requests.get(url)

    # Save the downloaded data into the 'earthquakes.geojson' file
    with open(earthquake_file, 'wb') as f:
        f.write(response.content)
    print("Earthquake data downloaded successfully.")
else:
    print("Earthquake data file found.")

# --- Step 2: Load Earthquake Data ---
# Load the GeoJSON file for Earthquakes
with open(earthquake_file, 'r') as f:
    data = json.load(f)  # Use json.load() to load the GeoJSON content

# --- Step 3: Visualizing Recent Earthquakes ---
# Create a base map for earthquakes
m_earthquakes = folium.Map(location=[20, 0], zoom_start=2)

# Plot earthquakes on the map
for feature in data['features']:
    coords = feature['geometry']['coordinates']
    mag = feature['properties']['mag']
    folium.CircleMarker(
        location=[coords[1], coords[0]],
        radius=mag * 2,  # Make circle size proportional to magnitude
        color='red',
        fill=True,
        fill_color='red'
    ).add_to(m_earthquakes)

# Save the earthquake map as an HTML file
m_earthquakes.save("recent_earthquakes_map.html")
print("Earthquake map saved as 'recent_earthquakes_map.html'.")

# --- Step 4: Download Active Fire Data ---
fire_file = 'world_fires_1_day.csv'

# Check if the fire data file exists
if not os.path.exists(fire_file):
    print("Fire data CSV file not found. Please make sure 'world_fires_1_day.csv' is available.")
else:
    fire_data = pd.read_csv(fire_file)

    # Create a base map for fires
    m_fires = folium.Map(location=[20, 0], zoom_start=2)

    # Plot fire locations on the map
    for _, row in fire_data.iterrows():
        lat, lon, brightness = row['latitude'], row['longitude'], row['brightness']
        folium.CircleMarker(
            location=[lat, lon],
            radius=5,
            color='orange',
            fill=True,
            fill_color='orange',
            fill_opacity=0.7,
            popup=f"Brightness: {brightness}"
        ).add_to(m_fires)

    # Save the fire map as an HTML file
    m_fires.save("world_fires_map.html")
    print("Fire map saved as 'world_fires_map.html'.")
