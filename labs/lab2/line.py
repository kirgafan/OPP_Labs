from shape import Shape


class LineShape(Shape):
    def __init__(self):
        Shape.__init__(self)

    def Show(self, c):
        c.create_line(self.x1, self.y1, self.x2, self.y2, fill="black", width=2)
