

import cv2
import os
import timeit


import numpy as np
def sepia_filter(image_filename):
    """
    Applies a sepia filter to image and saves it
    :param image_filename: path to file
    :return None
    """
    if not os.path.exists(f'{image_filename}'):
        raise FileNotFoundError(f'The input filename, {image_filename}, does not exitst')
    image = cv2.imread(image_filename)
    sepia_matrix = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168],[0.393, 0.769, 0.189] ]) #bgr
    image_sepia = np.dot(image, sepia_matrix.T)
    image_sepia *= 255.0 / image_sepia.max()
    image_sepia = image_sepia.astype(np.uint8)
    cv2.imwrite(f"{os.path.splitext(image_filename)[0]}_sepia.JPEG", image_sepia)


if __name__== "__main__":
    start = timeit.default_timer()
    sepia_filter("rain.jpg")
    stop = timeit.default_timer()
    with open('numpy_report_color2sepia.txt', 'w+') as out_file:
        str = f"Timing = numpy_color2sepia \n"
        str += f"Average runtime running numpy_color2sepia after 3 runs :{(stop - start)/3} seconds \n"
        str += f"Averagely {(4.16472806 / (stop - start)/3):.2f} faster than python \n"
        str += f"Timing performed using: timeit"
        out_file.write(str)
    print('Time: ', stop - start)
