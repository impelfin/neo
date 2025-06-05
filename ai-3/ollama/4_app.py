from pykrx import stock
from datetime import datetime
import matplotlib.pyplot as plt

end_date = datetime.today()
end_date = end_date.strftime('%Y%m%d')
start_date = '20250501'

df_ss = stock.get_market_ohlcv(start_date, end_date, '005930')
dates_ss = df_ss.index

fig, ax1 = plt.subplots(2, 1, figsize=(14, 10))

ax1[0].plot(dates_ss, df_ss['시가'], color='green', label='시가')
ax1[0].plot(dates_ss, df_ss['종가'], color='red', label='종가')
ax1[0].set_xlabel('Date')
ax1[0].set_ylabel('Price')
ax1[0].set_title(stock.get_market_ticker_name('005930') + " 주가")
ax1[0].legend()
ax1[0].grid()

ax1[1].bar(dates_ss, df_ss['거래량'], color='blue', alpha=0.5, label='거래량')
ax1[1].set_xlabel('Date')
ax1[1].set_ylabel('Volume')
ax1[1].set_title(stock.get_market_ticker_name('005930') + " 거래량")
ax1[1].legend()
ax1[1].grid()

plt.tight_layout()
plt.show()
