import pandas as pd

filename = 'memberInfo.csv'
df = pd.read_csv(filename, encoding='utf-8')
print(df)
print('-' * 50)

newdf01 = df.set_index(keys=['id'])
print(newdf01)
print('-' * 50)

newdf02 = df.set_index(keys=['id'], drop=False)
print(newdf02)
print('-' * 50)

df02 = pd.read_csv(filename, encoding='utf-8', index_col='id')
print(df02)
print('-' * 50)
