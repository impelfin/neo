mystring = "lift is egg"
mylist = mystring.split()
print(mylist)

for idx in range(len(mylist)):
    if idx % 2 == 0:
        mylist[idx] = mylist[idx].upper()
    else:
        mylist[idx] = mylist[idx].lower()

print(mylist)

result = '#'.join(mylist)
print('result : ', result)
print('result : ', result.replace('#',':'))

result = ' '.join(mylist)
print('result : ', result)
