from manim import *
from manim.mobject.mobject import _AnimationBuilder

class Cell(VMobject):

    def __init__(self, value:int):
        super().__init__()
        self.add(Square(stroke_width=1).set_fill(BLACK, opacity=1.0).scale(0.55))
        self.add(Text(str(value), color=WHITE).scale(0.7))
        self.status = 0
        #self.scale(0.8)

    def animateFill(self, color:str) -> _AnimationBuilder:
        return self.submobjects[0].animate.set_fill(color)
        
    def getStatus(self) -> int:
        return self.status

    def setStatus(self, status:int):
        self.status=status

class CustomGrid(VMobject):

    def __init__(self, cellCount:int, width:int):
        super().__init__()
        self.cellMap : Dict[int, Cell] = {}

        for i in range(2,cellCount):
            col = ((i-1)%width)
            row = ((i-1)//width)
            self.cellMap[i] = Cell(i).move_to( RIGHT*col + DOWN*row + LEFT * 4 + UP*3)
            self.add(self.cellMap[i])

    
    def animateCellFill(self, cellIndeces: List[int], color: str) -> List[_AnimationBuilder]:
        animations : List[_AnimationBuilder] = []
        for i in cellIndeces:
            animations.append( self.cellMap[i].animateFill(color))
        return animations

    def getCellStatus(self, cellIndex: int) ->int:
        return self.cellMap[cellIndex].getStatus()

    def setCellStatus(self, cellIndex: int, status: int):
        self.cellMap[cellIndex].setStatus(status)
        
    def copyCell(self, cellIndex: int) -> Mobject:
        return self.cellMap[cellIndex].copy()