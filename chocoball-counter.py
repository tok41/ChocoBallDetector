
# coding: utf-8

"""
チョコボールの検出
"""


import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

import os
import glob
import numpy as np
from PIL import Image
import random

from chainercv.visualizations import vis_bbox
from chainercv.links import FasterRCNNVGG16


class ChocoballDetector:
    class_file = 'data/classes.txt'
    pretrain_model = 'model/snapshot_model.npz'

    def __init__(self):
        self.getClasses()
        self.setModel()

    def getClasses(self):
        classes = list()
        with open(self.class_file) as fd:
            for one_line in fd.readlines():
                cl = one_line.split('\n')[0]
                classes.append(cl)
        self.classes = classes
        return classes

    def setModel(self):
        self.model_frcnn = FasterRCNNVGG16(n_fg_class=len(self.classes),
                                           pretrained_model=self.pretrain_model)
        return 0

    def detectChocoball(self, img):
        bboxes, labels, scores = self.model_frcnn.predict([img])
        return {'box': bboxes, 'objects': labels, 'scores': scores}


def main():
    HOME = './'

    # ## 画像データのロード
    data_dir = os.path.join(HOME, 'data/res_images')
    img_files = glob.glob(os.path.join(data_dir, '*.JPG'))

    img_file = random.choice(img_files)
    print('image_file : ', img_file)
    img = Image.open(img_file)
    img_arr = np.asarray(img).transpose(2, 0, 1).astype(np.float32)

    cd = ChocoballDetector()
    res = cd.detectChocoball(img_arr)

    bboxes = res['box']
    labels = res['objects']
    scores = res['scores']
    classes = cd.classes

    fig = plt.figure(figsize=(12, 4))
    ax = fig.subplots(1, 2)
    vis_bbox(img_arr, bboxes[0], labels[0], ax=ax[0])
    vis_bbox(img_arr, bboxes[0], labels[0],
             scores[0], label_names=classes, ax=ax[1])
    plt.savefig('out/detected.png')
    print("detected choco-ball : ", np.sum(labels[0] == 0))

    return 0


if __name__ == '__main__':
    main()
