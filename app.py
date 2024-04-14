import model
import numpy as np
import streamlit as st
import tensorflow as tf
from matplotlib.pyplot import imshow
from tensorflow.keras.preprocessing import image
base_learning_rate = 0.005
loaded_model = model.sculpture_model()

loaded_model.load_weights('cp-0020.ckpt')
loaded_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=base_learning_rate),
              loss=tf.keras.losses.SparseCategoricalCrossentropy (),
              metrics=['accuracy'])



num_px = 64

st.title("Cat classifier application")
img_path = None
img_path = st.file_uploader("upload an image")






if img_path is not None:





    img = image.load_img(img_path, target_size = (160, 160))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)
    imshow(img)

    prediction = loaded_model.predict(x)
    prob = max(prediction[0])
    class_names = ['buddha', 'lakshmi', 'monivong', 'shiva', 'vishnu']
    Class =  class_names[np.argmax(prediction)]
    
    st.text(f"This picture is a picture of {Class}")
    st.text(f"with {prob} %")
    st.image(img)
