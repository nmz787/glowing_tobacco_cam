s="""There are 13 files in folder '/DCIM/460CANON'.
#1     _MG_6088.CR2               rd  6254 KB image/x-canon-raw
#2     _MG_6089.CR2               rd  6254 KB image/x-canon-raw
#3     _MG_6090.CR2               rd  6207 KB image/x-canon-raw
#4     _MG_6091.CR2               rd  6208 KB image/x-canon-raw
#5     _MG_6092.CR2               rd  6208 KB image/x-canon-raw
#6     _MG_6093.CR2               rd  6208 KB image/x-canon-raw
#7     _MG_6094.CR2               rd  6206 KB image/x-canon-raw
#8     _MG_6095.CR2               rd  6207 KB image/x-canon-raw
#9     _MG_6096.CR2               rd  6208 KB image/x-canon-raw
#10    _MG_6097.CR2               rd  6206 KB image/x-canon-raw
#11    _MG_6098.CR2               rd  6206 KB image/x-canon-raw
#12    _MG_6099.CR2               rd  6209 KB image/x-canon-raw
#13    _MG_6100.CR2               rd  6206 KB image/x-canon-raw
There are 18 files in folder '/DCIM/461CANON'.
#14    _MG_6101.CR2               rd  6255 KB image/x-canon-raw
#15    _MG_6102.CR2               rd  6275 KB image/x-canon-raw
#16    _MG_6103.CR2               rd  6278 KB image/x-canon-raw
#17    _MG_6104.CR2               rd  6273 KB image/x-canon-raw
#18    _MG_6105.CR2               rd  6226 KB image/x-canon-raw
#19    _MG_6106.CR2               rd  6217 KB image/x-canon-raw
#20    _MG_6107.CR2               rd  6235 KB image/x-canon-raw
#21    _MG_6108.CR2               rd  6241 KB image/x-canon-raw
#22    _MG_6109.CR2               rd  6243 KB image/x-canon-raw
#23    _MG_6110.CR2               rd  6229 KB image/x-canon-raw
#24    _MG_6111.CR2               rd  6238 KB image/x-canon-raw
#25    _MG_6112.CR2               rd  6247 KB image/x-canon-raw
#26    _MG_6113.CR2               rd  6226 KB image/x-canon-raw
#27    _MG_6114.CR2               rd  6224 KB image/x-canon-raw
#28    _MG_6115.CR2               rd  6227 KB image/x-canon-raw
#29    _MG_6116.CR2               rd  6227 KB image/x-canon-raw
#30    _MG_6117.CR2               rd  6226 KB image/x-canon-raw
#31    _MG_6118.CR2               rd  6222 KB image/x-canon-raw"""

s="""#1     _MG_6088.CR2               rd  6254 KB image/x-canon-raw
#2     _MG_6089.CR2               rd  6254 KB image/x-canon-raw
#3     _MG_6090.CR2               rd  6207 KB image/x-canon-raw
#4     _MG_6091.CR2               rd  6208 KB image/x-canon-raw
#5     _MG_6092.CR2               rd  6208 KB image/x-canon-raw
#6     _MG_6093.CR2               rd  6208 KB image/x-canon-raw
#7     _MG_6094.CR2               rd  6206 KB image/x-canon-raw
#8     _MG_6095.CR2               rd  6207 KB image/x-canon-raw
#9     _MG_6096.CR2               rd  6208 KB image/x-canon-raw
#10    _MG_6097.CR2               rd  6206 KB image/x-canon-raw
#11    _MG_6098.CR2               rd  6206 KB image/x-canon-raw
#12    _MG_6099.CR2               rd  6209 KB image/x-canon-raw
#13    _MG_6100.CR2               rd  6206 KB image/x-canon-raw
There are 24 files in folder '/DCIM/461CANON'.
#14    _MG_6101.CR2               rd  6255 KB image/x-canon-raw
#15    _MG_6102.CR2               rd  6275 KB image/x-canon-raw
#16    _MG_6103.CR2               rd  6278 KB image/x-canon-raw
#17    _MG_6104.CR2               rd  6273 KB image/x-canon-raw
#18    _MG_6105.CR2               rd  6226 KB image/x-canon-raw
#19    _MG_6106.CR2               rd  6217 KB image/x-canon-raw
#20    _MG_6107.CR2               rd  6235 KB image/x-canon-raw
#21    _MG_6108.CR2               rd  6241 KB image/x-canon-raw
#22    _MG_6109.CR2               rd  6243 KB image/x-canon-raw
#23    _MG_6110.CR2               rd  6229 KB image/x-canon-raw
#24    _MG_6111.CR2               rd  6238 KB image/x-canon-raw
#25    _MG_6112.CR2               rd  6247 KB image/x-canon-raw
#26    _MG_6113.CR2               rd  6226 KB image/x-canon-raw
#27    _MG_6114.CR2               rd  6224 KB image/x-canon-raw
#28    _MG_6115.CR2               rd  6227 KB image/x-canon-raw
#29    _MG_6116.CR2               rd  6227 KB image/x-canon-raw
#30    _MG_6117.CR2               rd  6226 KB image/x-canon-raw
#31    _MG_6118.CR2               rd  6222 KB image/x-canon-raw
#32    _MG_6119.CR2               rd  6213 KB image/x-canon-raw
#33    _MG_6120.CR2               rd  6212 KB image/x-canon-raw
#34    _MG_6121.CR2               rd  6214 KB image/x-canon-raw
#35    _MG_6122.CR2               rd  6213 KB image/x-canon-raw
#36    _MG_6123.CR2               rd  6214 KB image/x-canon-raw
#37    _MG_6124.CR2               rd  6212 KB image/x-canon-raw
"""

import re
import os
import subprocess
raw_image_line = re.compile(r"#(\d+)\s+(_[A-Za-z\d]+_\d+\.[A-Za-z\d][A-Za-z\d][A-Za-z\d])\s+rd\s+\d+\s+KB\s+image/x-canon-raw")
dir_heading_re = re.compile(r"There are (\d+) files in folder '(\/DCIM\/\d+CANON)'\.")

def get_camera_image_file_list(s=None):
    if s is None:
        proc = subprocess.Popen('gphoto2 --list-files',
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        o,e = proc.communicate()
        s=o
    img_dir_tree = {}
    img_list = []
    last_folder=''
    for line in s.split('\n'):
        img_found = raw_image_line.match(line)
        if img_found:
            # img_list.append({
            #   'file_number':img_found.group(1),
            #   'file_path':os.path.join(last_folder, img_found.group(2))
            #   })
            # img_list.append({
            #   os.path.join(last_folder, img_found.group(2)):img_found.group(1)
            #   })
            img_dir_tree[os.path.join(last_folder, img_found.group(2))] = img_found.group(1)
        else:
            folder_found = dir_heading_re.match(line)
            if folder_found:
                # if img_list:
                #   img_dir_tree[last_folder]=img_list
                #   img_list=[]
                last_folder = folder_found.group(2)


        # print('{}\t{}'.format(r1 if not r1 else (r1.group(1), r1.group(2)),
        #                     r2 if not r2 else (r2.group(1), r2.group(2))
        #                     )
        # )
    #print(img_dir_tree)
    return img_dir_tree

if __name__=='__main__':
    for img in sorted(get_camera_image_file_list(s)):
        print(img)