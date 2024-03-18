import os#Använda opertaions systemet, en mellan person till underliggande operations system, genom detta kan man ta reda på viktig information
import random#Hjälper med att skapa slumpmässiga variabler
import turtle#För att skapa turtle objekt
#Sätter upp turtle skärmen
turtle.fd(0)#Sätter framåt riktningen till 0, fd är en metod som flyttar variabeln framåt med en angiven distans.
turtle.speed(0)#Sätter variabelns hastighet till 0. Detta betyder att variabeln rör sig direkt utan någon animeringsfördröjnin.
turtle.bgcolor("black")#Sätter Bakgrund färgen till svart, "black" säger att det ska vara svart.
turtle.setundobuffer(1)#Sätter storleken på ångra bufferten sparar en historik av det variabeln gör. Ettan gör så att man kan göra om ett tidigare riktkommandon.
turtle.tracer(1)#Aktiverar variablens animation, kontrollerar animations hastigheten.
#Definierar en klass för att skapa en karaktär(sprite)
class Sprite(turtle.Turtle):#Definerar en klass som heter sprite
    def __init__(self, sprite, color, startx, starty):#Self, insatsen av klassen Sprite, klassen har med sprites att göra Color, färg associerad med spriten Startx, 
        super().__init__(shape=sprite)  # Pass the shape directly
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx, starty)
        self.speed = 1
#Gör så att karaktärerna har möjligheten att röra på sig
    def move(self):
        self.fd(self.speed)
#Hanterar gränserna och när en karaktär nuddar gränserna så byter de riktning
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)
        if self.xcor() > -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        if self.ycor() > -290:
            self.sety(-290)
            self.rt(60)
#Hanterar kollitionerna mellan de olika karaktärerna
def is_collision(self, other):
    if (self.xcor() >= (other.xcor() - 20)) and \
            (self.xcor() <= (other.xcor() + 20)) and \
            (self.ycor() >= (other.ycor() - 20)) and \
            (self.ycor() <= (other.ycor() + 20)):
        return True
    else:
        return False





#En klass för spelar karaktären
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3
#Hanterar spelarens åtgärder
    def turn_left(self):
        self.lt(45)


    def turn_left(self):
        self.rt(45)


    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1
#Definerar en klass för andra typer av karaktärer
class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0,360))

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 8
        self.setheading(random.randint(0,360))

    def move(self):
        self.fd(self.speed)
#Hanterar gränser
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
        if self.xcor() > -290:
            self.setx(-290)
            self.lt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)
        if self.ycor() > -290:
            self.sety(-290)
            self.lt(60)


class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)
    def fire(self):
        if self.status == "ready":
           self.goto(player.xcor(), player.ycor())
           self.setheading(player.heading())
           self.status = "firing"
    def move(self):

        if self.status == "ready":
            self.goto(-1000, 1000)

        if self.status == "firing":
            self.fd(self.speed)

            if self.xcor() < -290 or self.x.cor() > 290 or \
                    self.ycor()< -290 or self.ycor()> 290:
                    self.goto(-1000,1000)
                    self.status = "ready"






class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3
    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.size(3)
        self.pen.penup()
        self.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()


game =  Game()
game.draw_border()









player = Player("triangle", "white", 0, 0)
enemy = Enemy("circle", "red", -100, 0)
misille = Missile("triangle", "yellow", 0,0)
ally = Ally("square", "blue", 0, 0)

turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_left, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(misille.fire, "space")
turtle.listen()


while True:
    player.move()
    enemy.move()
    misille.move()
    ally.move()

    if player.is_collition(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        enemy.goto(x, y)

    if misille.is_collition(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        enemy.goto(x, y)
        misille.status = "ready"




    if misille.is_collition(ally):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        ally.goto(x, y)
        misille.status = "ready"




delay = input("Press enter to finish. >")
