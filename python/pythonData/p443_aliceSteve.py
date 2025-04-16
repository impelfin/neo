import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from wordcloud import ImageColorGenerator

image_file = 'alice.png'

img_file  = Image.open(image_file)
print(type(img_file))
print('-' * 50)

alice_mask = np.array(img_file)
print(type(alice_mask))
print('-' * 50)

filename = 'steve.txt'
myfile = open(filename, mode='r', encoding='utf-8')

plt.figure(figsize=(8, 8))
plt.imshow(alice_mask, interpolation='bilinear')
plt.axis('off')

filename = 'p434_alice_graph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')

mystopwords = set(STOPWORDS)
mystopwords.add('said')
mystopwords.update(['hohoho', 'hahaha'])

print(len(mystopwords))
print(mystopwords)

wc = WordCloud(background_color='white', mask=alice_mask, stopwords=mystopwords, max_words=2000)

stevefile = 'steve.txt'
text = open(stevefile, mode='r', encoding='utf-8').read()

wc.generate(text)
print(wc.words_)
print('-' * 50)

plt.figure(figsize=(12, 12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')

filename = 'p434_alice_graph02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')

alice_color_file = 'alice_color.png'
alice_color_mask = np.array(Image.open(alice_color_file))

wc = WordCloud(background_color='white', mask=alice_color_mask, stopwords=mystopwords, max_words=2000, max_font_size=40, random_state=42)
wc = wc.generate(text)

plt.figure(figsize=(12, 12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')

filename = 'p434_alice_graph03.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')

plt.figure(figsize=(12, 12))
plt.imshow(alice_color_mask, interpolation='bilinear')
plt.axis('off')

filename = 'p434_alice_graph04.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved') 

image_colors = ImageColorGenerator(alice_color_mask)

plt.figure(figsize=(12, 12))
newwc = wc.recolor(color_func=image_colors, random_state=42)
plt.imshow(newwc, interpolation='bilinear')
plt.axis('off')

filename = 'p434_alice_graph05.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()