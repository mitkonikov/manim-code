from manim import *
# from manim_code import *

# When developing the script it's nice to just grab it from the source file
# import sys
sys.path.append('C:\GitHub\ManimWorks\manim-code\src')

from manim_code.array import Array
from manim_code.pointer import TextPointer

class ArrayMain(Scene):
    def construct(self):
        array = Array(
            "Array", 
            *range(6), # this is the array 
            name_config={"fill_color": WHITE}
        )
        array.create_array(sq_size=0.5, name_size=1.2)
        for anims in array.draw_array():
            self.play(anims, run_time = 0.5)
        
        # create a pointer with a text label
        pointer = TextPointer("Here", 0.8, UP)
        pointer.next_to(array.get_square(2), DOWN)
        self.play(*pointer.draw(), run_time=0.5)

        # connect the pointer, so when you transform the array
        # it will transform the pointer as well
        array.connect_pointer(pointer)

        # shift the pointer
        self.play(
            ApplyMethod(pointer.next_to, array.get_square(4), DOWN, aligned_edge=UP),
            run_time=0.5
        )
        
        self.play(*array.indicate_at(4), run_time=0.5)
        # example for scaling the whole array
        self.play(ApplyMethod(array.scale, 1.1), run_time=0.5)
        
        # popping an element
        pop_anims = list(array.pop(index=3))
        self.play(*pop_anims[:-1]) # pop the element
        self.wait()
        self.play(*pop_anims[-1:]) # shift the others
        self.wait()
