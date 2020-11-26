
from tkinter import *
from random import *
from time import*

width = 800
height = 500

myInterface = Tk()
s = Canvas(myInterface, width = width, height = height, background = "black")
s.pack()

#Scene 1(Shooting star prehaps?)
#Stars
for stars in range (1, 20):
    starX = randint(10, 790)
    starY = randint(10, 490)
    starX2 = starX - 5
    starX3 = starX + 5
    starY2 = starY + 7.5
    starDownY = starY + 10
    starDownY2 = starDownY - 7.5
    s.create_polygon(starX, starY, starX2, starY2, starX3, starY2, fill = "white")
    s.create_polygon(starX, starDownY, starX2, starDownY2, starX3, starDownY2, fill = "white")

#Little Stars
for Litstars in range (1, 200):
    sizeIncrease = randint(1, 3)
    LitStarX = randint(0, 800)
    LitStarY = randint(0, 500)
    s.create_oval(LitStarX, LitStarY, LitStarX + sizeIncrease, LitStarY + sizeIncrease, fill = "white")

#Meteor flash
def changeflamecolor():
    global meteorLineColors
    
    colorChoice = randint(0, 1)
    if colorChoice == 0:
        meteorLineColors = ["#b71e00", "#f99a00", "#f6ff00"]
    else:
        meteorLineColors = ["#ff0000", "#ff6e00", "#f4cc00"]

#Meteor Animation
meteorLineColors = ["#b71e00", "#f99a00", "#f6ff00"]
meteorX = 800
meteorY = 0
s.update()

for f in range(150):
    meteorLine = s.create_line(meteorX + 10, meteorY - 10, meteorX + 210, meteorY - 210, fill = meteorLineColors[2], width = 2)
    meteorLine1 = s.create_line(meteorX + 10, meteorY - 10, meteorX + 180, meteorY - 180, fill = meteorLineColors[1], width = 6)
    meteorLine2 = s.create_line(meteorX + 10, meteorY - 10, meteorX + 120, meteorY - 120, fill = meteorLineColors[0], width = 9)                          
    meteor = s.create_oval(meteorX, meteorY, meteorX + 20, meteorY - 20, fill = "#494949")
    s.update()
    sleep(0.03)
    s.delete(meteorLine, meteorLine2, meteorLine1, meteor)
    meteorX -= 5
    meteorY += 5
    changeflamecolor()

s.delete("all")

#Scene 2(Hitting earth)
#Stars
for stars in range (1, 20):
    starX = randint(10, 790)
    starY = randint(10, 490)
    starX2 = starX - 5
    starX3 = starX + 5
    starY2 = starY + 7.5
    starDownY = starY + 10
    starDownY2 = starDownY - 7.5
    s.create_polygon(starX, starY, starX2, starY2, starX3, starY2, fill = "white")
    s.create_polygon(starX, starDownY, starX2, starDownY2, starX3, starDownY2, fill = "white")

#Little Stars
for Litstrs in range (1, 200):
    sizeIncrease = randint(1, 3)
    LitStarX = randint(0, 800)
    LitStarY = randint(0, 500)
    s.create_oval(LitStarX, LitStarY, LitStarX + sizeIncrease, LitStarY + sizeIncrease, fill = "white")

#Earth
s.create_oval(-300, 200, 300, 800, fill = "#007ef4")
s.create_polygon(42, 253, 16, 273, 15, 305, 23, 334, 30, 351, 46, 358, 89, 367, 114, 365, 128, 349, 127, 324, 112, 311, 102, 277, 77, 256, fill = "green", smooth = True)
s.create_polygon(44, 495, 57, 466, 86, 444, 119, 425, 155, 420, 184, 420, 207, 410, 225, 403, 243, 413, 267, 447, 284, 481, 285, 500, 200, 550, 100, 550, fill = "green", smooth = True) 

#Meteor
meteorX = 800
meteorY = -100
flameColors = ["#ff0000", "#ff6e00", "#f4cc00"]
for meteorfly in range (100):
    s.delete(meteor)
    ranFlame = randint(0,2)
    flameX = meteorX + 50
    flameY = meteorY
    flame = s.create_polygon(flameX, flameY, flameX + 13.3, flameY + 26.6, flameX + 50, flameY - 15, fill = flameColors[ranFlame])
    flame2 = s.create_polygon(flameX + 13.3, flameY + 26.6, flameX + 13.3*2, flameY + 26.6*2, flameX + 50*1.5, (flameY + 26.6) -15, fill = flameColors[ranFlame])
    flame3 = s.create_polygon(flameX + 13.3*2, flameY + 26.6*2, flameX + 13.3*3, flameY + 26.6*3, flameX + 50*2, (flameY + 26.6*2) - 15, fill = flameColors[ranFlame])
    meteor = s.create_polygon(meteorX, meteorY, meteorX - 15, meteorY + 28, meteorX - 29, meteorY + 81, meteorX - 30, meteorY +82, meteorX + 17, meteorY + 119, meteorX + 64, meteorY + 128, meteorX + 107, meteorY + 100, meteorX + 95, meteorY + 66, meteorX + 84, meteorY + 27, meteorX + 63, meteorY - 8, meteorX + 26, meteorY - 15, fill = "grey")
    s.update()
    sleep(0.03)
    s.delete(flame, flame2, flame3)

    meteorX -= 3
    meteorY += 2

s.delete("all")

#Scene 3 - Meteor closing in
#Sunset
cX = width / 2
cY = 400

skyShades = ["#ffd51c", "#ffcf00", "#ffc700", "#ffbf00", "#ffb200", "#ffaa00", 
             "#ff9d00", "#ff9400", "#ff8800", "#ff7f00", "#ff7200", "#ff6600", 
             "#ff5900", "#ff4300", "#ff2e00", "#ff2a00", "#ff1500", "#ff0000"]

#1st number = start, 2nd = stop, 3rd represents step (reverse step)
#reverse loop (don't overlap smaller sky shades)
for i in range(len(skyShades)-1,-1,-1):
    shade = skyShades[i]

    #ovals gets smaller each time
    skyX = cX - (200 + i * 30) 
    skyY = cY - i * 30
    skyX2 = cX + (200 + i * 30)
    skyY2 = cY + i * 30
 
    s.create_oval(skyX, skyY, skyX2, skyY2, fill = shade, outline = shade)

#Sun
s.create_oval(300, 250, 500, 450, fill = "yellow", outline = "yellow")
s.create_rectangle(0, 400, 800, 500, fill = "black")

#Pointing
xArm = 105
yArm = 497
for arm in range (0, 50):
    s.create_line(100, 505, xArm, yArm, width = 10)
    xArm += 3
    yArm -= 5
    s.update()
    sleep(0.03)

#Talking
birdTxt = s.create_text(cX-200, 100, text = "Is that a bird?", font = "arial 25")
s.update()
sleep(2)
s.delete(birdTxt)

#Meteor coming IN
flameColors = ["#ff0000", "#ff6e00", "#7c7c7c"]
meteorSize = 1
meteorClose = 0
while meteorSize <= 170:
    s.delete(meteorClose)
    randFlame = randint(0, 2)
    meteorClose = s.create_oval(cX - 3*meteorSize, 200 - 3*meteorSize, cX + 3*meteorSize, 200 + 3*meteorSize, fill = flameColors[randFlame], outline = flameColors[randFlame])
    meteorSize += 1
    s.update()
    sleep(0.03)

#Talking
meteorTxt = s.create_text(cX, 100, text = "NO! It's a meteor, and it's coming right at us!!!", font = "arial 25")
s.update()
sleep(4)
s.delete("all")

#Scene Three - Escaping death
#Stars
for stars in range (1, 20):
    starX = randint(10, 790)
    starY = randint(10, 490)
    starX2 = starX - 5
    starX3 = starX + 5
    starY2 = starY + 7.5
    starDownY = starY + 10
    starDownY2 = starDownY - 7.5
    s.create_polygon(starX, starY, starX2, starY2, starX3, starY2, fill = "white")
    s.create_polygon(starX, starDownY, starX2, starDownY2, starX3, starDownY2, fill = "white")

#Little Stars
for Litstrs in range (1, 200):
    sizeIncrease = randint(1, 3)
    LitStarX = randint(0, 800)
    LitStarY = randint(0, 500)
    s.create_oval(LitStarX, LitStarY, LitStarX + sizeIncrease, LitStarY + sizeIncrease, fill = "white")

#Earth
s.create_oval(-300, 200, 300, 800, fill = "#007ef4")
s.create_polygon(42, 253, 16, 273, 15, 305, 23, 334, 30, 351, 46, 358, 89, 367, 114, 365, 128, 349, 127, 324, 112, 311, 102, 277, 77, 256, fill = "green", smooth = True)
s.create_polygon(44, 495, 57, 466, 86, 444, 119, 425, 155, 420, 184, 420, 207, 410, 225, 403, 243, 413, 267, 447, 284, 481, 285, 500, 200, 550, 100, 550, fill = "green", smooth = True)

#Meteor veers away from Earth
#Cordinates change at different speed, causing parabola motion
ySpeed = 3
xSpeed = -2
for meteorfly in range (120):
    #draw meteor
    s.delete(meteor)
    meteor = s.create_polygon(meteorX, meteorY, meteorX - 15, meteorY + 28, meteorX - 29, meteorY + 81, meteorX - 30, meteorY +82, meteorX + 17, meteorY + 119, meteorX + 64, meteorY + 128, meteorX + 107, meteorY + 100, meteorX + 95, meteorY + 66, meteorX + 84, meteorY + 27, meteorX + 63, meteorY - 8, meteorX + 26, meteorY - 15, fill = "grey")
    s.update()
    sleep(0.03)

    #update postition
    meteorX += xSpeed
    meteorY += ySpeed

    #change ySpeed
    ySpeed += -0.1

s.delete("all")

#Scene 4 - Physics are weird
for i in range(len(skyShades)-1,-1,-1):
    shade = skyShades[i]

    #ovals gets smaller each time
    skyX = cX - (200 + i * 30) 
    skyY = cY - i * 30
    skyX2 = cX + (200 + i * 30)
    skyY2 = cY + i * 30
 
    s.create_oval(skyX, skyY, skyX2, skyY2, fill = shade, outline = shade)

#Sun
s.create_oval(300, 250, 500, 450, fill = "yellow", outline = "yellow")
s.create_rectangle(0, 400, 800, 500, fill = "black")

#meteor going OUT
while meteorSize >= 0:
    s.delete(meteorClose)
    randFlame = randint(0, 2)
    meteorClose = s.create_oval(cX - 3*meteorSize, 200 - 3*meteorSize, cX + 3*meteorSize, 200 + 3*meteorSize, fill = flameColors[randFlame], outline = flameColors[randFlame])
    meteorSize -= 1
    s.update()
    sleep(0.03)

#questioning physics
turnTxt = s.create_text(cX, 100, text = "Wait what?!?!?! Did the meteor just turn around?", font = "arial 25")
s.update()
sleep(5)
s.delete(turnTxt)
weirdTxt = s.create_text(cX, 100, text = "I should've paid more attention in physics class...", font = "arial 25")
s.update()
sleep(5)
s.delete(weirdTxt)

s.delete("all")

#Scene 5 - Good bye moon
#Stars
for stars in range (1, 20):
    starX = randint(10, 790)
    starY = randint(10, 490)
    starX2 = starX - 5
    starX3 = starX + 5
    starY2 = starY + 7.5
    starDownY = starY + 10
    starDownY2 = starDownY - 7.5
    s.create_polygon(starX, starY, starX2, starY2, starX3, starY2, fill = "white")
    s.create_polygon(starX, starDownY, starX2, starDownY2, starX3, starDownY2, fill = "white")

#Little Stars
for Litstrs in range (1, 200):
    sizeIncrease = randint(1, 3)
    LitStarX = randint(0, 800)
    LitStarY = randint(0, 500)
    s.create_oval(LitStarX, LitStarY, LitStarX + sizeIncrease, LitStarY + sizeIncrease, fill = "white")

#Moon
cY = 250
cX = 400
moon = s.create_oval(cX + 100, cY + 100, cX - 100, cY - 100, fill = "yellow")
meteorX = cX
meteorY = 550
while meteorY > 325:
    meteor = s.create_polygon(meteorX, meteorY, meteorX - 15, meteorY + 28, meteorX - 29, meteorY + 81, meteorX - 30, meteorY +82, meteorX + 17, meteorY + 119, meteorX + 64, meteorY + 128, meteorX + 107, meteorY + 100, meteorX + 95, meteorY + 66, meteorX + 84, meteorY + 27, meteorX + 63, meteorY - 8, meteorX + 26, meteorY - 15, fill = "grey")
    meteorY -= 1
    s.update()
    sleep(0.03)
    s.delete(meteor)
s.delete(moon)

#Explosion
flameColors = ["#b71e00", "#f99a00", "#f6ff00"]
explosionX = 178
explosionY = 47
for time in range (20):
    randFlame = randint(0, 2)
    outline = randint(0, 2)
    explosion = s.create_polygon(explosionX, explosionY, explosionX + 46, explosionY + 142, explosionX - 6, explosionY + 261, explosionX + 110, explosionY + 296, explosionX + 168, explosionY + 441, explosionX + 272, explosionY + 344, explosionX + 387, explosionY + 240, explosionX +357, explosionY + 111, explosionX + 317, explosionY - 8, explosionX + 180, explosionY + 49, fill = flameColors[randFlame], outline = flameColors[outline], width = 5) 
    s.update()
    sleep(0.03)
    s.delete(explosion)
s.delete("all")

#End Scene
s.create_text(cX, cY, text = "And that was the story of how the moon disappeared.", font = "Arial 20", fill = "white")
s.update()
