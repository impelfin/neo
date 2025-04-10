import os

myfolder = './'
newpath = os.path.join(myfolder, 'work')

try:
    os.rmdir(path=newpath)
    for idx in range(1, 11):
        newfile = os.path.join(myfolder, 'somefolder' + str(idx).zfill(2))
        os.rmdir(path=newfile)
except FileNotFoundError:
    print("Directory not found")
finally:
    print("Done~!!")