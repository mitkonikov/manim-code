from manim.animation.creation import DrawBorderThenFill, ShowCreation, Write
from manim.animation.fading import FadeOutAndShift
from manim.animation.indication import Indicate
from manim.animation.transform import ApplyMethod, MoveToTarget
from manim.constants import DOWN, LEFT, RIGHT, UP
from manim.mobject.geometry import Rectangle, Square, Vector
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
        self.pointers = dict()
        self.pointer_texts = dict()

    def create_array(self, sq_size: int, name_size=1, **kwargs):
        """Creates the objects for each element in the array.
        """
        # TODO: Should this be expected as part of __init__?
        self.squares = VGroup()
        self.elements = VGroup()

        # Create the squares and the numbers for each array element
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
        # I think it's better style for this method to simply return the animations
        # rather than play them, since the rendering of the scene feels more a part
        # of what a Scene is rather than an Array
        all_anims = list(
            [DrawBorderThenFill(square), Write(element)]
            for square, element in zip(self.squares, self.elements)
        )
        all_anims[0].append(Write(self.array_name))
        for anims in all_anims:
            yield anims

    def pop(self, index: int):
        """Animation when poping an element from the array
        Parameters
        ----------
        index : int
            The index of the element
        """
    
        # Fade out the element with the given index
        yield FadeOutAndShift(self.squares[index], DOWN)
        yield FadeOutAndShift(self.elements[index], DOWN)

        target = self.copy()

        square = target.squares[index]
        element = target.elements[index]

        # Noticed a bit of a logical flaw here
        self -= square
        self -= element
        self.squares -= square
        self.elements -= element
        # del square
        # del element

        #! There's a bit of a paradox here
        yield ApplyMethod(
            self.squares[index + 1:].move_to, 
            target.squares[index:-1]
        )

    def create_pointer(self, index: int):
        """Creates a pointer to an element in the array with given index.

        Parameters
        ----------
        index: Index of the element to which this pointer will point.

        Returns
        -------
        Vector
        """
        # Let the square above the pointer access the pointer itself
        # eg. array.squares[2].pointer
        pointer = Vector(direction=UP)
        pointer.next_to(self.squares[index].get_bottom(),
                        direction=DOWN, aligned_edge=UP)
        # self.squares[index].add(pointer)
        self.pointers[self.squares[index]] = pointer
        self.add(pointer)

    def draw_pointer(self, index):
        """Returns ShowCreation animation for the pointer with the square's index
        """
        return ShowCreation(self.pointers[self.squares[index]])

    def draw_pointer_name(self, index: int, text: str, text_size: int):
        """Draws a text below the pointer

        Parameters
        ----------
        index: Index of the array to acquire the pointer
        text: Text to draw below the pointer
        play: play function from the scene

        """
        index = self.squares[index]
        item = Tex(f"${text}$").scale(text_size)
        item.next_to(self.pointers[index], DOWN)
        # Again, slightly better than the updater
        self.pointers[index].add(item)
        self.pointer_texts[index] = item
        self.add(item)
        return Write(item)

    def get_pointer(self, index: int):
        """Gets the pointer object by the index of the square
        """
        return self.pointers[self.squares[index]]

    def get_square(self, index: int):
        """Get the square object of an element with a given index
        """
        return self.squares[index]

    def indicate_at(self, index: int):
        """Uses the Indicate animation on the element with the given index
        """
        yield Indicate(self.squares[index])
        yield Indicate(self.elements[index])
