import subprocess
import sys
import os
import re
from get_img_list_from_cam import get_camera_image_file_list

exposure=15
cmd = 'gphoto2 --set-config /main/settings/shutterspeed={}'.format(exposure)

timout=exposure+5
output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output.communicate()
output_regex = re.compile(r'New file is in location (\/DCIM\/\d+CANON\/_[A-Za-z\d]+_\d+\.[A-Za-z\d][A-Za-z\d][A-Za-z\d]) on the camera')
pics_taken = []
for i in range(4):
    try:
        proc=subprocess.Popen('gphoto2 --port usb: --capture-image', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for ii in range(10):
            try:
                o,e = proc.communicate()
                m = output_regex.match(o)
                if m:
                    print('Just captured{}'.format(m.group(1)))
                    pics_taken.append(m.group(1))
                break
            except:
                pass
    except:
        pass
    print(i+1)
imgs_on_cam = get_camera_image_file_list()
# for img in sorted(imgs_on_cam):
#   print(img)
print('Done Capturing, now to confirm the files are present:\n\n')
confirmed = []
import time
for pic in pics_taken:
    present = False
    for x in range(10):
        if pic not in imgs_on_cam:
            time.sleep(1)
            print("pic wasn't found on the camera, trying again! ({})".format(pic))
            imgs_on_cam = get_camera_image_file_list()
            # for img in sorted(imgs_on_cam):
            #   print(img)
            # print('\n\n')
        else:
            img_num = imgs_on_cam[pic]
            print("#{} is {}".format(img_num, pic))
            present = True
            break
    confirmed.append(present)

confirmed = all(confirmed)
if not confirmed:
    print('Files missing from camera, stopping until issue can be debugged!')
    sys.exit(-1)
print('All files confirmed to be present, now to download them:\n\n')

for pic in pics_taken:
    get_file_cmd = 'gphoto2 --get-file {}'.format(imgs_on_cam[pic])
    proc = subprocess.Popen(get_file_cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    o,e = proc.communicate()
    print(o.strip('\n'))

from add_imgs import *
imgs = []
for img_path in pics_taken:
    img_path = os.path.split(img_path)[-1]
    imgs.append(load_cr2_image(img_path))
import datetime
save_img(add_images(imgs), 'live_{}.tiff'.format(str(datetime.datetime.now()).replace(' ','_')))
