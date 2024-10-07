from manim import *

class ToyExample(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)

        self.add(orange_square)
        self.play(ReplacementTransform(orange_square, blue_circle, run_time=3))
        
        small_dot = Dot()
        small_dot.add_updater(lambda mob: mob.next_to(blue_circle, DOWN))

        self.play(Create(small_dot))
        self.play(blue_circle.animate.shift(RIGHT))
        self.wait()
        self.play(FadeOut(blue_circle, small_dot))


class VMObjectsDemo(Scene):
    def construct(self):
        plane = NumberPlane()
        my_vmobject = VMobject(color=GREEN)
        my_vmobject.points = [
            np.array([-2, -1, 0]), #start of first curve
            np.array([-3,1, 0]),
            np.array([0, 3, 0]),
            np.array([1, 3, 0]), #end of first curve
            np.array([1, 3, 0]), #start of second curve
            np.array([0 ,1, 0]),
            np.array([4, 3, 0]),
            np.array([4, -2, 0])
        ]

        handles = [
            Dot(point, color=RED) for point in
            [[-3, 1, 0], [0, 3, 0], [0, 1, 0], [4, 3, 0]]
        ]

        handle_lines = [
            Line(
                my_vmobject.points[ind],
                my_vmobject.points[ind+1],
                color=RED,
                stroke_width=2
            ) for ind in range(0, len(my_vmobject.points), 2)
        ]

        

        self.add(plane, *handles, *handle_lines, my_vmobject)
