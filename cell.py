from line import Line
from point import Point

class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall)
        if self.has_right_wall:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall)
        if self.has_top_wall:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall)

    def draw_move(self, to_cell, undo=False):
        bg = "gray"
        if undo:
            bg = "red"

        midpoint1 = abs(self._x2 - self._x1) // 2
        x_mid1 = midpoint1 + self._x1
        y_mid1 = midpoint1 + self._y1

        midpoint2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_mid2 = midpoint2 + to_cell._x1
        y_mid2 = midpoint2 + to_cell._y1

        line = Line(Point(x_mid1, y_mid1), Point(x_mid2, y_mid2))
        self._win.draw_line(line, bg)
