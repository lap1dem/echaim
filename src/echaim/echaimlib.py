import glob
import os
from os.path import join as jpath

import numpy as np

# echaimlib_path = os.path.join(
#     os.path.dirname(os.path.realpath(__file__)),
#     "source_c/cmake-build-debug"
# )

echaimlib_path = os.path.dirname(os.path.abspath(__file__))


def _import_libs():
    echaimlib = np.ctypeslib.load_library("libECHAIM", echaimlib_path)
    return echaimlib


def _move_libs():
    parent_dir = os.path.abspath(jpath(echaimlib_path, '..'))
    libs = glob.glob(jpath(parent_dir, 'libECHAIM*'))
    for lib in libs:
        parent, file = os.path.split(lib)
        os.rename(lib, jpath(parent, 'echaim', file))


try:
    iri2016, iri2020 = _import_libs()
except OSError:
    _move_libs()
    try:
        iri2016, iri2020 = _import_libs()
    except OSError:
        raise ImportError("Could not import IRI libraries. Please make sure you have installed the package correctly.")