from time import*
from random import*
from turtle import*

redcircle = Turtle()
circles = 0
redcircle.color('red')
redcircle.goto(0,0)
redcircle.shape('circle')
redcircle.circles = 1
def circlesbuy(y,x):
    t1.clear()
    redcircle.circles += 1 + up2.upg1 + up4.upg1 + up6.upg1


redcircle.onclick(circlesbuy)

evilcircle = Turtle()
circles = 0
evilcircle.color('maroon')
evilcircle.penup()
evilcircle.goto(-450,-250)
evilcircle.shape('circle')
evilcircle.circles = 1
def evilbuy(y,x):
    t1.clear()
    redcircle.circles -= 100


evilcircle.onclick(evilbuy)


goldcircle = Turtle()
goldcircle.speed(100)
goldcircle.color('gold')
goldcircle.penup()
goldcircle.goto(500,0)
goldcircle.shape('circle')
goldcircle.circles = 1
def goldbuy(y,x):
    t1.clear()
    redcircle.circles += randint(1,300)*randint(1,10+up5.upg1+up8.upg1) + up9.upg1


goldcircle.onclick(goldbuy)

def goldpos():
    if goldcircle.xcor() > 5000:
        goldcircle.goto(-5000,0)
    else:
        sleep(0)





up1 = Turtle()
up1.color('black')
up1.penup()
up1.goto(-400,140)
up1.shape('square')
up1.upg1 = 0
def up1buy(y,x):
    if redcircle.circles >= 100:
        redcircle.circles -= 100
        t4.clear()
        t1.clear()
        up1.upg1 += 1
    else:
        sleep(0)

up1.onclick(up1buy)

up2 = Turtle()
up2.color('black')
up2.penup()
up2.goto(-400,200)
up2.shape('square')
up2.upg1 = 0
def up2buy(y,x):
    if redcircle.circles >= 10:
        redcircle.circles -= 10
        t3.clear()
        t1.clear()
        up2.upg1 += 1
    else:
        sleep(0)


up2.onclick(up2buy)

up3 = Turtle()
up3.color('black')
up3.penup()
up3.goto(-400,20)
up3.shape('square')
up3.upg1 = 0
def up3buy(y,x):
    if redcircle.circles >= 1000:
        redcircle.circles -= 1000
        t6.clear()
        t1.clear()
        up3.upg1 += 10
    else:
        sleep(0)

up3.onclick(up3buy)

up4 = Turtle()
up4.color('black')
up4.penup()
up4.goto(-400,80)
up4.shape('square')
up4.upg1 = 0
def up4buy(y,x):
    if redcircle.circles >= 100:
        redcircle.circles -= 100
        t5.clear()
        t1.clear()
        up4.upg1 += 10
    else:
        sleep(0)

up4.onclick(up4buy)


up5 = Turtle()
up5.color('gold')
up5.penup()
up5.goto(150,200)
up5.shape('square')
up5.upg1 = 0
def up5buy(y,x):
    if redcircle.circles >= 5000:
        redcircle.circles -= 5000
        t7.clear()
        t1.clear()
        up5.upg1 += 100
    else:
        sleep(0)

up5.onclick(up5buy)
        
up6 = Turtle()
up6.color('red')
up6.penup()
up6.goto(150,140)
up6.shape('square')
up6.upg1 = 0
def up6buy(y,x):
    if redcircle.circles >= 10000:
        redcircle.circles -= 10000
        t8.clear()
        t1.clear()
        up6.upg1 += 1000
    else:
        sleep(0)


up6.onclick(up6buy)

up7 = Turtle()
up7.color('red')
up7.penup()
up7.goto(150,80)
up7.shape('square')
up7.upg1 = 0
def up7buy(y,x):
    if redcircle.circles >= 100000:
        redcircle.circles -= 100000
        t9.clear()
        t1.clear()
        up7.upg1 += 10000
    else:
        sleep(0)

up7.onclick(up7buy)

up8 = Turtle()
up8.color('gold')
up8.penup()
up8.goto(150,20)
up8.shape('square')
up8.upg1 = 0
def up8buy(y,x):
    if redcircle.circles >= 10000000:
        redcircle.circles -= 10000000
        t10.clear()
        t1.clear()
        up8.upg1 += 100000
    else:
        sleep(0)

up8.onclick(up8buy)

up9 = Turtle()
up9.color('purple')
up9.penup()
up9.goto(150,-40)
up9.shape('square')
up9.upg1 = 0
def up9buy(y,x):
    if redcircle.circles >= 1000000000:
        redcircle.circles -= 1000000000
        goldcircle.color('purple')
        t11.clear()
        up9.upg1 = 100000000000
    else:
        sleep(0)

up9.onclick(up9buy)


t2 = Turtle()
t2.speed(10)
t2.hideturtle()
t2.penup()
t2.goto(-100,220)
t2.write('circles=', font=('Arial',20,'normal'))
t2.goto(-400,220)
t2.write('Upgrades', font=('Arial',20,'normal'))
t2.goto(150,220)
t2.color('red')
t2.write('Upgrades deluxe', font=('Arial',20,'normal'))
t2.goto(-55,-40)
t2.color('black')
t2.write('Press Me', font=('Arial',20,'normal'))
t2.goto(-420,155)
t2.write('+1 click,cost:10', font=('Arial',20,'normal'))
t2.goto(-420,95)
t2.write('+1 autoclick,cost:100', font=('Arial',20,'normal'))
t2.goto(-420,35)
t2.write('+10 click,cost:100', font=('Arial',20,'normal'))
t2.goto(-420,-25)
t2.write('+10 autoclick,cost:1K', font=('Arial',20,'normal'))
t2.goto(130,155)
t2.write('increased golden circle,cost:5K', font=('Arial',15,'normal'))
t2.goto(130,95)
t2.write('+1K click,cost:10K', font=('Arial',20,'normal'))
t2.goto(130,35)
t2.write('+10K autoclick,cost:100K', font=('Arial',20,'normal'))
t2.goto(130,-25)
t2.color('red')
t2.write('super golden circle,cost:10M', font=('Arial',15,'normal'))
t2.goto(130,-85)
t2.color('purple')
t2.write('Purple circle,cost:1B', font=('Arial',15,'normal'))
t2.color('black')

t3 = Turtle()
t3.speed(10)
t3.hideturtle()
t3.penup()
t3.goto(-385,185)


t4 = Turtle()
t4.speed(10)
t4.hideturtle()
t4.penup()
t4.goto(-385,125)

t1 = Turtle()
t1.speed(10)
t1.hideturtle()
t1.penup()
t1.goto(0,220)

t5 = Turtle()
t5.speed(10)
t5.hideturtle()
t5.penup()
t5.goto(-385,65)

t6 = Turtle()
t6.speed(10)
t6.hideturtle()
t6.penup()
t6.goto(-385,5)

t7 = Turtle()
t7.speed(10)
t7.hideturtle()
t7.penup()
t7.goto(165,185)

t8 = Turtle()
t8.speed(10)
t8.hideturtle()
t8.penup()
t8.goto(165,125)

t9 = Turtle()
t9.speed(10)
t9.hideturtle()
t9.penup()
t9.goto(165,65)

t10 = Turtle()
t10.color('red')
t10.speed(10)
t10.hideturtle()
t10.penup()
t10.goto(165,5)

t11 = Turtle()
t11.color('purple')
t11.speed(10)
t11.hideturtle()
t11.penup()
t11.goto(165,-55)


while circles < 5000000000000 and circles > -50000:
    t1.clear()
    redcircle.circles += up1.upg1 + up3.upg1 + up7.upg1
    circles = redcircle.circles
    goldcircle.forward(100)
    goldpos()
    t1.write(circles, font=('Arial',20,'normal'))
    t4.write(up1.upg1, font=('Arial',20,'normal'))
    t3.write(up2.upg1, font=('Arial',20,'normal'))
    t6.write(up3.upg1, font=('Arial',20,'normal'))
    t5.write(up4.upg1, font=('Arial',20,'normal'))
    t7.write(up5.upg1, font=('Arial',20,'normal'))
    t8.write(up6.upg1, font=('Arial',20,'normal'))
    t9.write(up7.upg1, font=('Arial',20,'normal'))
    t10.write(up8.upg1, font=('Arial',20,'normal'))
    t11.write(up9.upg1, font=('Arial',20,'normal'))
    sleep(0.1)

t1.clear()
t2.clear()
t3.clear()
t4.clear()
t5.clear()
t6.clear()
t7.clear()
t8.clear()
t9.clear()
t10.clear()
t11.clear()
up1.hideturtle()
up2.hideturtle()
up3.hideturtle()
up4.hideturtle()
up5.hideturtle()
up6.hideturtle()
up7.hideturtle()
up8.hideturtle()
up9.hideturtle()
if circles > 1:
    evilcircle.hideturtle()
    redcircle.pensize(1000)
    redcircle.circle(90)
    t2.goto(-200,0)
    t2.write('YOU WIN',font=('Arial',70,'normal'))
    sleep(10)
else:
    redcircle.hideturtle()
    evilcircle.goto(0,0)
    t2.goto(-540,0)
    t2.write('W̶̡̡̡̢̨̧̢̢̢̡̧̨̨̧̧̧̨̧̘̠͇̼̼̠͔̪̗̻̭͎͕̭̟͍̠̥̤͎̖̬̣͙͍̲̞͕̩̥̺̙͖̻͇̞͎̘̲̦̥̟̬̟͕̝̲̘͇͉̼̦̯̻͖̳̲̮̯̲̟̪̤̩͎̳̞̻̪͙͉̲̺͚̦̰̮̲͇̬̺̩̲̟̙̲̘̹̙͎͎͚͈͉̩͚͖̺̗̯̜͍̟͈̠̝̹͓̱͎̳̗̺͔͎̺̳͔͉͍̠͕̭̻̟͎̪̬̣̻͗̇̂̿̈́͜͜͜ͅͅͅͅͅḦ̴̡̤̙̄̍͑̌̌̍͂̎͒͆̈́̽̅͑͒̄̈́̈̋̋̌̒̑̔͌́̚̕͝͠Á̸̧̧̢̛͕͇̦̘͔͇̝̙̳̠͓̹̝̣͙̜̻̳̺̮̻̣̞̠̬̘͙͓̼̼̪̫̹͚͍͍̫̥͖̉̀̿̄̍͋́̂̀́́͛̑͐͗̊͂̉̾̃͜͝͝͝ͅͅŢ̷̡̢̢̨̢̡̧̡̧̡̨̢̢̛̛̛̛̳̝͙͈̹͔͖͇̤̠̖̤͎͔̪̱̙̖̭̱̘̼͇͎̖̜̙̙̳̰̦̲̮̝̝̣̲̟̱͚̫̫̻̱̯͉̯͎̯̫̝̯͙͍̫̞̬̯͔͓̲̣̮͎̳̰͍̞̙̘̳̝͈̣̤͙̮͚͔̮̘̘̭͇̯͔̭͉͓̟̳̹͔̫̲̺̟͙͕̥̲̜͍͍̣͖̻̭͍̻̬̠̼̤̞̖̥̯̗̘̣͚̦̞̯̥̙̺̯̪̫̼̰̯͚̭͓͕̤̣̼͐̉͆̈́̆̾̏̓̽͒̈̏̊̈́͗̃̉́̃͛̽̇́̇͂͑͂̇̏̈́́̔́̋̌̓̈́͆̏̋͂̍̀̊͑̈̌̓̄̄̿̀̓͛̓̃͛̀̄̃̔̔͋͒̊̄͂̂̊̂̿̄̈́̎̇̎̊̀̈͌̀̽̃̆̀͐̈́͒̒͊̈̐̈́́͒͌̓̎̒͌́̄̑̄̑͛̎̐̆̅͆̈́̀͐̄̉̊͗̽̈́͆̈͑̆̊̀̋͂̃̔̈́̿̉̌́̂͌̀̚̕͘̚̕̚͘̕̚̚̚̕̚͘͜͜͜͜͝͝͝͝͝͠͝͠͝͝͠͝͝ͅͅͅ ̸̧̨̡̡̨̛̛̛̛̺̦͖̙̝̜̣̮͇̫̮͔̲̘̣̣̫̜̝͎͖̺̳̣͔̩͈̣̞̥̝̬̜͚̭̝̭͖̮͖̗̩̪̤̻̬̠͙͖̼̣͙̠̪͕͕̦̣̱̠̳͇̳̖̮̯͍̳̽̔̏́̌̃́̓̄̈̈̏͋̓̌̄̍̅̂̂̎͒́̓͒̐͊͊̾̊͌̾͊̂̒͊͆̑͆̈͌͋͆̋̄̓̓̑̌̽̈́͑͐͂̿̅̇̽́̅̽͋̐̀́̈́̈͋͆̓͂̏̍͘̕̕͘̚̕͜͜͜͜͝͝͝͠ͅH̶̨̨̧̨̨̡̧̨͍͚̯̙̬̰̗͍̦͎̲̳̬̬̹̗̟͉̯̘͇̻̱͉͕̬̲̠̼͔͈̥̟͖̙̙̟̗͖̥͙͉̭͓̙͍̟̙̟͇̘̘͇̺̙̤͉̙͈̠͎̟̺͔̗̻͇̩̞̝̠̣͔̤̦͕͎̘̦͉̩̟̗̱̼̘͓̯̫̗̥͉̠̰̟͎͍͎͓̘̙̘͉͖̥̲̭̹̖̼̰̻͙̯̻̎̋̈́̅͋͘͘͜͝ͅͅͅͅͅͅA̷̢̨̨̡̨̨̨̢̧̢̨̡̨̡̛̛̛̼̥̬̟̹̤̫͎̥͍͇̦̤̰̤̥̯̦̘̯̪͙̗̹̹̖̱͇̝̤̖͈̭̱̜̱̲͕͓̟͔̼͈̗͕̺͚̺͕̖̩̥̫͖̤͖̤͎̠̥̝̳̖̲̼̲̭̬̞͍̳̝̙͇̖͎̳͓̬̘̹̙̦̠̠̭͈̙̰̙͚͎̟̟̬̭͖͇͖͈̹͇͉͕͚͓̺̠̩̯̣̖̤̦͙͉͈̳͖̹̹̖̻͇̦͍̪͙̫̙̺͍̟̜̦̯̹̗̻̪̖̱̅͂͋̒̄͛̐̋̒̉̈͐͗̅̑̑̆̇́͐̒̆̾̇͌̾̾̊͌͗̏͂̎̊̑̈́̓̇̌́́̌̏̈̏͆́̀̆̂̓̿́̾̑̇͐̆̆͊̽͐͒͆͑̌̄͑͗̊̈́̇̈́̋̾̊͛͐̓̍̄̂͋͆̂͒͂̂̓͒͆̿͂̐͋̌̃́̅͌̃̈́́̀̄͂͗̌̄̑̌͌͂̾͑̍̊̇̀͂̋̇̒̿̃̾̆̿͐̈̀͊́̒̌̿̀̈̈́̒͆̀̑̚̚͘̚̕̚͘̚̚̕͜͜͜͜͝͝͠͠͝͠͝͠͝͝͠ͅͅͅͅͅV̷̧̡̛̛̰͇̖͙̮͓̱̩̮̺̞̟̹̘̠̤̩̜́̑͗̈̋͌̎̈́̾͒̓͑̊̓̊̍̈̃̈̽̋̊̃͋̈̂͗͐̀̄͗̍̈́̊̊͋̈͂̔̈́̈́͌̒̈́̎̎̾̂̉̍͒̚͜͝͝͠Ẹ̶̢̢̧̢̨̢̡̧̡̧̡̛̛̩̣̝̥͎͕̣͈͚̲̭̙͎̮͚̞͙̼̙̰̩̠̜̤̦̤̯̥̣̜̜̘͙̟̱̫͙͖͙̮͚͓̥̩̠̣̙̰̪͕̝̺̤̙̦͚̪̭̟̦͓̺̦͇̮̣̫̪̪̝̩̜̯̙̳̍̍̐̃̄̓̃́̾͌̍̑̐͒̂̀̀̏̔͊̆̎̐͑͑̾̂̄̀̍̉͂̋̀̎͒̈́̒̍͛̓̌̑̒͐͌̏̓̈̔͑́̒̇̓̎͐̈́̂̓̐͗̽̈́̀̈͑́̇͂̓͑̔͋̂̐̈́̅̽̈͛͘̕̚̚͜͜͜͝͝͠͠͠͠͠͠ͅͅ ̵̧̡̨̨̧̨̨̡̛̛̛̛̼̹̤̪̱͖͔̯̞̙̠̯̪̮̼̜̻͓̜̦̖͍̟̮̼̩͇̫̩̱̙̹͈͙̲̬̭̜̬̳̜̯̲̘̜̤͙̹͓̲̗͕̜̩̦͔͓̯̤͙̗̼͔̭͖͉̉́͛̂͂̄̄̌̔̑̋̒͂͂̔̔̈͗̀̋̐͒̆͋̏͗̒͋͐̋͆̈́͒̃̓̈́̿͗̍͆̏͋͋͛͌̒̆̆̎̂̂͂̉̄̌̿̿̄͐̈́̓̏̈́̾̓̔͑̾̀̈́̂̆́̌̓̍̏̑̑̾̓̽͋̇̊̀͒̈͊̈́̆̋̾̔̈́͐̔̽̈́͊̅̑̊̀́̏̆̏̑̉̈́͊̓̀̃͂̑̇̐̄͑̑́̀̓͆̈́̓̊̇͗͐̈̂̊̍̀͛̂̀̽̓͆̊͂̓̌̈͘̕̕̕̕͜͝͝͝͠͝͝͝͝͝͠͝Ÿ̸̡̡̢̡̨̧̧̢̛̛̛̛̛̩̦̺̝͎̗̘̲͖̘̯̦͇͚̗̬͖͉͍͕̪͈̠̳̟̼̭̳̞̯̩̩͙͖͓̝̭̼̙̼̜̖̖̱͚̳̣̻͙̺̮̪̪̳̖̖͉̹͉̳̤͚̟̤̣͇͚͎̙͇̈̂̊͒̐̎̏̈͗̎̆͐̎̓̈͌̍̃̋̎̃̓̂̅̂͌͒̐̾͑̈́͒̀̄͐̓͒̀̉̄̈͋͛̏͒̈́̉̑̏́̑͗̅͊̔͌́̔̏̆̄̈̊̋͋̿͗̓͑̊̍͋͗̐͊̆̆͛͗̿̀̓̀͐͌̀͑̔̐̃͗̋̒̎̔̈́̄́͛̇̆̃̈́̌̇̿͊̋̊̽̌̇͒̀̏͛̒͆͛̌̍͛̆̓͗̓̈̄̿̏̀́̀̐̌̐̔͆̾̾͒̃̾̚̕̚̚̚̕̚͜͜͜͜͜͜͝͝͝͝͝͝͠͝͝͝͝͠͠͝ͅͅͅͅƠ̴̡̨̡̧̡̡̧̨̡̛̜͇̩̫͓̰͇̦̬͉̹̺͓͕͎̩͕̪̳̥̻̙̗̣̜̜͍̲̬̣̟͔͙̰̪̰͕͚̝͈̳̳͇̝̱̠͙̤̫̹̲̟̩̮͍̟̰̠̠̠͎̘̦̙͇̼͈̱̰̪̖̺͍̞̰̠̬͈̰̱͙̲͕̙͖̩̺̼̼͇̭̫̮̫̝̰̞̟̜̬̫͙͓̗͚̝̥̼̗͓͉̱͉͈̝̮͔̠̞̜̦̰͇͖͈̲͓̜͓̖͓̺̬̙̘̭͖̜̤͙̥̰̜͍̄̌̈́̃͒̔̓̈̅̑̈́͒̄́̍͐̓͊̌̂̏̀́̆͋̐̈́̈́̉̈́̐̌͌̏̈͛͊͊̈́͊̐͌̀͐̾̾̂̐̈̏͂͂́̒̑̊̓̿̉̂̌̓̇̾͑̉͒̽͊̔̽̀̓̐̇̄̇̉̀̄́̐̑̈̓̒̀͋̔͂̐͆͌̒̋́̿͗̌͐̾̓̃̍͌̈́̆͆̉̓͋̒̇̎̈́̊̚̕͘̚͘͘͜͜͜͝͝͝͠͝͝͝͠͠͝͝͝͝͠ͅͅͅͅͅͅͅƯ̵̧̧̨̨̨̨̧̡̨̨̧̡̢̨̛̛̟̞̰̘̗̦̠̼̣̙̦̳͚̣̳͓̲̺̥͖̭͕̺̱̹̣̭̩̤̯̣̩͈̯̣͖͖̻͔̭̦̜͚͓̬̲̹͔̦̮̼̻̘͔͚͕͔̙͈̝̝͓͇͇͙̟̲̮̼̞͎͎̩̰̙͎͙͙̹̙̞͖̠̼̮̮̻͓͍͙̪͋͂͋̎̊̏͊̆̇̔̀́͊̇̔̇̀̈͆͗̉̾̂͆̋̉̉̈́̈͑̍̓̏̂̇̉̏͗̋̈́̄̈́̽̂͗͌̆́̑͛̋̍̿̊͆̑̄̀̊̈̍̐̇̌̓̇̈͌̏͊̑͗̑̃͗̅̌̀͛̍̀̄͑̉́̈́̔͌̈̀̏̋̎̑̐̀͑̇͂̈́̀̿͆͛̒͘̕̚͘̕̕͜͜͜͜͝͝͝ͅ ̸̢̨̢̢̨̡͓̮̺̫̬̭͇̤͍͇̲̭̣͙̮͖̹̫̥͔̪̹͎͔̬̻̪̠͖̳͎̬̯̝̝̫̞̦̼̭̗̠̫̟̱̻͍̮̺̫̗͕̜̱͇̦̲̩̪̜̜̹̗̝̪̟̬̦͍̼̫͍̩̱͎̦͚̝̬͕̼̩̱̩̻̖͎̲̪͎̗͙̥̯̠̹̻͓͚͔̝͚̬͈͖̝̭͔͍̹̮̝̝̘̫̝̥̣̩̤̹̫̗̰͎̟̭̙͇͓͛̀́̍̀͛̄͜͜͜͜͜ͅͅͅͅͅḌ̶̨̨̡̢̢̡̨̡̛̛̛̛͉̪̭̗̪̦̳̞̤̜͓͙͍̭̙̱͖̼͈͈̭̝̝̰̰̭̥̺̣̹̪̥̫̺̱̖̭͓͈̗̦̼͈͖̰͔̟͎̱̮͉̟̼̗̝̘̫̳̦͓̖̠͉̝̲͖̟͓͉͓̺̫͇̪͔͚̮͍͈͚̣̝͓͇̠͍̬̘̹̰̙̞̝̯͇͔̹̮͖͈͙̘̏͒͊̾̑͗͛̂̓̑͊́̋̋́́̊̄̀̓̎̀̌̊͒͌͒̈͑̌̀́͗̏̿͂̈́̒̋̒̀̃̀̒̿͒̑̇̈́͐̂̃̊̅͑̓̃͌̄̈͆̈́̉̓̔͌̌̊̏͐͆̉̍̒͊̒̄̄̚̚̕̚͘͘̕̕̕̚͜͜͠͠͠͝͠͠͝ͅͅǪ̵̧̨̢̢̨̡̢̛̖̻̼̤̪̺͕͎͍̻̘̪̦̭̝̗̫̟̖̳͖̩̟̦̤͇̝̙̺̝͔̥͍͕̙̰̲̮̲͎̳͈̤̙͇̦̖̮̺̩͕̩͔͖̮̞̠̖͖̰̬̫͉͖̲̣̖̱̹͉̮̞̜̫̱̞̮͐́͗̌̎͒̇̿͐̿̅̈́̏̋͛̀̄̎̏̃̌̅̍͛̐̈̈̄̐̈́̿̍̆̈́̐̑̔̾͒̇̅͆͋̈͌̅͆́͗̏̽̏̌͐́̋̀̈̃̈̈͒̾̋̎͂̅̎͊̄̊̌̆̍̔̓̈́̽̊̏̋̋̂̃̓̑̓͑́̑̈́̃̈́͒̍̏͆̅̾̐̉̀̅͌͆̓͋͌̅̇̅͊͛͋͐̑̑͒͐̓͗̀̔͆̍͒͆͑͋̏̍͂͑̌͛́͊͆͒̃͊̈́̑̾̾͌̋̍̈́͑̐̑̆̍͂͋͂̓̉̃̊̈́͂̏̀͋̐̾͗̽͗̒̚̕͘̚̚̕̚͘͘̕̚̕͜͜͜͝͝͝͠͠͝͠͝͠͝͝͝ͅͅͅŅ̴̨̡̡̨̨̧̢̢̢̡̢̛̗͈̫̜͈̺̙̱̦̲̠̩̦̘̘͖̼̭͚̙̗͖͎̫̟̦̣̫̟̪͔̼̮̳͇̜̳̞͍̙͔̲̻̝̞̦̰͎̖͍̖̬̬̖̦̺̖̪͚͇̬̟̲̬͍̦̠͓̱̰̠͎̲͌̈̒̉̍̽̆̋̈̈́̍̇́̉̈̍̈́͛͆̂̑̂̅̂͊̽̃̃̒͘̕̕̕͜͝͝͝ͅE̵̛̛̥͇̼͚̼̹̰̦̺̘̹̠̲̲̤̯̰̬̱̖͚̮͎̥̭͈̙̮͎̯̹̊̉́̌͋͗̇̓̎̃̇̏͗́͂̈͆̃̾͆́̌̽͒̒̊̀̀̆̌̅̾̂̉͊͐̋̒͐̒̃̑̆͐̓̈̾̓͊̊͊̓̾̔̈́̔͊̎̊͑͛̇̌̌́͐̎̊̋̒̈͋̒̊̒̉̓̃́̄͐̈̀̊̌͊̀͋̉̊̆̄̔͊̌́̒̈́̒̂̾̒̆̎͑͌̚̕̕͘̕̚̚̕͜͜͠͠͝͝͝͝͝͝͝͝͝͝͝͝͝͠ͅͅͅ',font=('Arial',70,'normal'))
    sleep(5)
