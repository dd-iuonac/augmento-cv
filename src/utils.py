import json


def read_algorithms():
    with open("algorithms.json", "r") as file:
        data = json.load(file)
        return data