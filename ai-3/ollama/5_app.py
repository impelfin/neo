from pykrx import stock
from openai import OpenAI
from datetime import datetime
import json

llama_client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama'
)

def llama_trading(start_date, end_date, ticker):
    df = stock.get_market_ohlcv(start_date, end_date, ticker)

    df_summary = df[['종가']].tail(30).copy()
    df_summary['MA5'] = df_summary['종가'].rolling(window=5).mean()
    df_summary['MA5=20'] = df_summary['종가'].rolling(window=20).mean()
    
    df_summary = df_summary.reset_index()
    df_summary['날짜'] = df_summary['날짜'].dt.strftime('%Y-%m-%d')
    data_json = df_summary.to_dict(orient='records')

    response = llama_client.chat.completions.create(
        model='llama3.2:latest',
        messages = [
            {
                'role': 'system', 
                'content': [
                    {
                        "type" : "text",
                        "text" : """
당신은 주식 매매 전문가입니다. 아래에 제공된 차트 데이터를 분석하여 현재 시점에서 '매수', '매도', '관망' 중 하나를 선택하고 이유를 설명하세요.
결과는 반드시 다음 JSON 형식으로 출력해야 합니다. 이외의 텍스는 금지입니다.

예시:
{"decision" : "매수", "reason" : "이동평균선이 상승세로 전환되고 있으며 거래량이 증가하고 있습니다. "}
{"decision" : "매도", "reason" : "주가가 과열 구간에 진입했고 차익실현 매물이 나올 가능성이 있습니다. "}
{"decision" : "관망", "reason" : "명확한 추세가 없고 방향성이 불확실합니다. "}
"""
                    }
                ]
            },
            {
                'role': 'user', 
                'content': [
                    {
                        "type" : "text",
                        "text" : json.dumps(data_json, ensure_ascii=False)
                    }   
                ]
                
            }
        ]
    )

    try:
        result = response.choices[0].message.content
        result = json.loads(result)
        print('----- 결정 : ', result['decision'].upper(), '-----')
        print('📌 사유 : ', result['reason'])
    except Exception as e:
        print('❌ 응답 파싱 중 오류 : ', e)
        print('원본 응답 : ', response.choices[0].message.content)

def main():
    end_date = datetime.today().strftime('%Y%m%d')
    start_date = '20250501'
    ticker = '005930'

    llama_trading(start_date, end_date, ticker)

if __name__ == '__main__':
    main()
