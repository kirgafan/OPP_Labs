from line import LineShape
from rect import RectShape


class CubeWireframe(LineShape, RectShape):
    def __init__(self):
        LineShape.__init__(self)

    def Show(self, c):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        RectShape.Show(self, c)
        ox = 36
        oy = -28
        self.x1 = x1 + ox
        self.y1 = y1 + oy
        self.x2 = x2 + ox
        self.y2 = y2 + oy
        RectShape.Show(self, c)
        edges = [
            (x1, y1, x1 + ox, y1 + oy),
            (x2, y1, x2 + ox, y1 + oy),
            (x1, y2, x1 + ox, y2 + oy),
            (x2, y2, x2 + ox, y2 + oy),
        ]
        for i in range(len(edges)):
            self.x1 = edges[i][0]
            self.y1 = edges[i][1]
            self.x2 = edges[i][2]
            self.y2 = edges[i][3]
            LineShape.Show(self, c)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
