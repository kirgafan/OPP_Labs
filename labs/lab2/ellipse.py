from shape import Shape


class EllipseShape(Shape):
    def __init__(self):
        Shape.__init__(self)

    def Show(self, c):
        # два кути охоплюючого прямокутника, без заливки
        c.create_oval(self.x1, self.y1, self.x2, self.y2, outline="black", width=2)
