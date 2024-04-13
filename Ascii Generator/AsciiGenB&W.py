from PIL import Image, ImageDraw, ImageFont
import math

#characters = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
#characters = "%#Wo- "[::-1]
characters = "%#Wovux()-,\"' "[::-1]
charArray = list(characters)
charLength = len(charArray)
interval = charLength/256

ScaleFactor = 0.3

oneCharWidth = 8
oneCharHeight = 18

def getChar(inputInt):   #H can be from 0 to 255
    return charArray[math.floor(inputInt*interval)]

text_file = open("Output.txt","w") #Write mode

im = Image.open(r"C:\Users\Manu\Documents\Miscellaneous\Ascii Generator\car2.jpg")

fnt = ImageFont.truetype(r"C:\Users\Manu\Documents\Miscellaneous\Ascii Generator\lucon.ttf",15)

width, height = im.size
im = im.resize((int(ScaleFactor * width),int(ScaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB',(oneCharWidth * width, oneCharHeight * height), color = (0,0,0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j,i]
        h = int((r + g + b)/3)  # Colors can only be integers
        pix[j,i] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j*oneCharWidth, i*oneCharHeight),getChar(h), font = fnt)
    
    text_file.write("\n")


outputImage.save("outputB&W.png")
