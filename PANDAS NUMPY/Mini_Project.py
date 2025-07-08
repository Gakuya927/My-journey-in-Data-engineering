import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")
df=pd.read_csv("time_series_covid19_confirmed_global.csv")
df_clean=df.drop(columns=["Lat","Long","Province/State"]) #removing null values
country_df=df_clean.groupby("Country/Region").sum()#grouping by country/region
latest_date = country_df.columns[-1]
top10 = country_df.sort_values(by=latest_date, ascending=False).head(10)
print(top10[latest_date])
daily_new_cases = country_df.diff(axis=1)

# Example: India's daily new cases
india_daily = daily_new_cases.loc["India"]
print(india_daily.tail())
peak_day = india_daily.idxmax()
peak_value = india_daily.max()

print(f"India's peak daily cases were {int(peak_value)} on {peak_day}")

# Global totals for latest day
world_total = country_df[latest_date].sum()
world_new = daily_new_cases[latest_date].sum()

print(f" Global confirmed cases as of {latest_date}: {int(world_total):,}")
print(f" New confirmed cases on {latest_date}: {int(world_new):,}")
import numpy as np
import matplotlib.pyplot as plt

# Get India's daily new cases
india_daily = country_df.loc["India"].diff().fillna(0)
india_daily[india_daily < 0] = 0  # Clean any negative values

# Convert to NumPy array
india_array = np.array(india_daily)

# Apply simple moving average for smoothing
window = 7
smoothed = np.convolve(india_array, np.ones(window)/window, mode='valid')

# Plot
plt.figure(figsize=(14, 5))
plt.plot(india_daily.index[window-1:], smoothed, label="7-day Moving Average")
plt.title("India - Smoothed Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
us_daily = country_df.loc["US"].diff().fillna(0)
us_daily[us_daily < 0] = 0

# Convert to NumPy for smoothing
india_smooth = np.convolve(india_daily, np.ones(window)/window, mode='valid')
us_smooth = np.convolve(us_daily, np.ones(window)/window, mode='valid')

# Align dates
date_range = india_daily.index[window-1:]
sns.histplot(india_daily, bins=50, kde=True)
plt.title("India – Daily New Cases Distribution")
plt.xlabel("New Cases per Day")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
