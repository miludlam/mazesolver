from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)

    # create test points
    pointA = Point(0, 0)
    pointB = Point(100, 0)
    pointC = Point(100, 100)
    pointD = Point(0, 100)

    # create test lines
    lineAtoB = Line(pointA, pointB)
    lineBtoC = Line(pointB, pointC)
    lineCtoD = Line(pointC, pointD)
    lineDtoA = Line(pointD, pointA)

    # draw lines
    win.draw_line(lineAtoB, "black")
    win.draw_line(lineBtoC, "black")
    win.draw_line(lineCtoD, "black")
    win.draw_line(lineDtoA, "black")

    win.wait_for_close()

if __name__ == "__main__":
    main()
