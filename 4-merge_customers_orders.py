import pandas as pd
import numpy as np
clients_df = pd.DataFrame({
    'id_client': [1, 2, 3, 4],
    'nom': ['Alice', 'Bob', 'Charlie', 'David']
})
commandes_df = pd.DataFrame({
    'id_commande': [101, 102, 103, 104],
    'id_client': [1, 2, 2, 4],
    'montant': [250, 150, 200, 300]
})

merged_df = pd.merge(clients_df, commandes_df, on='id_client', how='inner')
print("Tableau fusionné des clients et des commandes :")
print(merged_df)