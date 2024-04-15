import turtle  # gör detta möjligt, detta är hur det är möjligt att göra missle, enemy, ally och player. Denna modul använder tkinter för underläggande grafiker
import random # gör det möjligt att generera modul, modulen innehåller en slumpmässig nummer generator
import math # gör det möjligt att utföra matematiska formler i python
import pygame
pygame.mixer.init()
pygame.mixer.music.load("")
pygame.mixer.music.play(-1,0.0)
# sätter upp skärmen
screen = turtle.Screen() # klass som innehåller modulen turtle, screen = raden tilldelar ett resultat
screen.setup(width=600, height=600) # sätter upp skärmen
screen.bgcolor("black") # bestämmer bakgrundsfärgen
screen.title("VisionHub games") # Skriver in vad det ska heta(på skärmen)

border_pen = turtle.Turtle() # rita tilldelar till variabeln
border_pen.speed(4) # ritningen kan ha en hastighet när den ritar jag vill inte att det ska synas att det ritar utan att den alltid är där , därför är den satt på snabbaste hastigheten för att alltid synas på skärmen
border_pen.color("yellow")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


class Sprite(turtle.Turtle):
    def __init__(self, sprite, color, startx, starty):
        super().__init__(shape=sprite)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)
        if self.xcor() > 290 or self.xcor() < -290 or self.ycor() > 290 or self.ycor() < -290:
            self.rt(60)



class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty, speed):
        super().__init__(spriteshape, color, startx, starty)
        self.speed = speed

    def move_left(self):
        self.lt(45)

    def move_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1



class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty, speed):
        super().__init__(spriteshape, color, startx, starty)
        self.speed = speed


class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty, speed):
        super().__init__(spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=None)
        self.speed = speed
        self.status = "ready"
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "firing":
            self.fd(self.speed)
            if self.xcor() < -290 or self.xcor() > 290 or \
                    self.ycor() < -290 or self.ycor() > 290:
                self.goto(-1000, 1000)
                self.status = "ready"


class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty, speed):
        super().__init__(spriteshape, color, startx, starty)
        self.speed = speed


class Game():
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.lives_display = turtle.Turtle()
        self.lives_display.speed(0)
        self.lives_display.color("white")
        self.lives_display.penup()
        self.lives_display.hideturtle()
        self.update_lives_display()

    def update_lives_display(self):
        self.lives_display.clear()
        self.lives_display.goto(-280, 260)
        self.lives_display.write("Lives: {}".format(self.lives), align="left", font=("Courier", 16, "normal"))

    def draw_border(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()



def is_collision(sprite1, sprite2):
    distance = math.sqrt((sprite1.xcor() - sprite2.xcor()) ** 2 + (sprite1.ycor() - sprite2.ycor()) ** 2)
    if distance < 20:
        return True
    else:
        return False



def create_allies():
    num_allies = 3
    for _ in range(num_allies):
        ally = Ally("square", "blue", random.randint(-280, 280), random.randint(-280, 280), ally_speed)
        allies.append(ally)


def choose_mode():
    mode = screen.textinput("Choose game mode", "Enter 'slow', 'medium', or 'fast': ").lower()
    if mode == "slow":
        return 10, 2, 15, 5
    elif mode == "medium":
        return 15, 3, 20, 7
    elif mode == "fast":
        return 20, 4, 25, 10
    else:
        print("Invalid mode! Setting to medium.")
        return 15, 3, 20, 7


player_speed, enemy_speed, missile_speed, ally_speed = choose_mode()


player = Player("triangle", "white", 0, -250, player_speed)


num_enemies = 5
enemies = []
for _ in range(num_enemies):
    enemy = Enemy("circle", "red", random.randint(-280, 280), random.randint(100, 280), enemy_speed)
    enemies.append(enemy)


missile = Missile("triangle", "orange", 0, 0, missile_speed)


allies = []
create_allies()


game = Game()
game.draw_border()


turtle.listen()
turtle.onkey(player.move_left, "Left")
turtle.onkey(player.move_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")


while game.lives > 0:
    player.move()
    missile.move()


    for enemy in enemies:
        enemy.move()


        if is_collision(player, enemy):
            game.lives -= 1
            game.update_lives_display()
            print("Lost a life! Lives left:", game.lives)
            enemy.goto(random.randint(-280, 280), random.randint(100, 280))


    for ally in allies:
        ally.move()


        if is_collision(player, ally):
            game.lives += 1
            game.update_lives_display()
            print("Gained a life! Lives:", game.lives)
            ally.goto(random.randint(-280, 280),

                      random.randint(-280, 280))


    for enemy in enemies:
        if is_collision(missile, enemy):
            game.score += 10
            print("Score:", game.score)
            missile.goto(-1000, 1000)
            missile.status = "ready"
            enemy.goto(random.randint(-280, 280), random.randint(100, 280))

    for ally in allies:
        if is_collision(missile, ally):
            game.lives += 1
            game.update_lives_display()
            print("Gained a life! Lives:", game.lives)
            ally.goto(random.randint(-280, 280), random.randint(-280, 280))

print("Game Over")

turtle.done()
