wordinfo = {'세탁기':50, '선풍기':30, '냉장고':60}
print(wordinfo)

myxticks = sorted(wordinfo, key=wordinfo.get, reverse=True)
print(myxticks)

reverse_key = sorted(wordinfo.keys(), reverse=True)
print(reverse_key)

chardata = sorted(wordinfo.values(), reverse=True)
print(chardata)