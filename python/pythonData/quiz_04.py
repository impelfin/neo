import pandas as pd

file1 = 'cheogajip.csv'
file2 = 'pelicana.csv'

df1 = pd.read_csv(file1, encoding='utf-8', index_col=0)
df2 = pd.read_csv(file2, encoding='utf-8', index_col=0)

result = pd.concat([df1, df2], ignore_index=True)
result.to_csv('NewChickenResult.csv', encoding='utf-8', index=True)

print(result, " file saved..!!")
