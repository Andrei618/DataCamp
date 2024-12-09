import os
import pandas as pd

print("Current working directory:", os.getcwd())

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'airlines_final.csv'))
print(df.head())
