"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING

from magicgui import magic_factory
from magicgui import widgets

from qtpy.QtWidgets import QHBoxLayout, QPushButton, QWidget
import napari

if TYPE_CHECKING:
    import napari

from gputools import denoise
from skimage.restoration import estimate_sigma


def denoise_nlm(
    image: napari.types.ImageData,
    sigma: float = 20,
    patch_radius: int = 2,
    search_radius: int = 11,
) -> napari.types.ImageData:


    if image.ndim==2: 
        y = denoise.nlm2(image, sigma, patch_radius, search_radius)
    elif image.ndim==3: 
        y = denoise.nlm3(image, sigma, patch_radius, search_radius)
    else:
        raise NotImplementedError('Only 2D/3D images supported!')
    

    return y

