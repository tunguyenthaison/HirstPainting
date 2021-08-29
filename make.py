# import subprocess
#
# def grid2gif(image_str, output_gif):
#     str1 = 'convert -delay 100 -loop 1 ' + image_str  + ' ' + output_gif
#     subprocess.call(str1, shell=True)
#
# grid2gif("./venv/art*.ps", "my_output.gif")

from PIL import Image
# img = Image.open("art71.ps")
# img.save("i.png")

img_list = []
for i in range(0, 90):
    name = "art{x:03d}.ps".format(x = i)
    Image.open(name).save(name[:-2]+"png")
    print(name)
    #img_list.append(name)
#print(img_list)