import qrcode
import turtle

from googletrans import Translator
translator = Translator()

font = "Helvetica Now Display"

item_ch = input("item name: ")
wdf = input("wet, dry or fresh?: ")
price = input("price: ")
kgpic = input("per kg or per piece?: ")

# Translation
item_en_alldata = translator.translate(item_ch, dest='en')
item_en = item_en_alldata.text

price_tag = turtle.Screen()
turtle = turtle.Turtle()
price_tag.setup(800, 400)

turtle.hideturtle()
turtle.penup()
turtle.speed(0)


if wdf == "wet":
    turtle.goto(-160, -155)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(65,steps=62)

    turtle.end_fill()

elif wdf == "dry":
    turtle.goto(-205, -155)
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(130)
        turtle.left(90)
    turtle.end_fill()

elif wdf == "fresh":
    turtle.goto(-205, -155)
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(145)
        turtle.right(-120)
    turtle.end_fill()

# English Name
turtle.goto(-365, 80)
turtle.write(str.upper(item_en), align="left", font=(font, 70, "bold"))

# Chinese Name
turtle.goto(-365, 0)
turtle.write(item_ch, align="left", font=(font, 70, "bold"))

# Price
turtle.goto(365, -55)
turtle.write(price, align="right", font=(font, 200, "bold"))

if kgpic == "piece":
    turtle.goto(365, -65)
    turtle.write("HKD", align="right", font=(font, 50, "bold"))
    turtle.goto(365, -115)
    turtle.write("/ PIECE", align="right", font=(font, 50, "bold"))
    turtle.goto(365, -165)
    turtle.write("一件", align="right", font=(font, 50, "bold"))
elif kgpic == "kg":
    turtle.goto(365, -65)
    turtle.write("HKD", align="right", font=(font, 50, "bold"))
    turtle.goto(365, -115)
    turtle.write("/ 1KG", align="right", font=(font, 50, "bold"))


# QR Code
qr = qrcode.QRCode(box_size = 6, border = 1)
qr.add_data(item_en+" recipe")
qr.make(fit=True)
img = qr.make_image()
img.save('item_qr.gif')

turtle.goto(-300, -90)
price_tag.addshape('item_qr.gif')
turtle.shape('item_qr.gif')
turtle.stamp()

# turtle.getscreen().getcanvas().postscript(file='outputname.ps')

price_tag.mainloop()
