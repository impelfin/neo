import numpy as np
import pandas as pd
from pandas import Series

filename = 'excel02.csv'

print('\n # 누락된 데이터 샘플 데이터프레임')

myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8')
print(myframe)
print('-' * 50)

print('\n # fillna()')
print(myframe.fillna(0, inplace=False))

print('\n inplace=False 사용 시 원본 데이터 변동 없음')
print(myframe)
print('-' * 50)

print('\n inplace=True 사용 시 원본 데이터 변동 있음')
print(myframe.fillna(0, inplace=True))
print('-' * 50)
print(myframe)
print('-' * 50)

print('\n # 누락된 데이터 샘플 데이터프레임')
myframe.loc[['강감찬', '홍길동'], ['국어', '영어']] = np.nan
myframe.loc[['박영희', '김철수'], ['수학']] = np.nan
print(myframe)
print('-' * 50)

print('\n # 누락된 데이터 값 임의의 값으로 치환')
print('\n # 국어, 영어, 수학 Nan값을 일괄 변경')
mydict = {'국어': 15, '영어': 25, '수학': 35}
myframe.fillna(mydict, inplace=True)
print(myframe)
print('-' * 50)

myframe.loc[['박영희'], ['국어']] = np.nan
myframe.loc[['홍길동'], ['영어']] = np.nan
myframe.loc[['김철수'], ['수학']] = np.nan
print(myframe)  
print('-' * 50)

mydict = {
    '국어': np.ceil(myframe['국어'].mean()),
    '영어': np.ceil(myframe['영어'].mean()),
    '수학': np.ceil(myframe['수학'].mean())
}
myframe.fillna(mydict, inplace=True)
print(myframe)
print('-' * 50)
