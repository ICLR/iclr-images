import glob
import os
for im in glob.glob("*.png"):
    print(im)
    os.system("convert  %s -quality 60 -resize 50%% small/%s"%(im, im.split(".")[0] + ".jpg"))

