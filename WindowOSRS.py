"""
Handles operations dealing with the window in which the robots "eyeball" can see.
Author: Mark II
"""
import pyautogui
from VisionCoreOSRS import take_pic, display_pic, get_point


class WindowOSRS:

    # class constructor (defaults to 0,0 w/ smallest sized runelite window.
    def __init__(self, window_top_left_pixel=(pyautogui.Point(0, 0)),
                 window_bottom_right_pixel=(pyautogui.Point(805, 530))):
        # sets up window location and size.
        self.window_top_left_pixel = window_top_left_pixel
        self.window_bottom_right_pixel = window_bottom_right_pixel

    # setups static window values and locations for the user. (will default to text settings in future?)
    def setup_window(self):
        setup_complete = False
        while setup_complete is False:
            # gets windows top left point from user.
            point_a = get_point()

            # sets top left pixel, bottom right pixel, takes screenshot of window, displays for user to confirm.
            window_top_left_pixel = point_a
            window_bottom_right_pixel = pyautogui.Point(window_top_left_pixel.x + 805, window_top_left_pixel.y + 530)
            temp_window = take_pic(window_top_left_pixel, window_bottom_right_pixel)

            # results
            print('Top left: ', window_top_left_pixel, '\t|\tBottom right: ', window_bottom_right_pixel)
            display_pic(temp_window)
            user_input = int(input('To accept this window, enter 0: '))
            if user_input == 0:
                setup_complete = True
                print("Exiting setup_window Method.")
                self.window_top_left_pixel = window_top_left_pixel
                self.window_bottom_right_pixel = window_bottom_right_pixel
                return setup_complete
