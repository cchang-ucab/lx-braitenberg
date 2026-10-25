import cv2
import numpy as np

# simulator images
#lower_hsv = np.array([20, 100, 100])
#upper_hsv = np.array([30, 255, 255])

#cchang test
lower_hsv = np.array([15, 50, 50])
upper_hsv = np.array([40, 255, 255])
# real images
# lower_hsv = np.array([12, 89, 76])
# upper_hsv = np.array([31, 255, 255])


# real images mecaduckie00
# lower_hsv = np.array([3, 92, 0])
# upper_hsv = np.array([24, 226, 255])


#original
#def preprocess(image_rgb: np.ndarray) -> np.ndarray:
#    """Returns a 2D array"""
#    hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
#    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
#    return mask


# Minimum brightness (V) to consider a pixel NOT part of the black floor
MIN_BRIGHTNESS_NOT_BLACK = 150


def preprocess(image_rgb: np.ndarray) -> np.ndarray:
    """Returns a 2D array"""
    hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
    # Duckies: count as 255
    duckie_mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    # Everything that is NOT black (high brightness): the edge of the area
    not_black_mask = cv2.inRange(hsv, np.array([0, 0, MIN_BRIGHTNESS_NOT_BLACK]), np.array([179, 255, 255]))
    # The edge counts less (30%), so it does not "hide" the duckies
    return duckie_mask.astype(np.float32) + 0.1 * not_black_mask.astype(np.float32)