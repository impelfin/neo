from itertools import count

for page_idx in count():
    if page_idx >= 5:
        break
    print(page_idx)
print('finished')