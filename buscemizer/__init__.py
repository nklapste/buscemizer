#!/usr/bin/python
# -*- coding: utf-8 -*-

"""buscemizer

Add Steve Buscemi's beautiful facial features to facial photos!

Scripts:
 + :mod:`.__main__` - argparse entrypoint script
Modules:
 + :mod:`.buscemizer` - Add Steve Buscemi's eyes to a face(s)
"""

import os

__version__ = (0, 0, 0)

package_dir, _ = os.path.split(os.path.realpath(__file__))
BUSCEMI_EYES = os.path.join(package_dir, "images", "buscemi.png")
