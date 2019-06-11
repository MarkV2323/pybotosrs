TODO: [ ] Add in method for checking if min number of pixels of color were found.
      [ ] Add in method for applying the Elbow Algorithm for a general search function. (avg k clusters)  
      [ ] Create dedicated vision class, move polished and refactored methods into this class permanently.

------------------------------------------------------------------------------------------------------------------------
Summary and Dependencies
------------------------------------------------------------------------------------------------------------------------
Basic use of openCV2, numpy, and pyAutoGUI to create a library of functions dedicated to color bot programming for OSRS.
Dedicated class functionality aimed towards creating a sense of vision for the bot to interpret data from.

To install packages / dependencies on a windows machine use: 
python -m pip install [packagename]

otherwise just use pip:
pip install [packagename]

OS X should use the following openCV install command:


------------------------------------------------------------------------------------------------------------------------
Algorithm for going from 2 points and a color -> detected pixel cluster w/ center point information.
------------------------------------------------------------------------------------------------------------------------
1: Gather points from user, take a screen shot.
2: Pass screenshot to image crop process, crop screen shot according to points gathered.
3: Pass cropped image to color finding process, which will find the desired color from the image provided.
4: Pass the detected color image to the cluster process, process coordinate data into cluster data w/ centers.
5: Pass cluster data into final filter process, this will filter the best cluster that matches our criteria.
6: Return the desired object's clusterData.


------------------------------------------------------------------------------------------------------------------------
Useful references and documentation on different dependencies.
------------------------------------------------------------------------------------------------------------------------
https://stackoverflow.com/questions/4195453/how-to-resize-an-image-with-opencv2-0-and-python2-6
https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
https://www.pyimagesearch.com/2018/01/01/taking-screenshots-with-opencv-and-python/
https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
https://docs.opencv.org/3.2.0/d0/d86/tutorial_py_image_arithmetics.html
https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_basic_image_operations_pixel_access_image_load.php

Cheat sheet for pyAutoGUI:
https://pyautogui.readthedocs.io/en/latest/cheatsheet.html


------------------------------------------------------------------------------------------------------------------------
Closing remarks, end of in-code Documentation.
------------------------------------------------------------------------------------------------------------------------

Author Notes: More or less I have been designing this class to function as a visual sense for the bot to use. Just like
              our vision, the bot is designed to work off of colors, and thus needs a class that is dedicated to 
              processing vision, so the dedicated logic class can perform actions based off of the data gathered.
              
Author: Mark Alan Vincent II
Version: 1.1, update 1a, last 06/01/2019