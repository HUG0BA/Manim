from manim import *
import numpy as np

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(2)
        self.remove(circle, square, triangle)
        self.wait(2)

class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # place the circle two units left from the origin (the origin if the reference point)
        circle.move_to(LEFT * 2)
        # place the square to the left of the circle (the mobject if the reference point)
        square.next_to(circle, LEFT )   
        # align the left border of the triangle to the left border of the circle
        triangle.align_to(circle, DOWN)

        self.wait(1)
        self.add(circle, square, triangle)
        self.wait(1)

class MObjectStyling(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.wait(0.5)
        self.add(circle, square, triangle)
        self.wait(1)

class MObjectZOrder(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.wait(0.5)
        self.add(triangle, square, circle)
        self.wait(1)

class SomeAnimations(Scene):
    def construct(self):
        square = Square()

        self.wait(0.5)
        self.play(FadeIn(square))
        self.play(Rotate(square, PI/4))
        self.play(FadeOut(square))
        self.wait(1)

class AnimateExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity = 1.0)
        self.add(square)

        self.wait()
        self.play(square.animate.set_fill(WHITE))
        self.wait(1)

        self.play(square.animate.shift(UP).rotate(PI/3))
        self.wait()

#Cusstom Animation
#__________________________________________________________________________________________
class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs):
        super().__init__(number, kwargs)

        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)

class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add to the scene
        number = DecimalNumber().set_color(WHITE).scale(5)

        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)

        self.wait()

#_____________________________________________________________________________________________

class MobjectExample(Scene):
    def construct(self):
        p1 = [-1, -1, 0]
        p2 = [1, -1, 0]
        p3 = [1, 1, 0]
        p4 = [-1, 1, 0]

        a = Line(p1, p2).append_points(Line(p2, p3).points).append_points(Line(p3, p4).points)

        point_start = a.get_start()
        point_end = a.get_end()
        point_center = a.get_center()   
        self.add(
            Text(
            f"a.get_start() = {np.round(point_start, 2).tolist()}",
            font_size=24)
            .to_edge(UR)
            .set_color(YELLOW)
        )
        self.add(
            Text(
            f"a.get_end() = {np.round(point_end, 2).tolist()}" ,
            font_size=24)
            .next_to(self.mobjects[-1], DOWN)
            .set_color(RED)
        )
        self.add(
            Text(
                f"a.get_center() = {np.round(point_center, 2).tolist()}",
                font_size=24)
                .next_to(self.mobjects[-1], DOWN)
                .set_color(BLUE)
        )

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)

class ExampleTransform(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1 = Square().set_color(RED)
        m2 = Rectangle().set_color(RED).rotate(0.2)
        self.play(Transform(m1, m2))

class ExampleRotation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a = Square().set_color(BLUE).shift(RIGHT)
        m2b = Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points
        points = np.roll(points, int(len(points)/4), axis = 0)
        m2a.points = points

        self.wait()
        self.play(Transform(m1a, m1b), run_time=1)
        self.wait()
        self.play(Transform(m2a, m2b), runt_time=1)
        self.wait()


class ExampleRotationCopied(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a = Square().set_color(BLUE).shift(RIGHT)
        m2b = Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points
        points = np.roll(points, int(len(points)/4), axis=0)
        m2a.points = points

        self.play(Transform(m1a,m1b),Transform(m2a,m2b), run_time=1)
    
