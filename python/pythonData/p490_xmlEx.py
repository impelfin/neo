from xml.etree.ElementTree import parse

tree = parse('xmlEx_03.xml')
myroot = tree.getroot()
print(type(myroot))
print(myroot)
print('-' * 50)

familys = myroot.findall('가족')
print(type(familys))
print(familys)
print('-' * 50)

for onefamily in familys:
    for onesaram in onefamily:
        if len(onesaram) >= 1:
            print(onesaram[0].text)
        else:
            print(onesaram.attrib['이름'])
    print('-' * 50)
print('finished')
