import pandas as pd
import csv

df = pd.read_csv('./csv/129.csv')

del df['Luminosity']

print(df.shape)

df = df[df['Star_name'].notna()]
df = df[df['Distance'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]


print(list(df))

df.to_csv('./csv/final_data.csv')
