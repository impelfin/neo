import pandas as pd

filename = 'seoul.csv'
df = pd.read_csv(filename, encoding='utf-8')
print(df)
print('-' * 50)

result = df.loc[df['시군구'].str.strip() == '서울특별시 강남구 신사동']
print('\n', result)

result = df.loc[(df['시군구'].str.strip() == '서울특별시 강남구 신사동') & (df['단지명'] == '삼지')]
print('\n', result)

newdf = df.set_index(keys=['도로명'])
print('\n', newdf)

result = newdf.loc['언주로']
print('\n', result)
count = len(newdf.loc['언주로'])
print('\ncount : ', count)