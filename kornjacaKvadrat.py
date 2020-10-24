
import turtle

window = turtle.Screen()
window.setup(500, 500)

jovan = turtle.RawTurtle(window)
jovan.shape ('turtle')
jovan.color('blue')


jovan.forward(50)
jovan.left(90)
jovan.forward(150)

jovan.left(90)
jovan.forward(50)

jovan.left(90)
jovan.forward(150)


window.exitonclick()