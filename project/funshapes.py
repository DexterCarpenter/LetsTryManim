from manim import *

class LineDiamond(Scene):
    def construct(self):
        
        cam = Camera(
            pixel_height=100,
            pixel_width=100,
        )

        #self.camera = cam

        ax = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            x_length=10,
            y_length=10,
            tips=False,
            axis_config={"include_ticks": False, "color": WHITE},
        )

        #self.add(ax)
        
        numLines = 15

        linesQ1 = VGroup()

        for k in range(numLines+1):
            #print(k)
            #print(numLines-k)
            line = Line(start=[0, numLines-k, 0], end=[k, 0, 0])
            linesQ1.add(line)
        
        linesQ2 = linesQ1.copy().shift(LEFT*numLines).flip([0, 1, 0])
        linesQ3 = linesQ1.copy().shift(DOWN*numLines).shift(LEFT*numLines).flip([1, -1, 0])
        linesQ4 = linesQ1.copy().shift(DOWN*numLines).flip([1, 0, 0])
        linesQ1.flip([1, 1, 0])

        allLines = VGroup(linesQ1, linesQ2, linesQ3, linesQ4)

        allLines.scale(0.25)

        waitTime = 0
        runTime = 0.4
        self.play(Create(linesQ1), run_time=runTime)
        self.wait(waitTime)
        self.play(Create(linesQ2), run_time=runTime)
        self.wait(waitTime)
        self.play(Create(linesQ3), run_time=runTime)
        self.wait(waitTime)
        self.play(Create(linesQ4), run_time=runTime)
        self.wait(waitTime)

        self.wait(1)




