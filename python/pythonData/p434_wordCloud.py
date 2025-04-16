import matplotlib.pyplot as plt
from wordcloud import WordCloud

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'steve.txt'
myfile = open(filename, mode='r', encoding='utf-8')

text = myfile.read()

wordcloud = WordCloud()
wordcloud = wordcloud.generate(text)
print(type(wordcloud))
print('-' * 50)

bindo = wordcloud.words_
print(type(bindo))
print('-' * 50)

sortedData = sorted(bindo.items(), key=lambda x: x[1], reverse=True)
print(sortedData)
print('-' * 50)

charData = sortedData[:10]
print(charData)
print('-' * 50)

xtick = []
chart = []

for item in charData:
    xtick.append(item[0])
    chart.append(item[1])

mycolor = ['r', 'g', 'b', 'c', 'm', 'y', '#fff0f0', '#f0fff0', '#f0f0ff', '#f0ffff']
plt.bar(xtick, chart, color=mycolor)
plt.title('상위 빈도 TOP 10')

filename = 'p434_wordCloud01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')

plt.figure(figsize=(12, 12))
plt.imshow(wordcloud)
plt.axis('off')

filename = 'p434_wordCloud02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()