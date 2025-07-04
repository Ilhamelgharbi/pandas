import pandas as pd
import numpy as np

df = pd.DataFrame({
    'temp_value': [20, np.nan, 30, np.nan, 50],
})
#df_cleaned = df.fillna(df.mean())
dfc = df.fillna({
    'temp_value': df['temp_value'].mean()
})
print("Original DataFrame:")
print(df)
print("DataFrame after filling missing values:")
print(dfc)