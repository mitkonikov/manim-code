Advanced Code Extensions
------------------------

This Manim extension allows you to quickly create arrays, assign elements, point to elements, push, pop and etc. It sits on top of the `Manim Community Edition <https://github.com/ManimCommunity/manim>`_.

Overview:
 - Array

In the works:
 - Code Highlighting by text search

TODO:
 - Queue
 - Stack

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

Contributing
~~~~~~~~~~~~

Feel free to contribute and suggest new features!