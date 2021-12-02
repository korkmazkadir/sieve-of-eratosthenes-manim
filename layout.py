from manim import *

class GridLayout(Mobject):
    
    def __init__(self, width:int, height:int, header:str="" ,showGrid: bool = True):
        super().__init__()
        self.dotMap : Dict[int, Dot] = {}

        offsetX = -width / 2
        offsetY = height / 2

        color = WHITE
        if not showGrid:
            color = BLACK

        if len(header)>0:
            t= Text(header,color=WHITE, font="Open Sans", slant=ITALIC)
            t.move_to( (UP+offsetY + 0.2) + (RIGHT * offsetX * 1.4 ))
            self.add(t)

        for y in range(0,height):
            for x in range(0, width):
                dot = Dot([x + offsetX, -y + offsetY, 0], color=color)
                self.dotMap[x + y*width] = dot
                self.add(dot)

    def getDot(self, index:int) ->Dot:
        return self.dotMap[index]
