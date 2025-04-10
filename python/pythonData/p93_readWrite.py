myfile01 = open('sample.txt', 'rt', encoding='utf-8')
linelists = myfile01.readlines()
myfile01.close()
print(linelists)

myfile02 = open('result.txt', 'wt', encoding='utf-8')

total = 0
for one in linelists:
    score = int(one)
    total += score
    myfile02.write('total = ' + str(total) + ', value = ' + str(score) + '\n')
averate = total / len(linelists)

myfile02.write('총점 : ' + str(total) + '\t')
myfile02.write('평균 : ' + str(averate))
myfile02.close()
print("done~!!")

myfile03 = open('result.txt', 'rt', encoding='utf-8')
line = 1
while line:
    line = myfile03.readline()
    print(line)
myfile03.close()