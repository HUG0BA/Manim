from manim import *
import numpy as np


class SquareToCircle(Scene):
    def construct(self):
        square = Square(side_length=3)
        square.set_fill(BLUE, opacity=0.5)
        square.rotate(PI/4)

        circle = Circle(radius=3, color=ORANGE)
        circle.set_fill(ORANGE)

        self.wait(0.5)
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(circle))
        self.wait(1)

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity = 0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, RIGHT, buff=0.1)

        self.wait(0.5)
        self.play(Create(circle), Create(square))
        self.wait(0.5)

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(Transform(square, circle))
        self.play(square.animate.set_fill(PURPLE, opacity=0.5))

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_squre = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)

        self.play(
            left_square.animate.rotate(PI), 
            Rotate(right_squre, angle=PI),
            run_time = 2
        )
        self.wait()

class TwoTransforms(Scene):
    def construct(self):
        
        a = Circle()
        b = Square()
        c = Triangle()

        self.wait(1)
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))
        #self.transform()
        self.wait(3)
        
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))


class TransformCycle(Scene):
    def construct(self):
        a = Circle()
        t1 = Square()
        t2 = Triangle()

       
        self.wait()
        for t in [t1,t2]:
            self.play(Transform(a,t))

class PlotFunctions(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[-3, 3, 1],  # X-axis range (start, end, tick spacing)
            y_range=[-5, 5, 1],  # Y-axis range (start, end, tick spacing)
            axis_config={"color": BLUE},  # Axis color
        )

        # Labels for the axes
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        labels.move_to(ORIGIN)

        # Define functions to plot
        x_squared = axes.plot(lambda x: x**2, color=RED, x_range=[-3, 3])
        x_squared.move_to(ORIGIN)
        x_cubic = axes.plot(lambda x: x**3, color=GREEN, x_range=[-3, 3])
        x_cubic.move_to(ORIGIN)
        log_x = axes.plot(lambda x: np.log(x), color=YELLOW, x_range=[0.1, 3])  # log(x) is undefined for x <= 0
        log_x.move_to(ORIGIN)
        linear = axes.plot(lambda x: x, color=ORANGE, x_range=[-3, 3])
        linear.move_to(ORIGIN)
        exp = axes.plot(lambda x: np.exp(x), color=PURPLE, x_range=[-2, 1])
        exp.move_to(ORIGIN)
        sine = axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[-3, 3])
        sine.move_to(ORIGIN)

        # Add the plots and labels to the scene
        self.play(Create(axes), Write(labels), run_time= 3)
        self.play(Create(x_squared), run_time=1.5)
        self.play(Create(x_cubic), run_time=1.5)
        self.play(Create(log_x), run_time=1)
        self.wait(1)
        self.play(Create(linear), run_time = 1)
        self.play(Create(exp), run_time = 1.5)
        self.play(Create(sine), run_time = 2)

        # Add labels for each function


        self.wait()



class RoseCurve(Scene):
    def construct(self):
        # Set up polar axes
        axes = PolarPlane(
            size=6,
            radius_max=2,  # Adjust the max radius
            azimuth_step=15*DEGREES,  # Angle spacing between radial lines
        ).add_coordinates()
        axes.move_to(ORIGIN)  # Move the axes slightly up

        # Label for the axes
        axes_label = MathTex(r"r = a \cdot \cos(k\theta)").to_edge(DOWN)

        # Define the parameters for the rose curve
        a = 1  # Amplitude
        k = 7  # Number of petals

        # Define the rose curve in polar coordinates
        def rose_curve(theta):
            r = a * np.cos(k * theta)
            return axes.polar_to_point(r, theta)

        # Create the rose curve as a parametric function
        rose = ParametricFunction(
            rose_curve,
            t_range = np.array([0, TAU]),  # Full revolution for theta
            color=RED,
            stroke_width=3,
        )
        rose.move_to(ORIGIN)

        # Animation
        self.play(Create(axes), Write(axes_label), run_time = 2)
        self.wait(1)
        self.play(Create(rose), run_time=6)
        self.wait(2)




class SierpinskiTriangle(Scene):
    def construct(self):
        # Recursive function to draw a Sierpinski triangle
        def sierpinski(order, length):
            if order == 0:
                # Base case: return an equilateral triangle
                return Polygon(
                    [0, 0, 0], 
                    [length, 0, 0], 
                    [length / 2, np.sqrt(3) * length / 2, 0],
                    fill_opacity=1, color=BLUE
                )
            else:
                # Recursive case: split into 3 smaller triangles
                triangle1 = sierpinski(order - 1, length / 2).shift(LEFT * length / 4)
                triangle2 = sierpinski(order - 1, length / 2).shift(RIGHT * length / 4)
                triangle3 = sierpinski(order - 1, length / 2).shift(UP * np.sqrt(3) * length / 4)
                return VGroup(triangle1, triangle2, triangle3)

        # Initial triangle parameters
        order = 5  # Depth of recursion
        length = 8  # Size of the triangle

        # Create the Sierpinski triangle and center it
        fractal = sierpinski(order, length)
        fractal.move_to(ORIGIN)  # Move the entire fractal to the center of the screen

        # Animate the fractal
        self.play(Create(fractal), run_time=5)
        self.wait(2)



        