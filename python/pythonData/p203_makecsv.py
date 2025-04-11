import random
import pandas as pd

result = []
myColumns = ['번호', '이름', '나이']
myencoding = 'utf-8'

for idx in range(1, 3):
    sublist = []
    sublist.append(100 * idx)
    sublist.append('김철수' + str(idx))
    sublist.append((random.randint(1, 10)))
    result.append(sublist)

myframe = pd.DataFrame(result, columns=myColumns)

filename = 'csv_01.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=True)

filename = 'csv_02.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False)

filename = 'csv_03.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False, header=False)

filename = 'csv_04.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False, sep='%')

for _ in range(1, 5):
    print(f'csv_0{_}.csv 파일 저장 완료~!!')

