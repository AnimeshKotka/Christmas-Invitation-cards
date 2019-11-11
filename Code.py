from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('Lato-Black.ttf', size=40)
message = "Happy Birthday!"
color = 'rgb(255, 255, 51)'

i = 1
while i < 357:
    image = Image.open('ChristmasParty.jpg')
    draw = ImageDraw.Draw(image)
    draw.text((360, 850), "E-Pass:"+str(3000+i), fill=color, font=font)
    image.save("C:/Users/HP/PycharmProjects/PreChristMasFinal/Cards_Invitation/"+"card"+str(i)+".png")

    i=i+1

# save the edited image

