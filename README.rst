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

    arr = [0, 1, 2, 3, 4, 5]

    arr_obj = Array("array:", len(arr), values = arr, name_config = {
        "fill_color": WHITE
    })

    arr_obj.create_array(sq_size = 0.5, text_size = 1.2)
    arr_obj.draw_array(self.play, run_time = 0.5)
    
    # create i pointer
    arr_obj.create_pointer("i", 2)
    arr_obj.draw_pointer("i", self.play, run_time = 0.5)
    arr_obj.draw_pointer_name("i", "i", self.play, run_time = 0.5)
    
    # this gets the pointer but not the name object
    pointer = arr_obj.get_pointer("i")
    # while shifting the pointer to specific square
    # it shifts the name also
    self.play(
        pointer.next_to, arr_obj.get_square(4), DOWN, 
        run_time = 0.5
    )
    
    arr_obj.indicate_at(4, self.play, run_time = 0.5)
    self.play(Indicate(arr_obj.get_pointer("i"), run_time = 0.5))
    self.play(arr_obj.scale, 1.1, run_time = 0.5)

    # pop the element with index 3
    arr_obj.pop(3, self.play)

    self.wait(1)

Functions
^^^^^^^^^

create_array (sq_size: `int`, text_size: `int`)
    Creates all the necessary objects with the given text and square size.

draw_array (play, `**config`)
    Draws the array on the screen. You need to pass the self.play function, so the array object can call it.

pop (index: `int`, play, `**config`)
    Animation of poping an element from the array. It deletes the objects associated with it, but not the pointers. It shifts all the other elements appropriately.

get_square (index: `int`)
    Gets the Square object of an element with the given index.

Pointers to elements
^^^^^^^^^^^^^^^^^^^^

create_pointer (name: `str`, index: `int`)
    Creates a pointer to an element with the given `index`. Each pointer has a unique name. The pointer is a Vector object.

draw_pointer(name, play, `**config`)
    Draws the pointer.

draw_pointer_name(name: `str`, text: `str`, play, `**config`)
    Draw a `text` below a pointer with the given `name`.

get_pointer(name: `str`)
    Gets the pointer's Vector object.

----------

Contributing
~~~~~~~~~~~~

This is a fairly small project, so I think there are many of you guys who can easily contribute to it! Feel free to contribute and suggest new features! The plans for the future are to make the array much more flexible and create different representations, such as 2D and 3D arrays, stacks, etc.