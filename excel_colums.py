import pandas as pd
import numpy as np
import math



df = pd.read_csv("test-Umut3.csv")

df = df.iloc[9:42]

df.filter(regex='^(?!NaN).+', axis=1)





df.drop(df.filter(regex="Unnamed: 8"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 9"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 10"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 11"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 12"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 13"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 14"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 15"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 16"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 17"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 18"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 19"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 20"),axis=1, inplace=True)
df.drop(df.filter(regex="Unnamed: 21"),axis=1, inplace=True)


df = df.replace(np.nan, 0)
print(df)

