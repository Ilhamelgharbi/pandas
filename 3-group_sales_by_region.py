import pandas as pd
import numpy as np
df = pd.DataFrame({
    'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'sales': [1500, 2000, 1800, 2200, 1600, 2100, 1900, 2300]
})
total_df = df.groupby('region')['sales'].sum()
print("Ventes totales par région :")
print(total_df)