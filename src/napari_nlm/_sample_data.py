"""
This module is an example of a barebones sample data provider for napari.

It implements the "sample data" specification.
see: https://napari.org/stable/plugins/guides.html?#sample-data

Replace code below according to your needs.
"""
from __future__ import annotations

import numpy as np
from skimage import data

def make_sample_data():
    """Generates an image"""
    x = data.brick()
    x = x + 20*np.random.normal(0,1,x.shape)
    return [(x, {})]
