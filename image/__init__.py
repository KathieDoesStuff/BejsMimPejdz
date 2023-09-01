import os

import cv2


def convert_to_jpg(image_filename: str):
    file_extension = image_filename.split(".")[-1]

    if file_extension == "jpg":
        return image_filename

    img = cv2.imread(image_filename)
    os.remove(image_filename)

    image_filename = image_filename.replace(file_extension, "jpg")

    cv2.imwrite(image_filename, img)
    return image_filename
