##!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os,cv2
import numpy as np
#from rcnn_bc_recognition import recognize

__author__ = 'Erian Liang'

'''
This can be used for generating a not duplicated file name for a new image,
according to current date time.
'''

# Get current time in millisecond
current_milli_time = lambda : str(round(time.time() * 1000))


def get_new_imgname(origin_imgname, format='jpg', tardir = '.'):
    new_imgname = origin_imgname
    new_imgname = new_imgname + current_milli_time() + '.' + format
    # Check if there is a name existing in current directory
    while(check_if_exist(new_imgname, tardir)):
        new_imgname = new_imgname[:-4] + 'e' + new_imgname[-4:]
    return new_imgname


def check_if_exist(new_imgname, tardir = '.'):
    files = [f for f in os.listdir(tardir) if os.path.isfile(os.path.join(tardir, f))]
    for file in files:
        if file == new_imgname:
            return True
    return False


def encrypt_md5(s):
    import hashlib
    m2 = hashlib.md5()
    m2.update(s.encode('utf-8'))
    return m2.hexdigest()


def gen_tagged_img(img, img_name='bc'):
    new_imgname = get_new_imgname(img_name)
    if recognize(cv2.imdecode(get_np_array_from_tar_object(img), 0), new_imgname) == False:
        return None
    return encrypt_md5(new_imgname)

def recognize(img, new_img_name):
    cv2.imwrite(new_img_name, img)
    return True


def get_np_array_from_tar_object(img_file):
    '''converts a buffer from a tar file in np.array'''
    return np.asarray(
        bytearray(img_file.read())
        , dtype=np.uint8)



