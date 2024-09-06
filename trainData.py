import os
import numpy as np
import cv2
from tensorflow.keras.utils import to_categorical
from keras.layers import Input,Dense
from keras.models import Model

def train_data():
    is_init=False
    size=-1
    label=[]
    dictionary={}
    c=0

    for i in os.listdir():
        if i.split('.')[-1] == "npy" and not(i.split(".")[0] == "labels"):
            if not(is_init):
                is_init=True
                x=np.load(i)
                size = x.shape[0]
                y=np.array([str(i.split(".")[0])]*size).reshape(-1,1)
            else:
                x=np.concatenate((x, np.load(i)))
                y=np.concatenate((y, np.array([str(i.split(".")[0])]*size).reshape(-1,1)))

            label.append(i.split('.')[0])
            dictionary[i.split('.')[0]]=c
            c=c+1

    # print(label)
    # print(dictionary)



    for i in range(y.shape[0]):
        y[i,0]=dictionary[y[i,0]]

    y=np.array(y,dtype="int32")

    # print(y)

    y=to_categorical(y)
    # print(y)

    x_new=x.copy()
    y_new=y.copy()
    counter=0

    cnt=np.arange(x.shape[0])
    # print(cnt)
    np.random.shuffle(cnt)
    # print(cnt)
    for i in cnt:
        x_new[counter]=x[i]
        y_new[counter]=y[i]
        counter=counter+1


    # print(y)
    # print(y_new)

    ip=Input(shape=(x.shape[1]))
    print(ip)
    m=Dense(512,activation="relu")(ip)
    m=Dense(512,activation="relu")(m)

    op=Dense(y.shape[1],activation="softmax")(m)

    model=Model(inputs=ip,outputs=op)

    model.compile(optimizer='rmsprop',loss="categorical_crossentropy",metrics=['acc'])
    model.fit(x,y,epochs=50)

    model.save("model.h5")
    np.save("labels.npy",np.array(label))



    return 1