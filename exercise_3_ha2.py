# Robert Jerye

import turtle

def hilbert(curve_order, size, angle=90):
    if curve_order <= 0:
        return

    turtle.speed(0)
    turtle.pensize(2)

    def draw_hilbert(order, size, angle, parity):
        if order == 0:
            return

        turtle.left(parity * angle)
        draw_hilbert(order - 1, size, angle, -parity)

        turtle.forward(size)
        turtle.right(parity * angle)
        draw_hilbert(order - 1, size, angle, parity)

        turtle.forward(size)
        draw_hilbert(order - 1, size, angle, parity)

        turtle.right(parity * angle)
        turtle.forward(size)
        draw_hilbert(order - 1, size, angle, -parity)

        turtle.left(parity * angle)

    draw_hilbert(curve_order, size, angle, 1)

# Beispielaufruf
hilbert(curve_order=10, size=40)
turtle.done()
