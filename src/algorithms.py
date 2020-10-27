import cv2
import numpy as np


def tint(frame, color):
    return cv2.applyColorMap(frame, color)


def rotate(frame, angle):
    image_center = tuple(np.array(frame.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(frame, rot_mat, frame.shape[1::-1], flags=cv2.INTER_CUBIC)
    return result


def resize(frame, width, height):
    return cv2.resize(frame, (width, height))


def brightness(frame, value):
    w, h, c = frame.shape
    for i in range(w):
        for j in range(h):
            for k in range(c):
                frame[i][j][k] = int(frame[i][j][k] + value)
    return frame


def contrast(frame, value):
    w, h, c = frame.shape
    for i in range(w):
        for j in range(h):
            for k in range(c):
                frame[i][j][k] = int(frame[i][j][k] * value)
    return frame


def gamma(frame, value):
    w, h, c = frame.shape
    for i in range(w):
        for j in range(h):
            for k in range(c):
                frame[i][j][k] = int(pow(frame[i][j][k], 1 / value))
    return frame


def gaussian_blur(frame, kernel_size, sigma_x: int = 0):
    return cv2.GaussianBlur(frame, ksize=(kernel_size, kernel_size), sigmaX=sigma_x)


def median_blur(frame, kernel_size):
    return cv2.medianBlur(frame, kernel_size)


def average_blur(frame, kernel_size):
    return cv2.blur(frame, cv2.blur(kernel_size, kernel_size))


algorithms = {
    "averageBlurring": average_blur,
    "medianBlurring": median_blur,
    "gaussianBlurring": gaussian_blur,
    "gamma": gamma,
    "brightness": brightness,
    "contrast": contrast,
    "rotation": rotate,
    "tint": tint,
    "resize": resize
}
