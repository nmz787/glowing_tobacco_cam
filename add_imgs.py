import rawpy
import cv2
import os

raw = None
def load_cr2_image(path):
    global raw
    raw = rawpy.imread(path)
    return raw.raw_image
        #rgb = raw.postprocess()
    return raw

def load_cr2_image_list(paths):
    imgs = []
    for img_path in paths:
        imgs.append(load_cr2_image(img_path))
    return imgs

def add_images(img_list, method='b'):
    temp=None
    if method == 'a':
        for img in img_list:
            if temp is None:
                temp = img
            else:
                temp = temp + img
        temp = temp/float(len(img_list))
    elif method=='b':
        temp = img_list[0]
        for img in img_list[1:]:
            temp += img
    return temp

def save_img(img, name):
    #raw.raw_image = img
    img = raw.postprocess(use_auto_wb=True)
    cv2.imwrite(name, img)



if __name__=='__main__':
    imgs = []
    for img_path in [f for f in os.listdir('.') if f.endswith('CR2')]:
        imgs.append(load_cr2_image(img_path))
    save_img(add_images(imgs), 'test.tiff')
