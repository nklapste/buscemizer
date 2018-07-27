#!/usr/bin/python
# -*- coding: utf-8 -*-

"""argparse entrypoint for buscemizer"""

import argparse
import os
import sys

from buscemizer.buscemizer import buscemize
from face_recognition import load_image_file


def get_parser() -> argparse.ArgumentParser:
    """Create and return the argparser"""
    parser = argparse.ArgumentParser(
        description="Add Steve Buscemi's beautiful facial features to "
                    "facial photos"
    )

    parser.add_argument("image", help="Path to the image to buscemize")

    return parser


def main() -> int:
    """argparse entrypoint function"""
    parser = get_parser()
    args = parser.parse_args()

    image = buscemize(load_image_file(args.image))
    filename, extension = os.path.splitext(args.image)
    filename = os.path.split(filename)[-1]
    image.save("{}-buscemi{}".format(filename, extension))

    return 0


if __name__ == "__main__":
    sys.exit(main())
