import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input, decode_predictions
import keras.preprocessing.image as Image
from keras.models import Model
from PIL import Image as Image2


class VGG16:
    model = VGG16(
            include_top=True,
            weights="imagenet",
            input_shape=None
        )

    def Judge(self,image_array):
        image = Image2.fromarray(np.uint8(image_array)).resize((224,224))
        #image_path = "img/lion.jpg"
        #image = Image.load_img(image_path) 
        # サイズを(224, 224)に変換
        #image = Image.load_img(image_path, target_size=(224, 224)) 
        print(image.size)
        # 配列に変換
        x=Image.img_to_array(image)
        print(x.shape)
        print(x[0,0])
        print(x[100,100])

        # 軸を指定して次元を増やす
        x = np.expand_dims(x, axis=0) 
        x.shape

        # 各画素値から平均値 (103.939, 116.779, 123.68) を引く
        # カラーのチャネルの順番をRGB→BGR
        x = preprocess_input(x)
        print(x.shape)

        print(self.model.input)
        print(self.model.output)

        result = self.model.predict(x)
        # 予測結果の上位3件を(class, description, probability)に decode
        result = decode_predictions(result, top=3)

        print(result)
        return result

if __name__ == '__main__':
    image_path = "img/lion.jpg"
    image = Image.load_img(image_path, target_size=(1000, 1000))
    x=Image.img_to_array(image)

    vgg=VGG16()
    vgg.Judge(image)