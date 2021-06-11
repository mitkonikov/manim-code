from manim.animation.creation import DrawBorderThenFill, Write
from manim.animation.fading import FadeOut
from manim.animation.indication import Indicate
from manim.animation.transform import ApplyMethod, MoveToTarget, ReplacementTransform, Transform
from manim.constants import DOWN, LEFT, RIGHT, UP
from manim.mobject.geometry import Square
from manim.mobject.svg.tex_mobject import Tex
from manim.mobject.types.vectorized_mobject import VGroup

class Array(VGroup):
    """
        Array Object

        Parameters
        ----------
        name:
            Name of the array. It's rendered when draw_array is called.

        values:
            The elements to be contained in the array

        name_config:
            Additional configuration to the Tex object that is the name
            of the array

        kwargs:
            Additional configurations to the object as inheriting from
            VMobject
    """

    def __init__(self, name: str, *values, name_config=dict(), **kwargs):
        self.array_name = Tex(
            name,
            **name_config
        )

        super().__init__(name=name, **kwargs)

        self.add(self.array_name)
        self.array = values
        self.squares = VGroup()
        self.elements = VGroup()

    def create_array(self, sq_size: int, name_size=1, **kwargs):
        """Creates the objects for each element in the array.
        """
        self.create_array_args = kwargs
        self.sq_size = sq_size

        for val in self.array:
            element = Tex(
                # None in the val for an empty box
                "" if val is None else f"{val}",
                **kwargs.pop("value_config", {})
            )
            # ? The notion of sq_size would be in comparison to the default size
            # ? instead of the unit square. Oh well
            square = Square(**kwargs.pop("square_config", {})).scale(sq_size)
            element.set_height(square.get_height() * 0.65)
            # Merely for the values to stay inside the squares
            # I could use an updater for this, but lazy reliance on present implementation
            square.add(element)
            self.squares.add(square)
            self.elements.add(element)

        self.squares.arrange(buff=0)

        self.add(*self.squares)
        self.add(*self.elements)

        self.array_name.scale(name_size)
        self.array_name.next_to(self.squares.get_left(),
                                direction=LEFT, aligned_edge=RIGHT)

    def draw_array(self):
        """Draws the name of the array and each element in order.
        """
        # Here we are just giving the square animation, because the element itself
        # is inside the square object, so it would be rendered as well.
        all_anims = [Write(self.array_name)]
        all_anims.extend(list(
            DrawBorderThenFill(square)
            for square in self.squares
        ))
        return all_anims

    def pop(self, index: int):
        """Animation when poping an element from the array
        Parameters
        ----------
        index : int
            The index of the element
        """
    
        # Fade out the element with the given index
        yield FadeOut(self.squares[index], shift = DOWN)
        yield FadeOut(self.elements[index], shift = DOWN)

        target = self.copy()

        square = target.squares[index]
        element = target.elements[index]

        # Noticed a bit of a logical flaw here
        self.remove(square)
        self.remove(element)
        self.squares.remove(square)
        self.elements.remove(element)
        # del square
        # del element

        #! There's a bit of a paradox here
        yield ApplyMethod(
            self.squares[index + 1:].move_to, 
            target.squares[index:-1]
        )

    def get_square(self, index: int):
        """Get the square object of an element with a given index
        """
        return self.squares[index]

    def indicate_at(self, index: int):
        """Uses the Indicate animation on the element with the given index
        """
        yield Indicate(self.squares[index])
        yield Indicate(self.elements[index])

    def at(self, index, value):
        """Changest the value at a given index"""
        ### TODO:   Fix this function
        ###         Right now, we don't change the square
        ###         Also, the MoveToTarget animation is not smooth
        
        element = Tex(
            # None in the val for an empty box
            "" if value is None else f"{value}",
            **self.create_array_args.pop("value_config", {})
        )

        oldElement = self.elements[index]
        
        element.set_height(self.squares[index].get_height() * 0.65)
        element.move_to(oldElement)

        oldElement.target = element
        
        return [
            MoveToTarget(oldElement)
        ]

    def connect_pointer(self, pointer):
        self.add(pointer)