import turtle
screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("white")
t = turtle.Turtle()
t.penup()
t.goto(0, 250)
t.pendown()
t.pencolor('dodger blue')
t.write("My Favorites", font=("Arial", 40, "bold italic"), align="center")

t.speed(0)
t.penup()
t.goto(150, 0)
t.pendown()
screen.addshape('ble color.gif')
t.shape("ble color.gif")
t.stamp()
t.shape('classic')
t.penup()
t.goto(-150, 0)
t.pendown()
screen.addshape('cat.gif')
t.shape("cat.gif")
t.stamp()
t.shape('classic')
t.pencolor('black')

t.fillcolor('green')
t.begin_fill()
t.penup()
t.goto(250, -250)
t.pendown()
t.setheading(0)
t.pensize(5)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()

t.penup()
t.goto(0, -200)
t.pendown()
t.pensize(1)
t.write("click ender to continue", font=("Arial", 25, "bold italic"), align="center")
round = input("Press Enter to Continue: ")
t.clear()


#Screen 2
screen.screensize(500,500)
screen.bgcolor("Blue")
t.penup()
t.goto(0, 200)
t.pendown()
t.write("My 1st and 2nd favorite foods", font=("Arial", 30, "bold italic"), align="center")

t.pencolor('white')
t.penup()
t.goto(250, -250)
t.pendown()
t.pensize(5)
t.fillcolor('brown')
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(-100, 120)
t.pendown()
t.write("pizza", font=("Arial", 25, "bold italic"), align="center")

t.penup()
t.goto(-150, 0)
t.pendown()
screen.addshape('pizza.gif')
t.shape("pizza.gif")
t.stamp()
t.shape('classic')

t.penup()
t.goto(100, 120)
t.pendown()
t.write("sushi", font=("Arial", 25, "bold italic"), align="center")

t.penup()
t.goto(200,0 )
t.pendown()
screen.addshape('sushi (1).gif')
t.shape("sushi (1).gif")
t.stamp()
t.shape('classic')
t.pencolor('black')

t.penup()
t.goto(0, -200)
t.pendown()
t.write("click ender to continue", font=("Arial", 25, "bold italic"), align="center")
round = input("Press Enter to Continue: ")
t.clear()







#page 3
screen.screensize(500,500)
screen.bgcolor("pink")
t.penup()
t.goto(0, 200)
t.pendown()
t.write("My 3rd favorite food and favorte movie", font=("Arial", 25, "bold italic"), align="center")

t.penup()
t.goto(150,-250)
t.pendown()
t.setheading(0)
t.fillcolor('blue')
t.begin_fill()
t.goto(250,-250)
t.goto(200,-150)
t.goto(150,-250)
t.end_fill()

t.pencolor('white')
t.penup()
t.goto(150, 120)
t.pendown()
t.write("BatMan Dark Knight", font=("Arial", 20, "bold italic"), align="center")

t.penup()
t.goto(100, 0)
t.pendown()
screen.addshape('batmaqn.gif')
t.shape("batmaqn.gif")
t.stamp()
t.shape('classic')


t.penup()
t.goto(-150, 120)
t.pendown()
t.write("chicken burritos", font=("Arial", 20, "bold italic"), align="center")

t.penup()
t.goto(-100, 0)
t.pendown()
screen.addshape('burrito.gif')
t.shape("burrito.gif")
t.stamp()
t.shape('classic')
t.pencolor('black')

t.penup()
t.goto(0, -150)
t.pendown()
t.write("click ender to continue", font=("Arial", 25, "bold italic"), align="center")
round = input("Press Enter to Continue: ")
t.clear()


#page 4
screen.screensize(500,500)
screen.bgcolor("Blue")
t.penup()
t.goto(0, 200)
t.pendown()
t.write("My favorite hobbies", font=("Arial", 40, "bold italic"), align="center")

t.speed(0)
t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('green')
t.pensize(8)
t.goto(-200,-100)
t.pensize(1)
t.pencolor('purple')
t.fillcolor('purple')
t.begin_fill()
t.penup()
t.goto(-200,0)
t.fillcolor('purple')
t.pendown()
t.circle(25)
t.setheading(90)
t.circle(25)
t.setheading(180)
t.circle(25)
t.setheading(270)
t.circle(25)
t.end_fill()

t.penup()
t.goto(-200,-15)
t.pendown()
t.begin_fill()
t.setheading(0)
t.fillcolor('yellow')
t.circle(15)
t.end_fill()

t.pencolor('white')
t.penup()
t.goto(100, 100)
t.pendown()
screen.addshape('controller.gif')
t.shape("controller.gif")
t.stamp()
t.shape('classic')

t.penup()
t.goto(-40, 100)
t.pendown()
t.write("gaming", font=("Arial", 25, "bold italic"), align="center")

t.penup()
t.goto(100, -100)
t.pendown()
screen.addshape('bat.gif')
t.shape("bat.gif")
t.stamp()
t.shape('classic')

t.penup()
t.goto(-40,-100)
t.pendown()
t.write("BaseBall", font=("Arial", 25, "bold italic"), align="center")

t.pencolor('black')
t.penup()
t.goto(0, -200)
t.pendown()
t.write("click ender to continue", font=("Arial", 25, "bold italic"), align="center")
round = input("Press Enter to Continue: ")
t.clear()

#page 5
screen.screensize(500,500)
screen.bgcolor("Aquamarine")

t.penup()
t.goto(0, 250)
t.pendown()
t.write("My others favorite hobbies and favorite sport", font=("Arial", 20, "bold italic"), align="center")

t.penup()
t.goto(-150, 150)
t.pendown()
screen.addshape('draw.gif')
t.shape("draw.gif")
t.stamp()
t.shape('classic')
t.penup()
t.goto(-150, 50)
t.pendown()
t.write("Drawling", font=("Arial", 30, "bold italic"), align="center")

t.fillcolor('green')
t.begin_fill()
t.pensize(5)
t.penup()
t.goto(-200,-200)
t.pendown()
t.goto(-250,-160)
t.goto(-190,-160)
t.goto(-240,-200)
t.goto(-220,-130)
t.goto(-200,-200)
t.end_fill()
t.penup()
t.goto(150, 50)
t.pendown()
t.write("Sleeping", font=("Arial", 40, "bold italic"), align="center")
t.penup()
t.goto(150, 150)
t.pendown()
screen.addshape('zzz.gif')
t.shape("zzz.gif")
t.stamp()
t.shape('classic')

t.penup()
t.goto(0, -230)
t.pendown()
t.write("Football", font=("Arial", 40, "bold italic"), align="center")
t.penup()
t.goto(0, -100)
t.pendown()
screen.addshape('football.gif')
t.shape("football.gif")
t.stamp()
t.shape('classic')

t.penup()
t.goto(0, -280)
t.pendown()
t.write("click ender to continue", font=("Arial", 25, "bold italic"), align="center")
round = input("Press Enter to Continue: ")
t.clear()



#end screen
screen.screensize(500,500)
screen.bgcolor("cyan")
t.penup()
t.goto(0, 200)
t.pendown()
t.write("The End", font=("Arial", 40, "bold italic"), align="center")

t.penup()
t.goto(0, -100)
t.pendown()
screen.addshape('booyeah.gif')
t.shape("booyeah.gif")
t.stamp()
t.shape('classic')
t.hideturtle()







































turtle.done()