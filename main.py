import os
import tkinter
from tkinter import filedialog

import cv2

from src.algorithms import algorithms
from src.utils import read_algorithms

root = tkinter.Tk()

if __name__ == '__main__':
    root.directory = filedialog.askdirectory(initialdir='.')
    counter = 0

    library = read_algorithms()

    for file in os.listdir(root.directory):
        img = cv2.imread(f"{root.directory}/{file}")
        for k in library.keys():
            image = img.copy()
            algorithms_list = library[k]
            counter += 1
            name = ""
            for i, algorithm in enumerate(algorithms_list):
                image = algorithms[algorithm["name"]](image, *algorithm["params"])
                name = name + algorithm["name"] + "_"
            cv2.imwrite(f"{os.getcwd()}/test_aug/{file.split('.')[0]}_{name[:-1]}_{counter}.jpg", image)
