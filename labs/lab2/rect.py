# lab2, прямокутник від центру, біла заливка

from shape import Shape


class RectShape(Shape):
    def __init__(self):
        Shape.__init__(self)

    def Show(self, c):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        dx = x2 - x1
        if dx < 0:
            dx = -dx
        dy = y2 - y1
        if dy < 0:
            dy = -dy
        # центр в x1 y1
        c.create_rectangle(x1 - dx, y1 - dy, x1 + dx, y1 + dy, outline="black", fill="white", width=2)
