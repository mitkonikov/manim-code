from manim_code import __version__
from manim_code import Array

def test_version():
    assert __version__ == '0.1.0'

def test_create_array_obj():
    arr = [3, 4, 5, 6, 7, 8]

    arr_obj = Array("test:", len(arr), values = arr, name_config = {
        "fill_color": "#ff0000"
    })

    assert arr_obj