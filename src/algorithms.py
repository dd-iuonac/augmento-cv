import cv2
import numpy as np


def tint(frame, color):
    return cv2.applyColorMap(frame, color % 11)


def rotate(frame, angle):
    image_center = tuple(np.array(frame.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(frame, rot_mat, frame.shape[1::-1], flags=cv2.INTER_CUBIC)
    return result


def resize(frame, width, height):
    return cv2.resize(frame, (width, height))


def brightness_manual(frame, value):
    w, h, c = frame.shape
    for i in range(w):
        for j in range(h):
            for k in range(c):
                frame[i][j][k] = int(frame[i][j][k] + value)
    return frame


def contrast_manual(frame, value):
    w, h, c = frame.shape
    for i in range(w):
        for j in range(h):
            for k in range(c):
                frame[i][j][k] = int(frame[i][j][k] * value)
    return frame


def gamma_manual(frame, value):
    w, h, c = frame.shape
    for i in range(w):
        for j in range(h):
            for k in range(c):
                frame[i][j][k] = int(pow(frame[i][j][k], 1 / value))
    return frame


# src1*alpha + src2*beta + gamma
def brightness(frame, value):
    return cv2.addWeighted(src1=frame, alpha=2, src2=np.zeros(frame.shape, frame.dtype), beta=0, gamma=value)


def contrast(frame, value):
    return cv2.addWeighted(src1=frame, alpha=value, src2=np.zeros(frame.shape, frame.dtype), beta=0, gamma=0)


def gamma(frame, value):
    inv_gamma = 1.0 / value
    table = np.array([((i / 255.0) ** inv_gamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(frame, table)


def gaussian_blur(frame, kernel_size, sigma_x: int = 0):
    return cv2.GaussianBlur(frame, ksize=(kernel_size, kernel_size), sigmaX=sigma_x)


def median_blur(frame, kernel_size):
    return cv2.medianBlur(frame, kernel_size)


def average_blur(frame, kernel_size):
    return cv2.blur(frame, (kernel_size, kernel_size))


def translation(frame, transform_matrix):
    rows, cols, _ = frame.shape

    m = np.float32(transform_matrix)
    dst = cv2.warpAffine(frame, m, (cols, rows))
    return dst


def flip(frame, value):
    return cv2.flip(frame, value)


def perspective_transform(frame, pts1, pts2, d_size):
    pts1 = np.float32(pts1)
    pts2 = np.float32(pts2)

    m = cv2.getPerspectiveTransform(pts1, pts2)
    return cv2.warpPerspective(frame, m, tuple(d_size))


algorithms = {
    "averageBlurring": average_blur,
    "medianBlurring": median_blur,
    "gaussianBlurring": gaussian_blur,
    "gamma": gamma,
    "gamma_manual": gamma_manual,
    "brightness": brightness,
    "brightness_manual": brightness_manual,
    "contrast": contrast,
    "contrast_manual": contrast_manual,
    "tint": tint,
    "rotation": rotate,
    "resize": resize,
    "translation": translation,
    "flip": flip,
    "perspective_transform": perspective_transform
}
