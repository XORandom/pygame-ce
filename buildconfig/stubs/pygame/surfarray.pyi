import numpy

# importing this way exports the functions in the typestubs
from pygame.pixelcopy import (
    array_to_surface as array_to_surface,
    surface_to_array as surface_to_array,
)
from pygame.surface import Surface
from typing_extensions import deprecated  # added in 3.13

def array2d(surface: Surface) -> numpy.ndarray: ...
def pixels2d(surface: Surface) -> numpy.ndarray: ...
def array3d(surface: Surface) -> numpy.ndarray: ...
def pixels3d(surface: Surface) -> numpy.ndarray: ...
def array_alpha(surface: Surface) -> numpy.ndarray: ...
def pixels_alpha(surface: Surface) -> numpy.ndarray: ...
def array_red(surface: Surface) -> numpy.ndarray: ...
def pixels_red(surface: Surface) -> numpy.ndarray: ...
def array_green(surface: Surface) -> numpy.ndarray: ...
def pixels_green(surface: Surface) -> numpy.ndarray: ...
def array_blue(surface: Surface) -> numpy.ndarray: ...
def pixels_blue(surface: Surface) -> numpy.ndarray: ...
def array_colorkey(surface: Surface) -> numpy.ndarray: ...
def make_surface(array: numpy.ndarray) -> Surface: ...
def blit_array(surface: Surface, array: numpy.ndarray) -> None: ...
def map_array(surface: Surface, array: numpy.ndarray) -> numpy.ndarray: ...
@deprecated("Only numpy is supported")
def use_arraytype(arraytype: str) -> None: ...
@deprecated("Only numpy is supported")
def get_arraytype() -> str: ...
@deprecated("Only numpy is supported")
def get_arraytypes() -> tuple[str]: ...
