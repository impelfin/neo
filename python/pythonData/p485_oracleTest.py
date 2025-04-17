import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series

cx_Oracle.init_oracle_client(lib_dir="/usr/local/OracleXE/instantclient_19_26")

plt.rcParams['font.family'] = 'NanumBarunGothic'

conn = None
cur = None

try:
    loginfo = 'hr/1234@192.168.1.111:1521/xe'
    conn = cx_Oracle.connect(loginfo)
    cur = conn.cursor()

    sql = 'select * from three_country'
    cur.execute(sql)

    name = []
    year = []
    bindo = []

    for result in cur:
        name.append(result[0])
        year.append(result[1])
        bindo.append(result[2])

    myseries = Series(bindo, index=[name, year])
    print(myseries) 

    for idx in range(0, 2):
        myframe = myseries.unstack(idx)
        print(myframe)
        
        myframe.plot(kind='barh', rot=0)
        plt.title('3개국 테러 발생 현황')
        plt.xlabel('년도')
        plt.ylabel('발생건수')
        
        filename = 'p485_oracleChart' + str(idx + 1) + '.png'
        plt.savefig(filename, dpi=400, bbox_inches='tight')
        print(filename + ' file saved...')
        plt.show()

except Exception as err:
    print(err)

finally:
    if cur != None:
        cur.close()

    if conn != None:
        conn.close()

print("finished...")