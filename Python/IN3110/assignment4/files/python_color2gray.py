import cv2
import os
import timeit

#import numpy as np
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
    weights = [0.07 , 0.71, 0.21]
    for x in image_rgb:
        for z in x:
            z[:] = min(255, sum([weights[j]*z[j] for j in range(len(z))]).astype("uint8"))
    grayscale = image_rgb
    grayscale_bgr = cv2.cvtColor(grayscale, cv2.COLOR_RGB2BGR)
    cv2.imwrite(f"{os.path.splitext(image_filename)[0]}_grayscale.JPEG", grayscale_bgr)

if __name__== "__main__":
    start = timeit.default_timer()
    grayscale_filter("rain.jpg")
    stop = timeit.default_timer()
    with open('python_report_color2gray.txt', 'w+') as out_file:
        str = f"Timing = python_color2gray \n"
        str += f"Average runtime running python_color2gray after 3 runs :{(stop - start)/3} seconds \n"
        str += f"Timing performed using: timeit"
        out_file.write(str)
    print('Time: ', stop - start)
    print('Time: ', stop - start)
