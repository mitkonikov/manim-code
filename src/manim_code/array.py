from manim import *

class Array(VGroup):
    """
        Array Object

        Parameters
        ----------
        name:
            Name of the array. It's rendered when draw_array is called.

        size:
            Number of elements in the array.
    """

    def __init__(self, name: str, size: int, **config):
        VGroup.__init__(self)

        self.name = name
        self.nameObject = Tex(name, 
                **config["name_config"]
            )
        
        self.add(self.nameObject)
        
        self.size = size
        self.array = []
        
        if (config["values"]):
            self.array = config["values"]
        elif (config["memset"]):
            self.initial_values = config["memset"]
            for i in range(0, size):
                self.array.append(self.initial_values)

        self.pointers = { }
        self.pointers_text = { }

    def create_array(self, sq_size: int, text_size: int):
        """Creates the objects for each element in the array.
        """
        self.squares = []
        self.numbers = []
        self.sq_size = sq_size
        self.text_size = text_size
        
        # Create the squares and the numbers for each array element
        for i in range(0, self.size):
            shift = RIGHT * i * sq_size * 2
            centralize = (self.size // 2 + 1) * sq_size * LEFT

            sqr = Square().scale(sq_size).shift(shift + centralize)
            num = Tex(str(self.array[i])).scale(text_size).shift(shift + centralize)
            self.add(sqr)
            self.add(num)
            self.squares.append(sqr)
            self.numbers.append(num)

        self.array = {
            "squares": self.squares,
            "numbers": self.numbers
        }

        self.nameObject.scale(self.text_size).next_to(self.squares[0], LEFT * 2)

    def draw_array(self, play, **config):
        """Draws the name of the array and each element in order.
        """
        for i in range(0, self.size):
            if i == 0:
                play(
                    DrawBorderThenFill(self.squares[i]), 
                    Write(self.numbers[i]),
                    Write(self.nameObject),
                    **config
                )
            else:
                play(
                    DrawBorderThenFill(self.squares[i]), 
                    Write(self.numbers[i]),
                    **config
                )

    def pop(self, index: int, play, **config):
        """Animation when poping an element from the array

        Parameters
        ----------
        index : int
            The index of the element
        play : Callable
            Pass self.play as a callback
        """
    
        # Fade out the element with the given index
        play(
            FadeOutAndShift(self.squares[index], DOWN),
            FadeOutAndShift(self.numbers[index], DOWN),
            **config
        )

        diff = self.squares[index].get_x() - self.squares[index - 1].get_x()
        
        self.remove(self.squares[index])
        self.remove(self.numbers[index])
        self.squares.pop(index)
        self.numbers.pop(index)

        # Shift the other elements appropriately
        if (index != self.size - 1):
            anims = []
            for i in range(index, len(self.squares)):
                anims.append(self.squares[i].shift)
                anims.append(diff * LEFT)
                anims.append(self.numbers[i].shift)
                anims.append(diff * LEFT)
            
            play(*anims)

    def create_pointer(self, name: str, index: int):
        """Creates a pointer to an element in the array with given index.

        Parameters
        ----------
        name: Name of the pointer. By this name you can get the pointer later.
        index: Index of the element to which this pointer will point.

        Returns
        -------
        Vector
        """
        pointer = Vector(UP)
        pointer.next_to(self.squares[index], DOWN)
        self.pointers[name] = pointer
        self.add(pointer)
        return pointer

    def draw_pointer(self, name, play, **config):
        """Draws the pointer using ShowCreation Animation
        """
        play(ShowCreation(self.pointers[name], **config))

    def draw_pointer_name(self, name: str, text: str, play, **config):
        """Draws a text below the pointer

        Parameters
        ----------
        name: Name of the pointer
        index: Text to draw below the pointer
        play: Callback to the play function

        """
        self.pointers_text[name] = Tex("$" + text + "$").scale(self.text_size)
        self.pointers_text[name].next_to(self.pointers[name], DOWN)
        self.pointers_text[name].add_updater(lambda m: m.next_to(self.pointers[name], DOWN))
        play(Write(self.pointers_text[name], **config))

    def get_pointer(self, name: str):
        """Gets the pointer object by it's name
        """
        return self.pointers[name]

    def get_square(self, index: int):
        """Get the square object of an element with a given index
        """
        return self.squares[index]

    def indicate_at(self, index: int, play, **config):
        """Uses the Indicate animation on the element with the given index
        """
        play(
            Indicate(self.squares[index]),
            Indicate(self.numbers[index]),
            **config
        )