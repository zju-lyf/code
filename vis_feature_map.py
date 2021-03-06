# coding: utf-8
 
# from keras.models import Model
import cv2
import matplotlib.pyplot as plt
# from keras.models import Sequential
# from keras.layers.convolutional import Convolution2D, MaxPooling2D
# from keras.layers import Activation
from pylab import *
import pdb
#import keras
 
 
def get_row_col(num_pic):
    squr = num_pic ** 0.5
    row = round(squr)
    col = row + 1 if squr - row > 0 else row
    return row, col
 
 
def visualize_feature_map(img_batch, layer_num):
    feature_map = np.squeeze(img_batch, axis=0)
    print(feature_map.shape)
 
    feature_map_combination = []
    plt.figure()
 
    num_pic = feature_map.shape[0]
    row, col = get_row_col(num_pic)
 
    for i in range(0, num_pic):
        feature_map_split = feature_map[i, :, :]
        feature_map_combination.append(feature_map_split)
        plt.subplot(row, col, i + 1)
        #pdb.set_trace()

        plt.imshow(feature_map_split.cpu().detach().numpy())
        axis('off')
        # title(i, usetex=False)
 
    plt.savefig('./feature/FX_waigua_atten/feature_map'+str(layer_num)+'.png')
    plt.show()
 
    # 各个特征图按1：1 叠加
    feature_map_sum = sum(ele for ele in feature_map_combination)
    
    plt.imshow(feature_map_sum.cpu().detach().numpy())
    plt.savefig("./feature/FX_waigua_atten/feature_map_sum"+str(layer_num)+'.png')
 
 
# def create_model():
#     model = Sequential()
 
#     # 第一层CNN
#     # 第一个参数是卷积核的数量，第二三个参数是卷积核的大小
#     model.add(Convolution2D(9, 5, 5, input_shape=img.shape))
#     model.add(Activation('relu'))
#     model.add(MaxPooling2D(pool_size=(4, 4)))
 
#     # 第二层CNN
#     model.add(Convolution2D(9, 5, 5, input_shape=img.shape))
#     model.add(Activation('relu'))
#     model.add(MaxPooling2D(pool_size=(3, 3)))
 
#     # 第三层CNN
#     model.add(Convolution2D(9, 5, 5, input_shape=img.shape))
#     model.add(Activation('relu'))
#     model.add(MaxPooling2D(pool_size=(2, 2)))
 
#     # 第四层CNN
#     model.add(Convolution2D(9, 3, 3, input_shape=img.shape))
#     model.add(Activation('relu'))
#     # model.add(MaxPooling2D(pool_size=(2, 2)))
 
#     return model
 
 
# if __name__ == "__main__":
#     img = cv2.imread('/home/lyf/ws/skip-ganomaly/data/bottle/test/broken_large/000.png')
 
#     model = create_model()
 
#     img_batch = np.expand_dims(img, axis=0)
#     conv_img = model.predict(img_batch)  # conv_img 卷积结果
 
#     visualize_feature_map(conv_img)