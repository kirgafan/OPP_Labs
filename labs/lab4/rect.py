from shape import Shape


class RectShape(Shape):
    def __init__(self):
        Shape.__init__(self)

    def Show(self, c, preview=False):
        fill = "yellow" if self.is_filled and not preview else ""
        dash = (4, 3) if preview else ()
        tags = "temp" if preview else ""
        c.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                           outline="black", fill=fill, width=2, dash=dash, tags=tags)
