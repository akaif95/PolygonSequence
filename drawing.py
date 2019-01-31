'''
Author: <Ali Kaif>
Date: <February 2nd, 2018>
Class: ISTA 130
Section Leader: <Sebastian>

Description:
<This program is designed to create a drawing of my choice by creating a
shapes function. I call the drawing, Polygon Palooza Swirl>
'''

import turtle


def shape(fun_animal, length):
    #creates a heptagon
    fun_animal.forward(length)
    fun_animal.left(51.43)
    fun_animal.forward(length)
    fun_animal.left(51.43)
    fun_animal.forward(length)
    fun_animal.left(51.43)
    fun_animal.forward(length)
    fun_animal.left(51.43)
    fun_animal.forward(length)
    fun_animal.left(51.43)
    fun_animal.forward(length)
    fun_animal.left(51.43)
    fun_animal.forward(length)
    return None

def triangle(fun_animal, length):
    #draws a 3 sided polygon, a triangle
    fun_animal.forward(length)
    fun_animal.left(120)
    fun_animal.forward(length)
    fun_animal.right(240)
    fun_animal.forward(length)
    return None
   

def square(fun_animal, length):
    #draws a 4 sided polygon, a square
    fun_animal.forward(length)
    fun_animal.left(90)
    fun_animal.forward(length)
    fun_animal.left(90)
    fun_animal.forward(length)
    fun_animal.left(90)
    fun_animal.forward(length)
    return None

def pentagon(fun_animal, length):
    #draws a 5 sided polygon, a pentagon
    fun_animal.forward(length)
    fun_animal.left(72)
    fun_animal.forward(length)
    fun_animal.left(72)
    fun_animal.forward(length)
    fun_animal.left(72)
    fun_animal.forward(length)
    fun_animal.left(72)
    fun_animal.forward(length)
    fun_animal.left(72)
    return None


def hexagon(fun_animal, length):
    #draws a 6 sided polygon, a hexagon
    fun_animal.forward(length)
    fun_animal.left(60)
    fun_animal.forward(length)
    fun_animal.left(60)
    fun_animal.forward(length)
    fun_animal.left(60)
    fun_animal.forward(length)
    fun_animal.left(60)
    fun_animal.forward(length)
    fun_animal.left(60)
    fun_animal.forward(length)
    return None

def octagon(fun_animal, length):
    #draws a 8 sided polygon, an octagon
    fun_animal.forward(length)
    fun_animal.left(45)
    fun_animal.forward(length)
    fun_animal.left(45)
    fun_animal.forward(length)
    fun_animal.left(45)
    fun_animal.forward(length)
    fun_animal.left(45)
    fun_animal.forward(length)
    fun_animal.left(45)
    fun_animal.forward(length)
    fun_animal.left(45)
    fun_animal.forward(length)
    fun_animal.left(45)
    fun_animal.forward(length)
    return None

def nonagon(fun_animal, length):
    #draws a 9 sided polygon, a nonagon
    fun_animal.forward(length)
    fun_animal.left(40)
    fun_animal.forward(length)
    fun_animal.left(40)
    fun_animal.forward(length)
    fun_animal.left(40)
    fun_animal.forward(length)
    fun_animal.left(40)
    fun_animal.forward(length)
    fun_animal.left(40)
    fun_animal.forward(length)
    fun_animal.left(40)
    fun_animal.forward(length)
    fun_animal.left(40)
    fun_animal.forward(length)
    fun_animal.left(40)
    fun_animal.forward(length)
    fun_animal.left(40)
    return None

def decagon(fun_animal, length):
    #draws a 10 sided polygon, a decagon
    fun_animal.forward(length)
    fun_animal.left(36)
    fun_animal.forward(length)
    fun_animal.left(36)
    fun_animal.forward(length)
    fun_animal.left(36)
    fun_animal.forward(length)
    fun_animal.left(36)
    fun_animal.forward(length)
    fun_animal.left(36)
    fun_animal.forward(length)
    fun_animal.left(36)
    fun_animal.forward(length)
    fun_animal.left(36)
    fun_animal.forward(length)
    fun_animal.left(36)
    fun_animal.forward(length)
    fun_animal.left(36)
    fun_animal.forward(length)
    return None

def hendecagon(fun_animal, length):
    #draws a 11 sided polygon an undecagon
    fun_animal.forward(length)
    fun_animal.left(33)
    fun_animal.forward(length)
    fun_animal.left(33)
    fun_animal.forward(length)
    fun_animal.left(33)
    fun_animal.forward(length)
    fun_animal.left(33)
    fun_animal.forward(length)
    fun_animal.left(33)
    fun_animal.forward(length)
    fun_animal.left(33)
    fun_animal.forward(length)
    fun_animal.left(33)
    fun_animal.forward(length)
    fun_animal.left(33)
    fun_animal.forward(length)
    fun_animal.left(33)
    fun_animal.forward(length)
    fun_animal.left(33)
    fun_animal.forward(length)
    return None

def dodecagon(fun_animal, length):
    #draws a 12 sided polygon, a dodecagon
    fun_animal.forward(length)
    fun_animal.left(30)
    fun_animal.forward(length)
    fun_animal.left(30)
    fun_animal.forward(length)
    fun_animal.left(30)
    fun_animal.forward(length)
    fun_animal.left(30)
    fun_animal.forward(length)
    fun_animal.left(30)
    fun_animal.forward(length)
    fun_animal.left(30)
    fun_animal.forward(length)
    fun_animal.left(30)
    fun_animal.forward(length)
    fun_animal.left(30)
    fun_animal.forward(length)
    fun_animal.left(30)
    fun_animal.forward(length)
    fun_animal.left(30)
    fun_animal.forward(length)
    fun_animal.left(30)
    fun_animal.forward(length)
    return None

def triskaidecagon(fun_animal, length):
    #draws a 13 sided polygon, a triskedecagon
    fun_animal.forward(length)
    fun_animal.left(27.69)
    fun_animal.forward(length)
    fun_animal.left(27.69)
    fun_animal.forward(length)
    fun_animal.left(27.69)
    fun_animal.forward(length)
    fun_animal.left(27.69)
    fun_animal.forward(length)
    fun_animal.left(27.69)
    fun_animal.forward(length)
    fun_animal.left(27.69)
    fun_animal.forward(length)
    fun_animal.left(27.69)
    fun_animal.forward(length)
    fun_animal.left(27.69)
    fun_animal.forward(length)
    fun_animal.left(27.69)
    fun_animal.forward(length)
    fun_animal.left(27.69)
    fun_animal.forward(length)
    fun_animal.left(27.69)
    fun_animal.forward(length)
    fun_animal.left(27.69)
    fun_animal.forward(length)
    return None
    



#==========================================================
def main():
    '''
    This program draws a funky picture of geometric shapes from
    a triangle all the way up to a triskadecagon. All shapes will
    use a shade of red for the pencolor and be following a swirling
    pattern when drawing all 13 shapes.
    '''
    # sets up initial drawing setting for the picture
    fun_animal = turtle.Turtle()
    fun_animal.pensize(10)
    fun_animal.shape('turtle')
    fun_animal.speed(0)

   
    #Draws out all the polygons from 3 -sided to 13-sided
    #Notice how it follows a certain swirling pattern

    fun_animal.pencolor("red")
    triangle(fun_animal, 100)

    fun_animal.pencolor("red2")
    square(fun_animal, 100)

    fun_animal.pencolor("indian red4")
    pentagon(fun_animal, 100)

    fun_animal.pencolor("indian red2")
    hexagon(fun_animal, 100)

    fun_animal.pencolor("indian red3")
    shape(fun_animal, 100)

    fun_animal.pencolor("red3")
    octagon(fun_animal, 100)

    fun_animal.pencolor("red4")
    nonagon(fun_animal, 100)

    fun_animal.pencolor("lavender")
    decagon(fun_animal, 100)

    fun_animal.pencolor("pink")
    hendecagon(fun_animal, 100)

    fun_animal.pencolor("indian red")
    dodecagon(fun_animal, 100)

    fun_animal.pencolor("indian red2")
    triskaidecagon(fun_animal, 100)

    
    




    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open but closes out when clicked on

if __name__ == '__main__':
    main()
