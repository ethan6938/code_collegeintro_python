import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime

def read_weather_data(filename):
    """Reads weather data from a CSV file and extracts dates, precipitation, and temperature information."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        # Automatically find indexes for PRCP, TMIN, and TMAX columns
        date_idx = header_row.index("DATE")
        prcp_idx = header_row.index("PRCP") if "PRCP" in header_row else None
        tmin_idx = header_row.index("TMIN")
        tmax_idx = header_row.index("TMAX")
        name_idx = header_row.index("NAME") if "NAME" in header_row else None
        
        # Extract data
        dates, prcp, tmin, tmax, station_name = [], [], [], [], ""
        for row in reader:
            try:
                current_date = datetime.strptime(row[date_idx], "%Y-%m-%d")
                prcp_value = float(row[prcp_idx]) if prcp_idx is not None and row[prcp_idx] else 0
                tmin_value = float(row[tmin_idx])
                tmax_value = float(row[tmax_idx])

                dates.append(current_date)
                prcp.append(prcp_value)
                tmin.append(tmin_value)
                tmax.append(tmax_value)
                if name_idx is not None:
                    station_name = row[name_idx]
            except ValueError:
                print(f"Skipping row: {row}")  # Debugging line to find errors
                continue
        
    min_length = min(len(dates), len(prcp))
    dates = dates[:min_length]
    prcp = prcp[:min_length]
    
    return dates, prcp, tmin, tmax, station_name

def plot_rainfall(dates, prcp, title):
    """Plots daily rainfall amounts."""
    print(f"Dates length: {len(dates)}, PRCP length: {len(prcp)}")  # Debugging
    plt.figure(figsize=(10, 5))
    plt.bar(dates, prcp, color='blue', alpha=0.6)
    plt.xlabel("Date")
    plt.ylabel("Precipitation (inches)")
    plt.title(f"Daily Rainfall - {title}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_temperature_comparison(dates, tmin, tmax, title):
    """Plots temperature range over time."""
    plt.figure(figsize=(10, 5))
    plt.plot(dates, tmax, label='High Temp', color='red', alpha=0.6)
    plt.plot(dates, tmin, label='Low Temp', color='blue', alpha=0.6)
    plt.fill_between(dates, tmin, tmax, color='gray', alpha=0.3)
    plt.xlabel("Date")
    plt.ylabel("Temperature (°F)")
    plt.title(f"Temperature Variation - {title}")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Load data for Sitka and Death Valley
sitka_dates, sitka_prcp, sitka_tmin, sitka_tmax, sitka_title = read_weather_data("sitka_weather_2021_full.csv")
dv_dates, dv_prcp, dv_tmin, dv_tmax, dv_title = read_weather_data("death_valley_2021_full.csv")

# Plot Sitka Rainfall
plot_rainfall(sitka_dates, sitka_prcp, sitka_title)

# Plot temperature comparisons with the same y-axis limits
plt.figure(figsize=(10, 5))
plt.plot(sitka_dates, sitka_tmax, label='Sitka High Temp', color='red', alpha=0.6)
plt.plot(sitka_dates, sitka_tmin, label='Sitka Low Temp', color='blue', alpha=0.6)
plt.plot(dv_dates, dv_tmax, label='Death Valley High Temp', color='darkred', alpha=0.6)
plt.plot(dv_dates, dv_tmin, label='Death Valley Low Temp', color='darkblue', alpha=0.6)
plt.fill_between(sitka_dates, sitka_tmin, sitka_tmax, color='gray', alpha=0.3)
plt.fill_between(dv_dates, dv_tmin, dv_tmax, color='black', alpha=0.1)
plt.xlabel("Date")
plt.ylabel("Temperature (°F)")
plt.title("Temperature Comparison: Sitka vs Death Valley")
plt.legend()
plt.xticks(rotation=45)
plt.ylim(0, 120)  # Same y-axis range for fair comparison
plt.tight_layout()
plt.show()

# San Francisco data (optional, requires downloading CSV)
# sf_dates, sf_prcp, sf_tmin, sf_tmax, sf_title = read_weather_data("san_francisco_weather_2021_full.csv")
# plot_temperature_comparison(sf_dates, sf_tmin, sf_tmax, sf_title)