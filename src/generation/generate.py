import matplotlib.pyplot as plot
import numpy
from generation.color_map import custom


def divergent_iterations(real, imaginary, max_iterations):
    c = complex(real, imaginary)
    z = 0.0j

    for iteration in range(max_iterations):
        z = z ** 2 + c
        if abs(z) > 2:
            return iteration

    return max_iterations


def generate_pixel_iterations_map(resolution, max_iterations):
    xs = resolution
    ys = resolution

    pixels = numpy.zeros([xs, ys])

    for x, real in enumerate(numpy.linspace(SCOPE[0], SCOPE[1], num=xs)):
        for y, imaginary in enumerate(numpy.linspace(SCOPE[2], SCOPE[3], num=ys)):
            pixels[x, y] = divergent_iterations(real, imaginary, max_iterations)
    return pixels


def draw_and_save_plot(pixels, color_map, size):
    plot.figure(dpi=size)
    plot.imshow(pixels.T, cmap=color_map, interpolation="bilinear", extent=SCOPE)
    plot.xlabel("Re")
    plot.ylabel("Im")
    plot.savefig("../images/mandelbrotImage.png")


# This value defines the quality/resolution of the image. For quick generations,
# 500 is recommended. For higher quality images, use a value between
# 2000-5000
RESOLUTION = 500
# This value defines the image size. It should be updated accordingly with the
# resolution. An image size above 300 should often not be necessary.
IMAGE_SIZE = min(RESOLUTION * 1.25, 300)
# This value defines the scope/detail of the image. Default: [-2, 1, -1, 1]
SCOPE = [-2, 1, -1, 1]
# This value should be changed if the scope is not the default. Default: 100
MAX_ITERATIONS = 100
# This value changes the color mapping of the generated image. For a small
# scope, "twilight" might be interesting. The default value uses
# a custom generated color map
COLOR_MAP = {
    'red': (
        (0.0, 0.09019607843137255, 0.09019607843137255),
        (0.4, 0.24313725490196078, 0.24313725490196078),
        (0.6,  0.0, 0.0),
        (1.0, 0.0, 0.0)
    ),
    'green': (
        (0.0, 0.1411764705882353, 0.1411764705882353),
        (0.4, 0.6313725490196078, 0.6313725490196078),
        (0.6, 0.8980392156862745, 0.8980392156862745),
        (1.0, 0.0, 0.0)
    ),
    'blue': (
        (0.0, 0.14901960784313725, 0.14901960784313725),
        (0.4, 0.6784313725490196, 0.6784313725490196),
        (0.6, 0.8823529411764706, 0.8823529411764706),
        (1.0, 0.0, 0.0)
    )
}


pixels = generate_pixel_iterations_map(RESOLUTION, MAX_ITERATIONS)
draw_and_save_plot(pixels, custom, IMAGE_SIZE)
print("Generated and saved image")

