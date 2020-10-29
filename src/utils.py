import json
import os

import cv2


def read_algorithms(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data


def read_images(folder):
    img_list = []
    names_list = []
    for file in os.listdir(folder):
        img = cv2.imread(f"{folder}/{file}")
        img_list.append(img)
        names_list.append(file)
    return img_list, names_list


def execute_algorithms(image, algorithms, algorithms_config_list):
    name = ""
    img = image.copy()
    for i, algorithm in enumerate(algorithms_config_list):
        img = algorithms[algorithm["name"]](img, *algorithm["params"])
        name = name + algorithm["name"] + "_"
    return img, name
