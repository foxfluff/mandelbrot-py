import mandelbrot

test_set = mandelbrot.mandelbrot()

# just going to use console output, printing something like '#' for points in
# the set.  Assuming default console size of 80x25 (typical for Windows
# systems). 'Minor' corrections for correct aspect ratio

xmin, xmax = -2.0, 1.0
ymin, ymax = -1.0, 1.0

width = 36 * 2  #correction for font not being square, mine happens to be 2:1
height = 24 * 1

for y in range(height):
    row = ""
    for x in range(width):
        real_x, real_y = (
            xmin + x * (xmax - xmin) / width,
            ymax - y * (ymax - ymin) / height
            )
        #print real_x, real_y
        if test_set.calc_point(complex(real_x, real_y))[0]:
            row += "#"
        else:
            row += " "
    print row
