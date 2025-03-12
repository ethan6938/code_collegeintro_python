from pathlib import Path
import csv
from matplotlib import pyplot as plt
from datetime import datetime

plt.style.use('seaborn-v0_8')

path = Path('sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
dates,highs,lows = [],[],[]
fig, ax = plt.subplots()

for index, column_header in enumerate(header_row):
    print(index, column_header)

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    single_high = int(row[4])
    single_lows = int(row[5])
    dates.append(current_date)
    highs.append(single_high)
    lows.append(single_lows)

print(highs)

ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)

ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.show()