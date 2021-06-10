from manim_code import __version__
from manim_code import Array
from manim_code import TextPointer
from manim.constants import UP

def test_version():
    assert __version__ == '0.1.0'

def test_create_array_obj():
    arr = [3, 4, 5, 6, 7, 8]

    arr_obj = Array("test:", arr, name_config = {
        "fill_color": "#ff0000"
    })

    assert arr_obj

def test_create_pointer_obs():
    pointer = TextPointer("Here", 0.8, UP)

    assert pointer