from webcolors import rgb_to_hex, hex_to_name, names, name_to_rgb

def get_color_name(rgb_tuple):
    try:
        # Convert RGB to hex
        hex_value = rgb_to_hex(rgb_tuple)
        # Get the color name directly
        return hex_to_name(hex_value)
    except ValueError:
        # If exact match not found, find the closest color
        return closest_colour(rgb_tuple)

def closest_colour(requested_colour):
    min_colours = {}
    for name in names("css3"):
        r_c, g_c, b_c = name_to_rgb(name)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]