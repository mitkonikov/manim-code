from manim.mobject.types.vectorized_mobject import VGroup
from manim.mobject.geometry import Vector
from manim.animation.creation import Create, Write
from manim.mobject.svg.text_mobject import Text
from manim.constants import DOWN, LEFT, RIGHT, UP
from numpy import array_equal

class Pointer(VGroup):
    def __init__(self, direction):
        super().__init__()
        self.arrow = Vector(direction)
        self.add(self.arrow)

    def draw(self):
        return Create(self.arrow)

class TextPointer(Pointer):
    def __init__(self, text, text_size = 1, direction = UP):
        super().__init__(direction)
        self.text = Text(text).scale(text_size)

        # Position the text
        if array_equal(direction, UP):
            self.text.next_to(self.arrow, DOWN)
        else:
            self.text.next_to(self.arrow, UP)

        self.add(self.text)

    def draw(self):
        """Returns list of [Create(arrow), Write(text)] animations""" 
        return [Create(self.arrow), Write(self.text)]