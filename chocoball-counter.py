
# coding: utf-8

"""
チョコボールの検出
"""


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import io
import os
import glob
import numpy as np
from PIL import Image
from io import BytesIO
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
        """
        ChocoBallの個数をカウントする

        Args:
            img : jpeg image (binary)
        Returns:
            dict{'box':[[ymin,xmin,ymax,xmax]], 'objects':[object_id], 'scores':[score]}
        """
        img_pil = Image.open(BytesIO(img))
        img_arr = np.asarray(img_pil).transpose(2, 0, 1).astype(np.float32)
        bboxes, labels, scores = self.model_frcnn.predict([img_arr])
        return {'box': bboxes, 'objects': labels, 'scores': scores}

    def detectChocoballImage(self, img):
        """
        ChocoBallの個数をカウントする

        Args:
            img : jpeg image (binary)
        Returns:
            dict{'img':image_binary, 'box':[[ymin,xmin,ymax,xmax]], 'objects':[object_id], 'scores':[score]}
        """
        img_pil = Image.open(BytesIO(img))
        img_arr = np.asarray(img_pil).transpose(2, 0, 1).astype(np.float32)
        bboxes, labels, scores = self.model_frcnn.predict([img_arr])

        fig = plt.figure(figsize=(5, 4))
        ax = fig.subplots(1, 1)
        vis_bbox(img_arr, bboxes[0], labels[0], ax=ax)
        plt.savefig('tmp.png')
        with open('tmp.png', 'rb') as f:
            img_b = f.read()
        return {'img': img_b, 'box': bboxes, 'objects': labels, 'scores': scores}


def main():
    HOME = './'

    # ## 画像データのロード
    data_dir = os.path.join(HOME, 'data/res_images')
    img_files = glob.glob(os.path.join(data_dir, '*.JPG'))

    img_file = random.choice(img_files)
    print('image_file : ', img_file)
    with open(img_file, 'rb') as f:
        img_b = f.read()

    # クラスのインスタンス作成
    cd = ChocoballDetector()
    # チョコボールの計測
    res = cd.detectChocoballImage(img_b)

    # bboxes = res['box']
    labels = res['objects']
    # scores = res['scores']
    # classes = cd.classes

    # res['img'].savefig('out/detected.png')
    print(type(res['img']))
    img_pil = Image.open(BytesIO(res['img']))
    img_pil.show()

    # fig = plt.figure(figsize=(12, 4))
    # img = Image.open(img_file)
    # img_arr = np.asarray(img).transpose(2, 0, 1).astype(np.float32)
    # ax = fig.subplots(1, 2)
    # vis_bbox(img_arr, bboxes[0], labels[0], ax=ax[0])
    # vis_bbox(img_arr, bboxes[0], labels[0],
    #          scores[0], label_names=classes, ax=ax[1])
    # # plt.savefig('out/detected.png')
    # plt.show()
    print("detected choco-ball : ", np.sum(labels[0] == 0))

    return 0


if __name__ == '__main__':
    main()
