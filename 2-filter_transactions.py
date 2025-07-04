import pandas as pd
import numpy as np
finance_df = pd.DataFrame({
   'id_transaction': [1, 2, 3, 4],
    'montant': [500, 1500, 300, 2000]
})
dt_filtered = finance_df[finance_df['montant'] > 1000]
print(f"DataFrame after filtering transactions with amount > 1000: \n{dt_filtered}\n")