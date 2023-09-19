import math
myfile = open("Line.PPM", "a")
myfile.truncate(0)
height = 500
width = 500
maxcol = 255

def line(x_0, y_0, x_1, y_1, col):
    written = "P3\n" + str(width) + " " + str(height) + "\n" + str(maxcol) + "\n"
    m = slope(x_0, y_0, x_1, y_1)
    print(m)
    errortol = 0.5
    for i in range(height):
        for j in range(width):
            currm = slope(x_0, y_0, j, i)
            if(currm <= math.ceil(m+errortol) and currm >= math.floor(m-errortol)):
                written += str(col[0]) + " " + str(col[1]) + " " + str(col[2]) + "  "
            else:
                written += (str(255) + " ") * 3 + " "
        written += "\n"
    myfile.write(written)
    myfile.close

def slope(x_0, y_0, x_1, y_1):
    if(x_0 == x_1):
        return 0
    else:
        return (y_1 - y_0) / (x_1 - x_0)