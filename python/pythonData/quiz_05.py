import pandas as pd

filename = 'NewChickenResult.csv'

df = pd.read_csv(filename, encoding='utf-8')

df = df[~df['sido'].astype(str).str.isnumeric()]
df = df[~df['sido'].astype(str).str.contains('테스트')]

df['sido'] = df['sido'].replace({'서울특별시' : "서울"})
df['sido'] = df['sido'].replace({'부산광역시' : "부산"})
df['sido'] = df['sido'].replace({'인천광역시' : "인천"})
df['sido'] = df['sido'].replace({'대전광역시' : "대전"})
df['sido'] = df['sido'].replace({'대구광역시' : "대구"})
df['sido'] = df['sido'].replace({'광주광역시' : "광주"})
df['sido'] = df['sido'].replace({'울산광역시' : "울산"})
df['sido'] = df['sido'].replace({'제주특별자치도' : "제주"})
df['sido'] = df['sido'].replace({'세종특별자치시' : "세종"})
df['sido'] = df['sido'].replace({'강원도' : "강원"})
df['sido'] = df['sido'].replace({'경기도' : "경기"})
df['sido'] = df['sido'].replace({'경상남도' : "경남"})
df['sido'] = df['sido'].replace({'경상북도' : "경북"})
df['sido'] = df['sido'].replace({'전라남도' : "전남"})
df['sido'] = df['sido'].replace({'전라북도' : "전북"})
df['sido'] = df['sido'].replace({'충청남도' : "충남"})
df['sido'] = df['sido'].replace({'충청북도' : "층북"})

result = df.groupby(['sido', 'brand']).size().reset_index(name='count')
print(result)

result.to_csv('xx_chicken.csv', encoding='utf-8', index=False)
print("\nFile Saved..")