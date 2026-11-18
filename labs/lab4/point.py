from shape import Shape


class PointShape(Shape):
    def __init__(self):
        Shape.__init__(self)

    def Show(self, c):
        r = 4
        c.create_oval(self.x1 - r, self.y1 - r, self.x1 + r, self.y1 + r, outline="black", fill="black")
