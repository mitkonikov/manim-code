from manim import *
from manim_code import *

# When developing the script it's nice to just grab it from the source file
# import sys
# sys.path.append('C:\GitHub\ManimWorks\manim-code\src')

# from manim_code.array import Array

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
        # example for scaling the whole array
        self.play(ApplyMethod(array.scale, 1.1), run_time=0.5)
        
        # popping an element
        pop_anims = list(array.pop(index=3))
        self.play(*pop_anims[:-1]) # pop the element
        self.wait()
        self.play(*pop_anims[-1:]) # shift the others
        self.wait()
