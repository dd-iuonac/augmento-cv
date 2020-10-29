import tkinter
from tkinter import filedialog

import cv2

from src.algorithms import algorithms
from src.utils import read_algorithms, read_images, execute_algorithms

root = tkinter.Tk()

if __name__ == '__main__':
    root.filename = filedialog.askopenfilename(initialdir="./configs/", title="Select Config file",
                                               filetypes=(("Json", "*.json"), ("all files", "*.*")))
    library = read_algorithms(root.filename)

    root.directory = filedialog.askdirectory(initialdir='.', title="Select Input folder")
    images, files = read_images(root.directory)

    root.directory = filedialog.askdirectory(initialdir='.', title="Select Output folder")

    counter = 0
    for k in library.keys():
        algorithms_config_list = library[k]
        for img, file in zip(images, files):
            counter += 1
            image, name = execute_algorithms(img, algorithms, algorithms_config_list)
            new_file = f"{root.directory}/{file.split('.')[0]}_{name[:-1]}_{counter}.jpg"
            cv2.imwrite(new_file, image)
            print(f"SAVED: {new_file}")
