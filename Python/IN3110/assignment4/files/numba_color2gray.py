import cv2
import os.path
import timeit
from numba import jit


@jit(nopython=True)
def numba_grayscale_filter(image):
    """
    A helper function which uses numba to calculate efficient and fast
    :param image: Image array
    :return: image array with filter
    """
    weights = (0.07, 0.71, 0.21)
    for x in image:
        for z in x:
            z[:] = min(255, int(weights[0] * z[0] + weights[1] * z[1] + weights[2] * z[2]))
    return image


def grayscale_filter(image_filename):
    """
    Applies a grayscale filter to image and saves it
    :param image_filename: path to file
    :return None
    """
    if not os.path.exists(f'{image_filename}'):
        raise FileNotFoundError(f'The input filename, {image_filename}, does not exitst')
    image = cv2.imread(image_filename)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    grayscale = numba_grayscale_filter(image_rgb.astype("float64")).astype('uint8')
    grayscale_bgr = cv2.cvtColor(grayscale, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f"{os.path.splitext(image_filename)[0]}_grayscale.JPEG", grayscale_bgr)


if __name__ == "__main__":
    start = timeit.default_timer()
    grayscale_filter('rain.jpg')
    stop = timeit.default_timer()
    with open('numba_report_color2gray.txt', 'w+') as out_file:
        str = f"Timing = numba_color2gray \n"
        str += f"Average runtime running numba_color2gray after 3 runs :{(stop - start) / 3} seconds \n"
        str += f"Averagely {((stop - start) / 3) / (0.009036466666666668) :.2f} faster than numpy_color2gray \n"
        str += f"Timing performed using: timeit"
        out_file.write(str)
    print('Time: ', stop - start)
