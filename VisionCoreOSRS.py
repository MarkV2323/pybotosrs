"""
Class that handles all vision related task that are core to a color bot, such as finding colors.
Author: Mark II
"""
import pyautogui
import cv2 as cv2
import numpy as _np


# handles finding a specific color within a image (in HSV).
# remember, you are searching BGR inside of the hsv_image, you need to get the BGR colors from hsv_image.
def find_color(user_image, a_color_palet_tuple, display_hsv=False):
    # a_color = colOSRS()           | a_color_palet_tuple = (colOSRS, colOSRS, ...)
    # a_np_array = (lower1, upper1) | a_np_array_list    = [a_np_array, a_np_array, ...]
    # converts colOSRS tuple into corresponding np.arrays in a similar format.
    a_np_array_list = []
    for a_color in a_color_palet_tuple:
        a_np_array = (_np.array(a_color.lower_bounds, dtype="uint8"), _np.array(a_color.upper_bounds, dtype="uint8"))
        a_np_array_list.append(a_np_array)

    # converts color space to HSV
    hsv_image = cv2.cvtColor(user_image, cv2.COLOR_BGR2HSV)
    if display_hsv is True:
        display_pic(hsv_image)

    # a_mask = cv2.inRange(hsv_image, a_np_array[0], a_np_array[1]) | a_mask_array = (a_mask, a_mask, ...)
    # creates a_mask_array from the a_array_np_list object.
    a_mask_array = []
    mask = None
    for a_np_array in a_np_array_list:
        mask = cv2.inRange(hsv_image, a_np_array[0], a_np_array[1])
        a_mask_array.append(mask)

    # loop through possible masks, layering them onto each other.
    for a_mask in a_mask_array:
        mask = cv2.bitwise_or(mask, a_mask)

    # final overlay
    target = cv2.bitwise_and(user_image, user_image, mask=mask)
    return target


# handles creating and processing clusters, returns information about said clusters.
def cluster_detected_pixels(detected_colors, k, debug=False):
    # constant color, black.
    color_black = (0, 0, 0)

    # detected colors image is converted into 2D array. Ex: row x col
    image_array = _np.array(detected_colors)

    # x: print(len(image_array))
    # y: print(len(image_array[0]))
    # records current time to track execution speed.
    # start_time = time.time()

    # gathers the locations of all detected pixels into a np.float32 type array. (X,Y pos)
    indices = _np.where(image_array != color_black)
    coordinates = zip(indices[0], indices[1])
    uniques = list(set(list(coordinates)))
    uniques = _np.float32(uniques)

    # controls the minimum amount of detected pixels for valid clusters to be formed.
    if len(uniques) < 100:
        print('total detected pixel count is < 100, no clusters will be formed')
        return False

    # begins process of applying K-Mean's cluster algorithm. Process will return center points of detected clusters.
    # k - The specified amount of clusters to form (this is the "supervised" part of the machine learning).
    # TODO: Apply some estimating algorithm to create an unsupervised version for estimating total number of clusters.
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 1.0)
    ret, label, center = cv2.kmeans(uniques, k, None, criteria, 100, cv2.KMEANS_RANDOM_CENTERS)

    # packs the cluster data into a list and returns the package.
    # ret -> label -> center -> all detected pixel coordinates
    cluster_data = [ret, label, center, uniques]

    # flag: if DEBUG CLUSTERS should execute.
    if debug is True:
        __cluster_print(detected_colors, cluster_data, k)

    return cluster_data


# handles performing final filter on clusters to find the most relevant object as compared to the query.
def filter_nearest_point(center_points, near_point):
    # performs an operation to find the nearest point using a the basic distance formula + smallest distance total.
    # Operates in O(n), linear time. This is fine, as we usually deal with < 20 cluster points at a time.
    best_point = None
    best_distance = None

    # goes through entire list of center points
    for current_point in center_points:
        # calculates the distance between current point, and the specified point.
        current_distance = __distance(current_point, near_point)
        # if best_point is empty, or a new smallest distance has been found, sets best point to the current point
        if best_point is None or current_distance < best_distance:
            best_point = current_point
            best_distance = current_distance

    # returns the closest point from the list.
    # print(best_point[0], " ", best_point[1])
    return best_point


# handles gathering a point from the screen. returns point gathered
def get_point():
    # Allows for input waiting.
    input('Press enter to record a point: ')
    point = pyautogui.position()
    return point


# for quick picture display
def display_pic(the_picture):
    cv2.imshow("Picture", the_picture)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# handles allowing the user to take a picture in an area of the primary screen. returns cropped image.
def take_pic(a_point, b_point):
    # taking a screenshot, in mem. must convert pyautogui screenshot into cv2 friendly object.
    image = pyautogui.screenshot(region=(a_point.x, a_point.y, (b_point.x - a_point.x), (b_point.y - a_point.y)))
    image = cv2.cvtColor(_np.array(image), cv2.COLOR_RGB2BGR)
    return image


"""
Private Methods
"""


# handles printing information about cluster for debug purposes. Will display picture with red center points of clusters
def __cluster_print(user_image, clusters, k):
    # DEBUG: Creates a copy of the detected colors image, to draw center points of detected clusters on.
    results = user_image
    placed = 0

    # places uniques data & label data & center data from clusters into unique instanced variable.
    # label = clusters[1]
    center = clusters[2]
    # uniques = clusters[3]

    # converts user_image into an np array
    user_array = _np.array(user_image)

    # begins placing cluster center points
    for i in range(k):
        # temp_cluster = uniques[label.ravel() == i]
        # print('size of cluster ', i, ': ', len(temp_cluster))
        temp_center = _np.round(center[i])
        # print('center: ', temp_center[1], ' ', temp_center[0])

        # check y
        if 0 <= temp_center[1] < len(user_array[0]):
            # check x
            if 0 <= temp_center[0] < len(user_array):
                # print('placed: ', temp_center[0], ' ', temp_center[1])
                placed += 1
                results[int(temp_center[0])][int(temp_center[1])] = [0, 0, 255]

    # DEBUG: Print out pos of detected cluster center point.
    # print(results[int(centerA[0])][int(centerA[1])])

    # Current end process for printing stats about operation.
    print('Valid Centers found: ', placed)
    cv2.imshow('Center locations of clusters', results)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# distance method
def __distance(point_a, point_b):
    x1, y1 = point_a
    x2, y2 = point_b
    dx = (x2 - x1)
    dy = (y2 - y1)
    return _np.sqrt((dx * dx) + (dy * dy))


# handles cropping an image to a specific width x height
def __crop_image(point_one_x, point_one_y, point_two_x, point_two_y, a_image):
    x = point_one_x
    y = point_one_y
    width = point_two_x - point_one_x
    height = point_two_y - point_one_y
    the_image = a_image[y:y+height, x:x+width]
    # print('X:', x, ' Y:', y, ' W:', width, ' H:', height)
    return the_image
