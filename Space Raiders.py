""" In this game, you start as a triangle, you have 0 points, and you're
at level 1. You move around to hit objects in space, and if you hit one,
you gain a point. The objects start as asteroids, and at 10 points,
you gain a level, and the asteroids turn into moons, then planets, stars,
and then unknown planets. later. You have an option to change your color,
which costs 5 points, an option to change your shape, which costs 10 points,
and an option to double the amount of points you get for 25 points.
You start at 100 health, and if you get to 0 health, you lose, and have
an option to restart the whole game, or quit. You lose health every time
you hit the spaceship that flies around in the game."""

from turtle import *
import math, random, time, os, socket, uuid, re

def getIP():
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    print("IP Address: " ,IP)

# Functions for some keyboard bindings
# PRESS THE RIGHT ARROW KEY ON YOUR KEYBOARD TO TURN RIGHT
def triangleright():
    right(30)
# PRESS THE LEFT ARROW KEY ON YOUR KEYBOARD TO TURN LEFT
def triangleleft():
    left(30)
# PRESS THE DOWN ARROW KEY ON YOUR KEYBOARD TO TURN AROUND
def triangledown():
    right(180)

# Directions on what to do
print("Press the 'esc' key on your keyboard to exit out of the game.")
print("Press the 'Right' or 'd' key on your keyboard to turn right.")
print("Press the 'Left' or 'a' key on your keyboard to turn left.")
print("Press the 'Down' or 'w or s' key on your keyboard to turn all the way around.")
print("\nWatch out for the spaceship that moves around the map! It may be evil.\n")


# Python Turtle stuff
canvas = Screen()
canvas.title("Space Raiders")
canvas.bgcolor("Black")
canvas.bgpic("Background.gif")
canvas.tracer(3, 25)
Comp1 = Turtle()
Comp2 = Turtle()
Comp3 = Turtle()
Comp4 = Turtle()
Comp5 = Turtle()
ColorChanger = Turtle()
ShapeChanger = Turtle()
DoublePoints = Turtle()
Spaceship = Turtle()

# start facing downward
penup()
left(90)
Stamina = 100

# This makes it so they go as fast as they can
speed(0);Comp1.speed(0);Comp2.speed(0);Comp3.speed(0);Comp4.speed(0);Comp5.speed(0)
Spaceship.speed(0);ColorChanger.speed(0);ShapeChanger.speed(0);DoublePoints.speed(0)

# Function to increase your size
#def increaseSize():
#    size = shapesize()
#    increase = tuple([1.05 * num for num in size])
#    shapesize(*increase)

# Go faster
def goFaster():
    global Stamina
    if Stamina > 100:
        Stamina = 100
    if Stamina > 0:
        forward(Stamina / 15 * speed / 2)
        Stamina -= 1
    else:
        print("You have no more Stamina!")

def startconsole():
    global points
    global health
    print("\nYou have paused the game. You're free to use commands while the game is paused.")
    print("These commands include: 'myscore', 'setpoints'")
    typing = input(": ")
    commands = ["myscore", "setpoints", "sethealth", "IP", "ip", "mac", "MAC"]
    if typing == "stop" or typing == "cancel" or typing == "exit" or typing == "resume":
        print("You have exited out of typing mode.")
        return
    if typing == commands[0]:
        print("Level: ", level, "\nHealth: "  ,health, "\nPoints: " ,points, "\nStamina: " ,Stamina)
        startconsole()
    if typing == commands[1]:
        points = int(input("How many points would you like?\nEnter points here: "))
        updatescore()
    if typing == commands[2]:
        health = int(input("How much health would you like?\nEnter here: "))
        updateHealth()
    if typing == commands[3] or typing == commands[4]:
        getIP()
        startconsole()
    if typing == commands[5] or typing == commands[6]:
        MAC = print("Your MAC Address is" + ':'.join(re.findall('..', '%012x' % uuid.getnode())))
        startconsole()
    else:
        startconsole()

speed = 3
    
# Key bindings
listen()
onkey(triangleright, "Right");onkey(triangleright, "d")
onkey(triangleleft, "Left");onkey(triangleleft, "a")
onkey(triangledown, "Down");onkey(triangledown, "s");onkey(triangledown, "w")
onkeypress(goFaster, "space")
onkey(startconsole, "p")
onkey(exit, "Escape")

# Register the shapes of everything
register_shape("Spaceship.gif")
register_shape("ChangeColor.gif")
register_shape("ShapeChanger.gif")
register_shape("DoublePoints.gif")
register_shape("Rigel.gif")
register_shape("Sol.gif")
register_shape("Pollux.gif")
register_shape("Stellar.gif")
register_shape("DeathStar.gif")
register_shape("Asteroid.gif")
register_shape("Asteroid2.gif")
register_shape("Asteroid3.gif")
register_shape("Asteroid4.gif")
register_shape("Asteroid5.gif")
register_shape("Moon.gif")
register_shape("Callisto.gif")
register_shape("Titan.gif")
register_shape("Io.gif")
register_shape("Umbriel.gif")
register_shape("Mercury.gif")
register_shape("Venus.gif")
register_shape("Earth.gif")
register_shape("Mars.gif")
register_shape("Jupiter.gif")
register_shape("CustomPlanet1.gif")
register_shape("CustomPlanet2.gif")
register_shape("CustomPlanet3.gif")
register_shape("CustomPlanet4.gif")
register_shape("CustomPlanet5.gif")

# Set the shapes of everything
shape("triangle");color("Turquoise");DoublePoints.shape("DoublePoints.gif");ShapeChanger.shape("ShapeChanger.gif");ColorChanger.shape("ChangeColor.gif");Spaceship.shape("Spaceship.gif")

# Set the Positions of the asteroids
Spaceship.penup();Spaceship.setposition(259, -259);ColorChanger.penup();ColorChanger.setposition(-370, 227)
ShapeChanger.penup();ShapeChanger.setposition(-370, -227);DoublePoints.penup();DoublePoints.setposition(-370, 0)

Comp1.penup();Comp1.left(random.randint(-360, 360))
Comp1.setposition(random.randint(-259, 259), random.randint(-259, 259))

Comp2.penup();Comp2.left(random.randint(-360, 360))
Comp2.setposition(random.randint(-259, 259), random.randint(-259, 259))

Comp3.penup();Comp3.left(random.randint(-360, 360))
Comp3.setposition(random.randint(-259, 259), random.randint(-259, 259))

Comp4.penup();Comp4.left(random.randint(-360, 360))
Comp4.setposition(random.randint(-259, 259), random.randint(-259, 259))

Comp5.penup();Comp5.left(random.randint(-360, 360))
Comp5.setposition(random.randint(-259, 259), random.randint(-259, 259))

# All the functions for boundaries
# Spaceship boundaries
def Spaceship_fixleft():
    Ship = Spaceship.xcor()
    if Ship < -260:
        Ship = -260
        Spaceship.setx(Ship)
        Spaceship.right(180)

def Spaceship_fixright():
    Ship = Spaceship.xcor()
    if Ship > 260:
        Ship = 260
        Spaceship.setx(Ship)
        Spaceship.right(180)
    
def Spaceship_fixdown():
    Ship = Spaceship.ycor()
    if Ship < -260:
        Ship = -260
        Spaceship.sety(Ship)
        Spaceship.right(180)

def Spaceship_fixup():
    Ship = Spaceship.ycor()
    if Ship > 260:
        Ship = 260
        Spaceship.sety(Ship)
        Spaceship.right(180)
        
# My own boundaries
def fixleft():
    x = xcor()
    if x < -260:
        x = 260
    setx(x)

def fixright():
    x = xcor()
    if x > 260:
        x = -260
    setx(x)
    
def fixdown():
    y = ycor()
    if y < -260:
        y = 260
    sety(y)
    
def fixup():
    y = ycor()
    if y > 260:
        y = -260
    sety(y)
    
# Comp1 boundaries
def comp1_fixleft():
    a = Comp1.xcor()
    if a < -260:
        a = -260
        Comp1.setx(a)
        Comp1.right(180)

def comp1_fixright():
    a = Comp1.xcor()
    if a > 260:
        a = 260
        Comp1.setx(a)
        Comp1.right(180)
    
def comp1_fixdown():
    b = Comp1.ycor()
    if b < -260:
        b = -260
        Comp1.sety(b)
        Comp1.right(180)

def comp1_fixup():
    b = Comp1.ycor()
    if b > 260:
        b = 260
        Comp1.sety(b)
        Comp1.right(180)
    
# Comp2 boundaries
def comp2_fixleft():
    c = Comp2.xcor()
    if c < -260:
        c = -260
        Comp2.setx(c)
        Comp2.right(180)

def comp2_fixright():
    c = Comp2.xcor()
    if c > 260:
        c = 260
        Comp2.setx(c)
        Comp2.right(180)
    
def comp2_fixdown():
    d = Comp2.ycor()
    if d < -260:
        d = -260
        Comp2.sety(d)
        Comp2.right(180)

def comp2_fixup():
    d = Comp2.ycor()
    if d > 260:
        d = 260
        Comp2.sety(d)
        Comp2.right(180)
    
# Comp3 boundaries
def comp3_fixleft():
    e = Comp3.xcor()
    if e < -260:
        e = -260
        Comp3.setx(e)
        Comp3.right(180)

def comp3_fixright():
    e = Comp3.xcor()
    if e > 260:
        e = 260
        Comp3.setx(e)
        Comp3.right(180)
    
def comp3_fixdown():
    f = Comp3.ycor()
    if f < -260:
        f = -260
        Comp3.sety(f)
        Comp3.right(180)

def comp3_fixup():
    f = Comp3.ycor()
    if f > 260:
        f = 260
        Comp3.sety(f)
        Comp3.right(180)
    
# Comp4 boundaries
def comp4_fixleft():
    g = Comp4.xcor()
    if g < -260:
        g = -260
        Comp4.setx(g)
        Comp4.right(180)

def comp4_fixright():
    g = Comp4.xcor()
    if g > 260:
        g = 260
        Comp4.setx(g)
        Comp4.right(180)
    
def comp4_fixdown():
    h = Comp4.ycor()
    if h < -260:
        h = -260
        Comp4.sety(h)
        Comp4.right(180)

def comp4_fixup():
    h = Comp4.ycor()
    if h > 260:
        h = 260
        Comp4.sety(h)
        Comp4.right(180)
    
# Comp5 boundaries
def comp5_fixleft():
    i = Comp5.xcor()
    if i < -260:
        i = -260
        Comp5.setx(i)
        Comp5.right(180)

def comp5_fixright():
    i = Comp5.xcor()
    if i > 260:
        i = 260
        Comp5.setx(i)
        Comp5.right(180)
    
def comp5_fixdown():
    j = Comp5.ycor()
    if j < -260:
        j = -260
        Comp5.sety(j)
        Comp5.right(180)

def comp5_fixup():
    j = Comp5.ycor()
    if j > 260:
        j = 260
        Comp5.sety(j)
        Comp5.right(180)

# Updates your score
def updatescore():
    pointstring = "Points: %s" %points
    point_pen.clear()
    point_pen.write(pointstring, False, align = "left", font = ("Arial Bold", 16, "normal"))

# Set your health to 100
health = 100

health_pen = Turtle()
    
# Draw your health points
def updateHealth():
    health_pen.speed(0)
    health_pen.color("Red")
    health_pen.penup()
    health_pen.setposition(155, -270)
    healthstring = "Health: %s" %health
    health_pen.write(healthstring, False, align = "left", font = ("Arial Bold", 16, "normal"))
    health_pen.hideturtle()
    
updateHealth()

# Start out with 0 points
points = 0

# This is how many points you get from colliding with the objects
givenPoints = 1
    
# Draw your point score
point_pen = Turtle()
point_pen.speed(0)
point_pen.color("White")
point_pen.penup()
point_pen.setposition(-265, 260)
pointstring = "Points: %s" %points
point_pen.write(pointstring, False, align = "left", font = ("Arial Bold", 16, "normal"))
point_pen.hideturtle()

# Set the level to 1
level = 1

# Draw the level
level_pen = Turtle()
level_pen.speed(0)
level_pen.color("White")
level_pen.penup()
level_pen.setposition(98, 260)
levelstring = "Level %s: Asteroids" %level
level_pen.write(levelstring, False, align = "left", font = ("Arial", 16, "normal"))
level_pen.hideturtle()

# Option to change your color if you have at least 5 points
def differentColor(x, y):
    global points
    if points < 5:
        print("\nYou must have atleast 5 points to use this feature.")
    else:
        print("This costs 5 points to use. Type 'Yes' if you want to change your color.")
        answer = input("Would you like to change your color?\nEnter here:")
        if answer == "Yes" or answer == "yes" or answer == "yea" or answer == "ye":
            yourcolor = input("\nWhat color would you like to change to? You cannot change to white.\nEnter here: ")
            color(yourcolor)
            bgcolor(yourcolor)
            points -= 5
            updatescore()
            while yourcolor == "White" or yourcolor == "white":
                print("Please choose a different color")
                yourcolor = input("\nWhat color would you like to change to? You cannot change to white.\nEnter here: ")
                color(yourcolor)
                bgcolor(yourcolor)
            else:
                print("Invalid color")
                return
            if yourcolor == ("Black") or yourcolor == ("black"):
                color("White")
                print("Your ship color has been changed to white for visibility.")
        if answer == "No" or answer == "no":
            print("Click on it again if you'd like to change your color.")
            return
        else:
            print("Invalid color, please use uppercase on the first letter.")
            return
        
# Changes your color on click at the cost of 5 points
ColorChanger.onclick(differentColor)

# Option to change your shape if you have at least 10 points
def differentShape(x, y):
    global points
    if points < 10:
        print("\nYou must have atleast 10 points to use this feature.")
    else:
        print("This costs 10 points to use. Type 'Yes' if you want to change your shape.")
        answer = input("Would you like to change your shape?\nEnter here:")
        if answer == "Yes" or answer == "yes" or answer == "yea" or answer == "ye":
            print("These shapes include: 'arrow', 'turtle', 'circle', 'square', 'triangle', and 'classic'.")
            yourshape = input("\nWhat shape would you like to change to? Do not enter a shape if you do not want to do this.\nEnter here: ")
            if yourshape == "arrow" or yourshape == "turtle" or yourshape == "circle" or yourshape == "square" or yourshape == "triangle" or yourshape == "classic":
                shape(yourshape)
                points -= 10
                updatescore()
            else:
                print("You did not enter a correct shape!")
                return
        else:
            return
# Changes your shape on click at the cost of 10 points.
ShapeChanger.onclick(differentShape)

# Function that doubles your points on click if you have 25 points
def doublePoints(x, y):
    global givenPoints
    global points
    if points < 25:
        print("\nYou must have 25 points to use this feature.")
    else:
        print("This costs 25 points to use. Type 'Yes' if you would like to use this feature.")
        answer = input("Would you like to double your points?\nEnter here:")
        if answer == "Yes" or answer == "yes":
            doubling = input("Are you sure? Type 'Yes' or 'No'\nEnter here: ")
            if doubling == "Yes" or doubling == "yes" or doubling == "ye":
                givenPoints *= 2
                points -= 25
                updatescore()
            if doubling == "No" or doubling == "no":
                print("Click on it again if you want to gain double points.")
                return
        else:
            return
    if givenPoints > 25:
        print("You have exceeded the amount of points earned")
        givenPoints = 25
        points += 25
        updatescore()
        
# Doubles the points you earn at a cost of 25 points
DoublePoints.onclick(doublePoints)

running = True
# Main game loop
while running:
    # All functions for boundaries
    fixleft()
    fixright()
    fixup()
    fixdown()
    Spaceship_fixleft()
    Spaceship_fixright()
    Spaceship_fixup()
    Spaceship_fixdown()
    comp1_fixleft()
    comp1_fixright()
    comp1_fixup()
    comp1_fixdown()
    comp2_fixleft()
    comp2_fixright()
    comp2_fixup()
    comp2_fixdown()
    comp3_fixleft()
    comp3_fixright()
    comp3_fixup()
    comp3_fixdown()
    comp4_fixleft()
    comp4_fixright()
    comp4_fixup()
    comp4_fixdown()
    comp5_fixleft()
    comp5_fixright()
    comp5_fixup()
    comp5_fixdown()
    # Formulas for distance
    spaceship = math.sqrt(math.pow(xcor()-Spaceship.xcor(),2) + math.pow(ycor()-Spaceship.ycor(),2))
    a = math.sqrt(math.pow(xcor()-Comp1.xcor(),2) + math.pow(ycor()-Comp1.ycor(),2))
    b = math.sqrt(math.pow(xcor()-Comp2.xcor(),2) + math.pow(ycor()-Comp2.ycor(),2))
    c = math.sqrt(math.pow(xcor()-Comp3.xcor(),2) + math.pow(ycor()-Comp3.ycor(),2))
    d = math.sqrt(math.pow(xcor()-Comp4.xcor(),2) + math.pow(ycor()-Comp4.ycor(),2))
    e = math.sqrt(math.pow(xcor()-Comp5.xcor(),2) + math.pow(ycor()-Comp5.ycor(),2))
    # If you touch the spaceship, you loose 5 health
    if spaceship < 30:
        health -= 25
        healthstring = "Health: %s" %health
        health_pen.clear()
        health_pen.write(healthstring, False, align = "left", font = ("Arial Bold", 16, "normal"))
        Spaceship.setposition(random.randint(-259, 259), random.randint(-259, 259))
        Spaceship.right(random.randint(-360, 360))
    # If im close to one of the computers, then they jump forward
    if a < 60:
        Comp1.forward(random.randint(20, 50))
    if b < 60:
        Comp2.forward(random.randint(20, 50))
    if c < 60:
        Comp3.forward(random.randint(20, 50))
    if d < 60:
        Comp4.forward(random.randint(20, 50))
    if e < 60:
        Comp5.forward(random.randint(20, 50))
    # If I get close, they dissapear, I get bigger, and the score updates.
    if a < 30:
        Comp1.setposition(random.randint(-259, 259), random.randint(-259, 259))
        # Update the score
        points += givenPoints
        updatescore()
    if b < 30:
        Comp2.setposition(random.randint(-259, 259), random.randint(-259, 259))
       # Update the score
        points += givenPoints
        updatescore()
    if c < 30:
        Comp3.setposition(random.randint(-259, 259), random.randint(-259, 259))
        # Update the score
        points += givenPoints
        updatescore()
    if d < 30:
        Comp4.setposition(random.randint(-259, 259), random.randint(-259, 259))
        # Update the score
        points += givenPoints
        updatescore()
    if e < 30:
        Comp5.setposition(random.randint(-259, 259), random.randint(-259, 259))
       # Update the score
        points += givenPoints
        updatescore()
     #You are at level 2 between 10 and 25 points.
    if points >= 10 and points < 25:
        level = 2
        if points == 10:
            levelstring = "Level %s: Moons" %level
            level_pen.clear()
            level_pen.write(levelstring, False, align = "left", font = ("Arial", 16, "normal"))
    # I made this code because if you get 2 points at once for example
    # And you go to 10 points, without getting level 2
    # This will fix it, and you will be set to level 2
    if points >= 10 and level == 1:
        level = 2
        if points == 10:
            levelstring = "Level %s: Moons" %level
            level_pen.clear()
            level_pen.write(levelstring, False, align = "left", font = ("Arial", 16, "normal"))
    # You are at level 3 between 25 and 50 points.
    if points >= 25 and points < 50:
        level = 3
        if points == 25:
            levelstring = "Level %s: Planets" %level
            level_pen.clear()
            level_pen.write(levelstring, False, align = "left", font = ("Arial", 16, "normal"))
    # if you go to 25 points without getting level 3,
    # This will fix it, and you will be set to level 3
    if points >= 25 and level <= 2:
        level = 3
        if points == 25:
            levelstring = "Level %s: Planets" %level
            level_pen.clear()
            level_pen.write(levelstring, False, align = "left", font = ("Arial", 16, "normal"))
    # You are at level 4 between 50 and 75 points.
    if points >= 50 and points < 75:
        level = 4
        if points == 50:
            levelstring = "Level %s: Stars" %level
            level_pen.clear()
            level_pen.write(levelstring, False, align = "left", font = ("Arial", 16, "normal"))
    # if you go to 50 points without getting level 4,
    # This will fix it, and you will be set to level 4
    if points >= 50 and level <= 3:
        level = 4
        if points == 50:
            levelstring = "Level %s: Stars" %level
            level_pen.clear()
            level_pen.write(levelstring, False, align = "left", font = ("Arial", 16, "normal"))
    if points == 75 and level == 4:
        level = 5
        if points == 75:
            levelstring = "Level %s: Unknown Planets" %level
            level_pen.clear()
            level_pen.write(levelstring, False, align = "left", font = ("Arial", 16, "normal"))
    # if you go to 75 points without getting level 5,
    # This will fix it, and you will be set to level 5
    if points >= 75 and level <= 4:
        level = 5
        if points == 75:
            levelstring = "Level %s: Unknown Planets" %level
            level_pen.clear()
            level_pen.write(levelstring, False, align = "left", font = ("Arial", 16, "normal"))
    if level == 1:
        Spaceship.forward(4);Spaceship.right(random.randint(-3, 4))
        Comp1.forward(3);Comp1.right(random.randint(-9, 9))
        Comp2.forward(3);Comp2.right(random.randint(-9, 9))
        Comp3.forward(3);Comp3.right(random.randint(-9, 9))
        Comp4.forward(3);Comp4.right(random.randint(-9, 9))
        Comp5.forward(3);Comp5.right(random.randint(-9, 9))
        Comp1.shape("Asteroid.gif");Comp2.shape("Asteroid2.gif");Comp3.shape("Asteroid3.gif");Comp4.shape("Asteroid4.gif");Comp5.shape("Asteroid5.gif")
    # Once you are level 2, everything gets faster than before, and the
    # Asteroids turn into Moons.
    if level == 2:
        Spaceship.forward(5);Spaceship.right(random.randint(-3, 4))
        Comp1.forward(3);Comp1.right(random.randint(-7, 9))
        Comp2.forward(3);Comp2.right(random.randint(-7, 9))
        Comp3.forward(3);Comp3.right(random.randint(-7, 9))
        Comp4.forward(3);Comp4.right(random.randint(-7, 9))
        Comp5.forward(3);Comp5.right(random.randint(-7, 9))
        Comp1.shape("Moon.gif");Comp2.shape("Titan.gif");Comp3.shape("Callisto.gif");Comp4.shape("Io.gif");Comp5.shape("Umbriel.gif")
    # Once you are level 5, everything gets faster than before, and the
    # Moons turn into Planets.
    if level == 3:
        Spaceship.forward(5);Spaceship.right(random.randint(-3, 4))
        Comp1.forward(3);Comp1.right(random.randint(-5, 9))
        Comp2.forward(3);Comp2.right(random.randint(-5, 9))
        Comp3.forward(3);Comp3.right(random.randint(-5, 9))
        Comp4.forward(3);Comp4.right(random.randint(-5, 9))
        Comp5.forward(3);Comp5.right(random.randint(-5, 9))
        Comp1.shape("Mercury.gif");Comp2.shape("Venus.gif");Comp3.shape("Earth.gif");Comp4.shape("Mars.gif");Comp5.shape("Jupiter.gif")
    # Once you are level 4, everything gets faster than before, and the
    # Planets turn into stars.
    if level == 4:
        Spaceship.forward(5);Spaceship.right(random.randint(-3, 4))
        Comp1.forward(3);Comp1.right(random.randint(-3, 9))
        Comp2.forward(3);Comp2.right(random.randint(-3, 9))
        Comp3.forward(3);Comp3.right(random.randint(-3, 9))
        Comp4.forward(3);Comp4.right(random.randint(-3, 9))
        Comp5.forward(3);Comp5.right(random.randint(-3, 9))
        Comp1.shape("Rigel.gif");Comp2.shape("Sol.gif");Comp3.shape("Pollux.gif");Comp4.shape("Stellar.gif");Comp5.shape("DeathStar.gif")
    # Once you are level 5, everything gets faster than before, and the
    # Stars turn into Planets that are currently Unknown.
    if level == 5 :
        Spaceship.forward(5);Spaceship.right(random.randint(-3, 4))
        Comp1.forward(3);Comp1.right(random.randint(-3, 9))
        Comp2.forward(3);Comp2.right(random.randint(-3, 9))
        Comp3.forward(3);Comp3.right(random.randint(-3, 9))
        Comp4.forward(3);Comp4.right(random.randint(-3, 9))
        Comp5.forward(3);Comp5.right(random.randint(-3, 9))
        Comp1.shape("CustomPlanet1.gif");Comp2.shape("CustomPlanet2.gif");Comp3.shape("CustomPlanet3.gif");Comp4.shape("CustomPlanet4.gif");Comp5.shape("CustomPlanet5.gif")    
    # If you are 0 health, you restart.
    if health == 0:
        print("You lost all your health!")
        restart = input("Would you like to restart? Type 'Yes' or 'No' \n:")
        if restart == "Yes" or restart == "yes":
            speed = 3
            Stamina = 100
            shapesize(1, 1, 1)
            health = 100
            healthstring = "Health: %s" %health
            health_pen.clear()
            health_pen.write(healthstring, False, align = "left", font = ("Arial Bold", 16, "normal"))
            points = 0
            updatescore()
            level = 1
            levelstring = "Level %s: Asteroids" %level
            level_pen.clear()
            level_pen.write(levelstring, False, align = "left", font = ("Arial", 16, "normal"))
        elif restart == "No" or restart == "no":
            bye()
        else:
            print("Invalid response")
    forward(speed)

    #canvas.update()
