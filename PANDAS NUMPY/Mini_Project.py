import pandas as pd
import numpy as np
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
