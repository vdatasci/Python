import glob
for file in glob.glob("C:\*.*"):
    print file


files = glob.iglob("*.*")
files
# <generator object at 0x777u1>
files.next()
# 'default.jpg'
files.next()
# 'my_generated_image.png'


for name in glob.glob('dir/*[0-9].*'):
    print name
# dir/file1.txt
# dir/file2.txt


import glob2

glob2.glob('F:\Python\**\*.py')




print '\n'.join([str(x) for x in fuzzfind.fuzzyfinder('map', glob2.glob('F:\Python\**\*.py'))])

