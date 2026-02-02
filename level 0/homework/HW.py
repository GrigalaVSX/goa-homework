from turtle import *
#paint a house

#drawing a square
speed(20)


width(5)
forward(400)


left(90)
forward(200)

left(90)
forward(400)

left(90)
forward(200)

#second floor
penup()
goto(200,200)

pendown()

backward(100)

right(90)

backward(400)

left(90)
forward(100)

right(90)
forward(200)

penup()
goto(500,200)

pendown()
left(90)
forward(200)

left(90)
forward(100)

left(90)
forward(200)

#making a balcony
penup()
goto(0,200)

pendown()
forward(30)

right(90)
forward(5)

right(90)
forward(30)

#making a garage
right(80)
forward(250)

left(80)
forward(157)

left(90)
forward(246)

backward(26)

left(90)
forward(157)

left(90)
forward(194)

left(90)
forward(157)

#making a door
begin_fill()
penup()
goto(100,0)

pendown()
backward(120)

left(90)
forward(70)

right(90)
forward(120)
end_fill()

#making a window
penup()
goto(250,70)

pendown()
backward(100)

left(90)
forward(100)

right(90)
forward(100)

right(90)
forward(100)

backward(50)
right(90)
forward(100)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(100)

#making a second window on the second floor
penup()
goto(340,230)
pendown()

forward(100)

left(90)
forward(40)

left(90)
forward(100)

left(90)
forward(40)

left(90)
forward(50)

left(90)
forward(40)

penup()
goto(340,250)

pendown()
right(90)
forward(100)

#making a second door an entry to the balcony

penup()
goto(200,200)
pendown()

left(90)
forward(50)

right(90)
forward(10)

right(90)
forward(50)



exitonclick()







