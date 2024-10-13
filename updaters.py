from manim import *
from numpy import *

class WHAT(Scene):
    def construct(self):
        def update_square(my_square, dt):
            my_square.shift(0.9 *dt * RIGHT)
            my_square.rotate(-0.75 *DEGREES)

        sq = Square()
        sq.set_fill(TEAL, 0.5)
        sq.to_edge(LEFT, buff=1)
        sq.rotate(45*DEGREES)

        sq.add_updater(update_square)
        self.add(sq)

        self.wait(10)

class BouncingBall(Scene):
    def construct(self):
        width = 12
        height = 6
        box = Rectangle(width=width, height=height)
        box.set_stroke(width=8)

        ball = Dot(radius=0.15)
        ball.vx, ball.vy = 0.05, 0.05

        def update_ball(b,dt):
            right_point = b.get_right()[0]
            left_point = b.get_left()[0]
            top_point = b.get_top()[1]
            bottom_point = b.get_bottom()[1]

            if right_point >= width/2 or left_point <= -width/2:
                b.vx *= -1
            
            if top_point >= height/2 or bottom_point <= -height/2:
                b.vy *= -1

            b.shift(b.vx * RIGHT + b.vy * UP )

        self.play(Create(ball), Create(box))
        ball.add_updater(update_ball)
        self.wait(10)


class NextToUpdater(Scene):
    def construct(self):
        def dot_position(mobject):
            mobject.set_value(dot.get_center()[0])
            mobject.next_to(dot)

        dot = Dot(RIGHT*3)
        label = DecimalNumber()
        label.add_updater(dot_position)
        self.add(dot, label)

        self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=linear))

class RosePattern(VMobject):
    def __init__(self, radius: float = 2, k: float = 3, **kwargs):
        
        self.radius = radius
        self.k = k
        super().__init__(**kwargs)
        
        step_size = 0.05
        theta = arange(0, TAU + step_size, step_size)

        points = [
            [
                radius * cos(k * t) * cos(t),
                radius * cos(k * t) * sin(t),
                0
            ]for t in theta
        ]

        self.set_points_smoothly(points)

class ShowingRosePattern(Scene):
    def construct(self):
        cs = [BLUE, WHITE, BLUE]
        rose = RosePattern(k = 10)
        rose.set_color_by_gradient(*cs)

        self.play(Create(rose), run_time=5)
        self.wait()

class AnimatingWithUpdateFunc(Scene):
    def construct(self):
        rose = get_rose_pattern(k = 0)
        rose.k = 0

        self.play(Create(rose))

        def update_pattern(pat, dt):
            pat.k += dt
            new_pat = get_rose_pattern(k=pat.k)
            pat.become(new_pat)

        rose.add_updater(update_pattern)
        self.wait(10)

class AnimatingWithValueTracker(Scene):
    def construct(self):
        track_k = ValueTracker(0)
        rose = get_rose_pattern(k=track_k.get_value())

        self.play(Create(rose))

        def update_pattern(pat):
            new_pat = get_rose_pattern(k=track_k.get_value())
            pat.become(new_pat)

        rose.add_updater(update_pattern)

        self.play(track_k.animate.set_value(10), run_time=5)

class AnimatingWithForLoop(Scene):
    def construct(self):
        rose = get_rose_pattern(k=0)
        self.play(Create(rose))

        k_increment = 0.01

        for k in arange(0, 10, k_increment):
            self.play(
                rose.animate.become(get_rose_pattern(k)),
                run_time = k_increment
            )

def get_rose_pattern(k: float, colors: list = [BLUE, WHITE, BLUE]):
    return RosePattern(k=k).set_color_by_gradient(*colors)

from manim import *

class RateFuncExample(Scene):
    def construct(self):
        x = VGroup()
        for k, v in rate_functions.__dict__.items():
            if "function" in str(v):
                if (
                    not k.startswith("__")
                    and not k.startswith("sqrt")
                    and not k.startswith("bezier")
                ):
                    try:
                        rate_func = v
                        plot = (
                            ParametricFunction(
                                lambda x: [x, rate_func(x), 0],
                                t_range=[0, 1, .01],
                                use_smoothing=False,
                                color=YELLOW,
                            )
                            .stretch_to_fit_width(1.5)
                            .stretch_to_fit_height(1)
                        )
                        plot_bg = SurroundingRectangle(plot).set_color(WHITE)
                        plot_title = (
                            Text(rate_func.__name__, weight=BOLD)
                            .scale(0.5)
                            .next_to(plot_bg, UP, buff=0.1)
                        )
                        x.add(VGroup(plot_bg, plot, plot_title))
                    except: # because functions `not_quite_there`, `function squish_rate_func` are not working.
                        pass
        x.arrange_in_grid(cols=8)
        x.height = config.frame_height
        x.width = config.frame_width
        x.move_to(ORIGIN).scale(0.95)
        self.add(x)