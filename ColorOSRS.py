"""
Object dedicated to holding HSV color space data. Holds Tuples of Lower and Upper bounds.
Default color object used in pybotosrs
- Mark
"""


class ColorOSRS:

    # class constructor
    def __init__(self, lower_bounds=(0, 0, 0), upper_bounds=(20, 20, 20)):
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds

    # prints color, lower , upper
    def print_color(self):
        print("Lower/Upper bounds of HSV color are: ", self.lower_bounds, ",", self.upper_bounds)
