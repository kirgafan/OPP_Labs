from shape import Shape


class PointShape(Shape):
    def __init__(self):
        Shape.__init__(self)

    def Show(self, c, preview=False):
        r = 4
        fill = "" if preview else "black"
        dash = (4, 3) if preview else ()
        tags = "temp" if preview else ""
        c.create_oval(self.x1 - r, self.y1 - r, self.x1 + r, self.y1 + r,
                      outline="black", fill=fill, dash=dash, tags=tags)
