# прямокутник по двох кутах, жовта заливка

from shape import Shape


class RectShape(Shape):
    def __init__(self):
        Shape.__init__(self)

    def Show(self, c):
        c.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="black", fill="yellow", width=2)
