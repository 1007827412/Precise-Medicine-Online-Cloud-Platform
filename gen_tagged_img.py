##!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, os,cv2
import numpy as np
from rcnn_bc_recognition import recognize

__author__ = 'Erian Liang'

'''
This can be used for generating a not duplicated file name for a new image,
according to current date time.
'''

# Get current time in millisecond
current_milli_time = lambda : str(round(time.time() * 1000))


def get_new_imgname(origin_imgname, format='jpg', tardir = '.'):
    new_imgname = origin_imgname[:-4]
    new_imgname = new_imgname + current_milli_time()
    # Check if there is a name existing in current directory
    while(check_if_exist(new_imgname, tardir)):
        new_imgname = new_imgname[:-4] + 'e' + new_imgname[-4:]
    new_imgname = os.path.join(tardir, encrypt_md5(new_imgname))
    new_imgname = new_imgname + '.' + format
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


def gen_tagged_img(img, img_name='bc.jpg'):
    indir = reduce(os.path.join, ['.','static','input'])
    outdir = reduce(os.path.join, ['.','static','output'])
    imdir = os.path.join(indir, img_name)
    img.save(imdir)
    new_imgname = get_new_imgname(img_name, tardir=outdir)
    if recognize(cv2.imread(imdir), new_imgname) == False:
        return None
    import re
    return re.split(r'[\\/]', new_imgname)[-1] #only encode file name


def get_np_array_from_tar_object(img_file):
    '''converts a buffer from a tar file in np.array'''
    return np.asarray(
        bytearray(img_file.read())
        , dtype=np.float32)
