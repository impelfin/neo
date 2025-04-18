from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get('/')
async def HealthCheck():
    return {'status': 'ok'}

@app.get('/getcsv')
async def GetCsv():
    csv_file = 'data.csv'

    df = pd.read_csv(csv_file)
    dict_data = df.to_dict()
    print(dict_data)
    return dict_data
        
