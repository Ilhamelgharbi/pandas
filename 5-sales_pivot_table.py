import pandas as pd

df = pd.DataFrame({
    'produit': ['A', 'D', 'B', 'E', 'C'],
    'region': ['Nord', 'Sud', 'Nord', 'Sud', 'Nord'],
    'ventes': [100, 200, 150, 250, 300]
})


tableau = pd.pivot_table(df, index='produit', columns='region', values='ventes', aggfunc='sum')

print("Tableau croisé dynamique :")
print(tableau)
