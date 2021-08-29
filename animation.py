import os

img_list = []
for i in range(0, 90):
    name = "art{x:03d}.ps".format(x = i)
    img_list.append(name)
print(img_list)
os.system('magick identify --version')
os.system('magick convert -loop 0 %s anime.gif' % ' '.join(img_list))
