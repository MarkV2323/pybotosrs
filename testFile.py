import VisionCoreOSRS as vcOSRS
import WindowOSRS as winOSRS
import ColorOSRS as colOSRS

# color: Blue, Green, Red _color_green = ([35, 115, 100], [40, 255, 130])

# Test build for multi layered color support.
color_green = colOSRS.ColorOSRS((35, 115, 100), (40, 255, 130))
color_brown = colOSRS.ColorOSRS((5, 125, 120), (30, 140, 155))
# color_red = colOSRS.ColorOSRS((23, 16, 65), (32, 21, 123))
color_palet_tuple = (color_green, color_brown)

# Test build for no color found exception.
# color = colOSRS.ColorOSRS((252, 252, 252), (253, 253, 253))
# color_palet_tuple = (color,)

# takes a picture of the user's desired area.
# pointA = findObj.get_point()
# pointB = findObj.get_point()


# takes a picture, displays resulting photo.
# user_image0 = findObj.take_pic(pointA, pointB)
# findObj.display_pic(user_image0)


# finds color and displays
# user_image0 = findObj.__find_color(user_image0, color_palet_tuple)
# cluster_data = findObj.__cluster_process(user_image0, 8)
# if cluster_data is False:
#     print('No clusters were found.')

window = winOSRS.WindowOSRS()
window.setup_window()

