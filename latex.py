from manim import *

class LaTeXSubstrings(Scene):
    def construct(self):
        text = MathTex(r"\int_a^b f'(x) dx = f(b) - f(a)")
        self.play(AddTextLetterByLetter(text), run_time=10)