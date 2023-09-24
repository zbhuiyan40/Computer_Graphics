myfile = open("Pixel.PPM", "a")
myfile.truncate(0)
height = 500
width = 500
maxcol = 255

def ombre(col_1, col_2, ombrelen):
    written = "P3\n" + str(width) + " " + str(height) + "\n" + str(maxcol) + "\n"
    for i in range(height):
        if(i % ombrelen == 0):
            for k in range(3):
                if(col_1[k] < col_2[k]):
                    col_1[k] += 1
                elif(col_1[k] == col_2[k]):
                    col_1[k] = col_1[k]
                else:
                    col_1[k] -= 1
        for j in range(width):
            written += str(col_1[0]) + " " + str(col_1[1]) + " " + str(col_1[2]) + " "
    myfile.write(written)
    myfile.close
