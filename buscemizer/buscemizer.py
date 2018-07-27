#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Add Steve Buscemi's eyes to a face(s)"""

import operator

from numpy import ndarray
from PIL import Image
import face_recognition

from buscemizer import BUSCEMI_EYES


def buscemize(image: ndarray) -> Image:
    """Add Steve Buscemi's eyes to a face(s)"""
    buscemized = False
    out_image = Image.fromarray(image)
    for face_landmarks in face_recognition.face_landmarks(image):
        eyes_image = Image.open(BUSCEMI_EYES, "r")
        if "left_eye" in face_landmarks:
            left_eye_min_x = \
                min(face_landmarks["left_eye"], key=operator.itemgetter(0))[0]
            left_eye_max_x = \
                max(face_landmarks["left_eye"], key=operator.itemgetter(0))[0]
            left_eye_min_y = \
                min(face_landmarks["left_eye"], key=operator.itemgetter(1))[1]
            left_eye_max_y = \
                max(face_landmarks["left_eye"], key=operator.itemgetter(1))[1]
            left_pos_x = int(left_eye_max_x - left_eye_max_x*0.15)
            left_pos_y = int(left_eye_max_y - left_eye_max_y*0.12)
            left_size_x = left_eye_max_x - left_eye_min_x
            left_size_y = left_eye_max_y - left_eye_min_y
            left_size_x = left_size_x + left_size_x*5
            left_size_y = left_size_y + left_size_y*5
            eyes_image.thumbnail((left_size_x, left_size_y), Image.ANTIALIAS)
            out_image.paste(eyes_image, (left_pos_x, left_pos_y), eyes_image)
            buscemized = True

        if "right_eye" in face_landmarks:
            right_eye_min_x = \
                min(face_landmarks["right_eye"], key=operator.itemgetter(0))[0]
            right_eye_max_x = \
                max(face_landmarks["right_eye"], key=operator.itemgetter(0))[0]
            right_eye_min_y = \
                min(face_landmarks["right_eye"], key=operator.itemgetter(1))[1]
            right_eye_max_y = \
                max(face_landmarks["right_eye"], key=operator.itemgetter(1))[1]
            right_pos_x = int(right_eye_max_x - right_eye_max_x * 0.1)
            right_pos_y = int(right_eye_max_y - right_eye_max_y * 0.12)
            right_size_x = right_eye_max_x - right_eye_min_x
            right_size_y = right_eye_max_y - right_eye_min_y
            right_size_x = right_size_x + right_size_x * 5
            right_size_y = right_size_y + right_size_y * 5
            eyes_image.thumbnail((right_size_x, right_size_y), Image.ANTIALIAS)
            out_image.paste(eyes_image, (right_pos_x, right_pos_y), eyes_image)
            buscemized = True

    if not buscemized:
        raise ValueError("No valid facial features to buscemize found")

    return out_image
