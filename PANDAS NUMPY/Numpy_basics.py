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
