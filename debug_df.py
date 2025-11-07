from time_series_visualizer import df

print("Max value:", df['value'].max())
print("95th percentile:", df['value'].quantile(0.975))
print("Min value:", df['value'].min())
print("2.5 percentile:", df['value'].quantile(0.025))
print("Total rows:", len(df))
