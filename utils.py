import numpy as np
import cv2

def transform(img, shape, inv=False):
    """
    Transform the image to the desired shape

    Args:
        img (np.array): image to be transformed
        shape (tuple): desired shape
    Returns:
        dst (np.array): transformed image
    
    """

    h, w, c = shape
    pts1 = np.float32([[410, 410], [921,423], [1028,503], [304,483]])
    pts2 = np.float32([[0,0],[w,0],[w,h],[0,h]])

    if inv:
        M = cv2.getPerspectiveTransform(pts2, pts1)
    else:
        M = cv2.getPerspectiveTransform(pts1, pts2)
    
    dst = cv2.warpPerspective(img, M, (w, h))

    return dst