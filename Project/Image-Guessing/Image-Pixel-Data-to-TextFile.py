from PIL import Image
im=Image.open("P:\city.png")
fil = open("P:\TempFile.txt", "w")
pixel = im.load()
row,column=im.size
for y in range(column):
    for x in range(row):
            pixel=pix[x,y]
            fil.write(str(pixel)+'\n')

