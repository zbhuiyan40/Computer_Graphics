myfile = open("Pixel.ppm", "a")
myfile.truncate(0)
global height, width, written, maxcol
height = 50
width = 100
maxcol = 255
def checkerboard():
    startcol = 255
    written = "P3\n" + str(width) + " " + str(height) + "\n" + str(maxcol) + "\n"
    for i in range(height):
        for j in range(width):
            if(i%2 == 0):
                if(j%2 == 0):
                    written += (str(startcol) + " ") * 3
                else:
                    written += "0 0 0"
            else:
                if(j%2 != 0):
                    written += (str(startcol) + " ") * 3
                else:
                    written += "0 0 0"
            written += "  "
        written += "\n\n"
        if startcol > 0:
            startcol -= 5
    myfile.write(written)
    myfile.close
