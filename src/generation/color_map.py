from matplotlib.colors import LinearSegmentedColormap
import numpy as np


def code_channel(channel):
    return np.interp(x=channel,xp=[0,255],fp=[0,1])


custom_data = {
    'red': (
        (0.0, code_channel(23), code_channel(23)),
        (0.4, code_channel(62), code_channel(62)),
        (0.6, code_channel(0), code_channel(0)),
        (1.0, code_channel(0), code_channel(0))
    ),
    'green': (
        (0.0, code_channel(36), code_channel(36)),
        (0.4, code_channel(161), code_channel(161)),
        (0.6, code_channel(229), code_channel(229)),
        (1.0, code_channel(0), code_channel(0))
    ),
    'blue': (
        (0.0, code_channel(38), code_channel(38)),
        (0.4, code_channel(173), code_channel(173)),
        (0.6, code_channel(225), code_channel(225)),
        (1.0, code_channel(0), code_channel(0))
    )
}


custom = LinearSegmentedColormap('custom', segmentdata=custom_data)

# Code to debug color mapping:

# from matplotlib import colors
# import matplotlib.pyplot as plot
# from matplotlib import mpl

# figure, axis = plot.subplots()
# figure.colorbar(mpl.ScalarMappable(norm=colors.Normalize(), cmap=custom), ax=axis)
# figure.show()
#
# print(custom_data)
