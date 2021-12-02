
from manim import *
from grid import *
from layout import *

class Title(Scene):
    def construct(self):
        title = Text("Sieve of Eratosthenes Algoritması ile Asal Sayıları Hesaplama", color=WHITE, font="Noto Sans")
        title.scale(0.75)
        title.to_edge(UP)

        g = VGroup()
        g += Text("Sift the two's and sift the three's:",color=YELLOW_A, font="Open Sans", slant=ITALIC)
        g += Text("The Sieve of Eratosthenes.",color=YELLOW_A, font="Open Sans", slant=ITALIC)
        g += Text("When the multiples sublime,",color=YELLOW_A, font="Open Sans", slant=ITALIC)
        g += Text("The numbers that remain are Prime.",color=YELLOW_A, font="Open Sans", slant=ITALIC)
        g.arrange(DOWN).scale(0.6)

        self.play(Write(title))
        self.wait(duration=1)
        self.play(Write(g))
        self.wait(duration=3)

        self.play(FadeOut(title), FadeOut(g))
        self.wait(duration=1)

class Intro(Scene):
    def construct(self):
        g1 = VGroup()
        g1+= Text("Asal sayılar 1'den ve kendinden başka",color=YELLOW_A, font="Open Sans", slant=ITALIC)
        g1+= Text("böleni olmayan sayma sayılardır.",color=YELLOW_A, font="Open Sans", slant=ITALIC)
        g1.arrange(DOWN).scale(0.6)

        self.play(Write(g1))
        self.wait(duration=3)
        self.play(Unwrite(g1))
        self.wait(duration=1)
    
        g2 = VGroup()
        g2 += Text("Sieve of Eratosthenes Algoritmasını kullanarak,",color=YELLOW_A, font="Open Sans", slant=ITALIC)
        g2 += Text("verilen bir sayıya kadar olan bütün asal sayıları hesaplayabiliriz.",color=YELLOW_A, font="Open Sans", slant=ITALIC)
        g2.arrange(DOWN).scale(0.6)

        self.play(Write(g2))
        self.wait(duration=3)
        self.play(Unwrite(g2))
        self.wait(duration=1)


class Credits(Scene):
    def construct(self):
        g1 = VGroup()
        g1+= Text("Bu video Manim Community v0.12.0",color=YELLOW_A, font="Open Sans", slant=ITALIC)
        g1+= Text("Kullanılarak geliştirildi.",color=YELLOW_A, font="Open Sans", slant=ITALIC)
        g1.arrange(DOWN).scale(0.6)

        self.play(Write(g1))
        self.wait(duration=3)
        self.play(Unwrite(g1))
        self.wait(duration=1)
    
        g2 = VGroup()
        g2 += Text("Son.",color=YELLOW_A, font="Open Sans", slant=ITALIC)
        g2 += Text("",color=YELLOW_A, font="Open Sans", slant=ITALIC)
        g2.arrange(DOWN)

        self.play(Write(g2))
        self.wait(duration=3)
        self.play(Unwrite(g2))
        self.wait(duration=1)


class Primes(Scene):

    def construct(self):
        grid = CustomGrid(121, 10)
        grid.move_to(LEFT*2)
        grid.scale(0.5)

        layout = GridLayout(6, 5, "Asal Sayılar", showGrid=False)
        layout.scale(0.6)
        layout.move_to(RIGHT*4)

        self.add(grid, layout)
        self.play(Create(grid), run_time=4)
        self.wait(duration=3)

        primeIndex = 0
        for i in range(2, 121):
            if grid.getCellStatus(i) == 0:
                self.play( *grid.animateCellFill([i], PURPLE), runtime=1.5)
                self.wait(duration=0.5)
                prime = grid.copyCell(i)
                self.play(prime.animate.move_to(layout.getDot(primeIndex))) 
                primeIndex+=1
                cellsToMark = []
                for j in range(i*2,121,i):
                    if grid.getCellStatus(j) == 0:
                        cellsToMark.append(j)
                        grid.setCellStatus(j, 1)
                if len(cellsToMark) >0:
                    self.play(*grid.animateCellFill( cellsToMark,RED))

        self.wait(duration=5)

        
class Grid(Scene):

    def construct(self):
        
        layout = GridLayout(6, 5, "Asal Sayılar", showGrid=True)
        layout.scale(0.8)

        self.add(layout)
        self.wait(duration=5)