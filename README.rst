Advanced Code Extensions
------------------------

This Manim extension allows you to quickly create arrays, assign elements, point to elements, push, pop and etc. It sits on top of the `Manim Community Edition <https://github.com/ManimCommunity/manim>`_.

Overview:
 - Array

In the works:
 - Code Highlighting by text search

TODO:
 - Make the array flexible i.e. each element with different Rectangles
 - 2D Array, maybe even 3D arrays
 - Stack
 - Tests

Array
~~~~~

The Array object has many functionalities. It creates a Rectangle and Tex object for each element, also it creates a Tex object for its name.

Example code:

 .. code-block:: python

    array = Array(
        "Array", 
        *range(6), # this is the array 
        name_config={"fill_color": WHITE}
    )
    array.create_array(sq_size=0.5, name_size=1.2)
    for anims in array.draw_array():
        self.play(anims, run_time=0.5)

Creating a pointer to an element in the array:

 .. code-block:: python

    array.create_pointer(index=2)
    self.play(array.draw_pointer(index=2), run_time=0.5)
    self.play(array.draw_pointer_name(index=2, text="Here", text_size=1.2))
    
    # get the pointer at index 2 and shift it to the square with index 4
    pointer = array.get_pointer(2)
    self.play(
        ApplyMethod(pointer.next_to, array.get_square(4), DOWN, aligned_edge=UP),
        run_time=0.5
    )
    self.play(*array.indicate_at(4), run_time=0.5)
    self.play(Indicate(pointer), run_time=0.5)

The array is a VGroup, so you can transform it as a whole.

 .. code-block:: python

    self.play(array.scale, 1.1, run_time=0.5)

Popping an element:

 .. code-block:: python

    pop_anims = list(array.pop(index=3))
    self.play(*pop_anims[:-1]) # pop the element
    self.wait()
    self.play(*pop_anims[-1:]) # shift the others
    self.wait()

Functions
^^^^^^^^^

create_array (sq_size: `int`, name_size: `int` = 1, `**kwargs`)
    Creates all the necessary objects with the given text and square size.

draw_array ()
    Returns the animations that draw the array on the screen. 

pop (index: `int`)
    Returns the animation of poping an element from the array. It deletes the objects associated with it, but not the pointers. It shifts all the other elements appropriately.

get_square (index: `int`)
    Gets the Square object of an element with the given index.

Pointers to elements
^^^^^^^^^^^^^^^^^^^^

create_pointer (index: `int`)
    Creates a pointer to an element with the given `index`. The pointer is identified (mostly?) by the Square above it

draw_pointer(index: `int`)
    Returns the animation that draws the pointer.

draw_pointer_name(index: `int`, text: `str`, text_size: `int`)
    Draw a `text` below a pointer of the square of that index.

get_pointer(index: `int`)
    Gets the pointer's Vector object.

----------

Contributing
~~~~~~~~~~~~

This is a fairly small project, so I think there are many of you guys who can easily contribute to it! Feel free to contribute and suggest new features! The plans for the future are to make the array much more flexible and create different representations, such as 2D and 3D arrays, stacks, etc.
