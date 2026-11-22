from line import LineShape
from ellipse import EllipseShape


class LineWithCircles(LineShape, EllipseShape):
    def __init__(self):
        LineShape.__init__(self)

    def Show(self, c, preview=False):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        LineShape.Show(self, c, preview)
        r = 8
        # ліве коло
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + r
        self.y2 = y1 + r
        EllipseShape.Show(self, c, preview)
        # праве коло, координати повернути назад
        self.x1 = x2
        self.y1 = y2
        self.x2 = x2 + r
        self.y2 = y2 + r
        EllipseShape.Show(self, c, preview)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
