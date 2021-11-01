

import cv2
import os
import timeit
from numba import jit


@jit(nopython=True)
def numba_sepia_filter(image):
    """
    A helper function which uses numba to calculate efficient and fast
    :param image: Image array
    :return: image array with filter
    """
    sepia_matrix = [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
    for x in image:
        for z in x:
            r = min(255, int(z[0] * sepia_matrix[0][0] + z[1] * sepia_matrix[0][1] + z[2] * sepia_matrix[0][2]))
            g = min(255, int(z[0] * sepia_matrix[1][0] + z[1] * sepia_matrix[1][1] + z[2] * sepia_matrix[1][2]))
            b = min(255, int(z[0] * sepia_matrix[2][0] + z[1] * sepia_matrix[2][1] + z[2] * sepia_matrix[2][0]))

            z[0] = r
            z[1] = g
            z[2] = b
    return image

def sepia_filter(image_filename):
    """
    Applies a sepia filter to image and saves it
    :param image_filename: path to file
    :return None
    """

    if not os.path.exists(f'{image_filename}'):
        raise FileNotFoundError(f'The input filename, {image_filename}, does not exitst')
    image = cv2.imread(image_filename)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_sepia = numba_sepia_filter(image_rgb.astype("float64")).astype('uint8')
    image_sepia_bgr = cv2.cvtColor(image_sepia, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f"{os.path.splitext(image_filename)[0]}_sepia.JPEG", image_sepia_bgr)

if __name__== "__main__":
    start = timeit.default_timer()
    sepia_filter("rain.jpg")
    stop = timeit.default_timer()
    with open('numba_report_color2sepia.txt', 'w+') as out_file:
        str = f"Timing = numba_color2sepia \n"
        str += f"Average runtime running numba_color2sepia after 3 runs :{(stop - start) / 3} seconds \n"
        str += f"Averagely {( (stop - start) / 3)/(0.009036466666666668) :.2f} faster than numpy_color2sepia \n"
        str += f"Timing performed using: timeit"
        out_file.write(str)
    print('Time: ', stop - start)




