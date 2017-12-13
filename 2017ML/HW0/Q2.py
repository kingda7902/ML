#!/usr/bin/env python
# coding: utf-8

from PIL import Image

def main(argv):
    file_path_1 = argv[0]
    file_path_2 = argv[1]
    img1 = Image.open(file_path_1).convert("RGBA")
    img2 = Image.open(file_path_2).convert("RGBA")
    data1 = img1.getdata()
    data2 = img2.getdata()
    count = 0 
    output = []
    zero_tuple = (0,0,0,0)
    for pixel1 in data1:
        pixel2 = data2[count]
        judge = np.sum([pixel1[x]==pixel2[x] for x in range(0,len(pixel1))])
        if judge != 4:
            output.append(pixel2)
        else:
            output.append(zero_tuple)
        count += 1
    oim = Image.new("RGBA", img1.size, "white")
    oim.putdata(output)
    oim.save("./ans_two.png")

if __name__ == "__main__":
    main(argv[1:])