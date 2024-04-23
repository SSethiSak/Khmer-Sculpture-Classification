import model
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.preprocessing import image
import cv2
from flask import Flask, redirect, render_template, request
import base64
from info_fetch import info


app = Flask(__name__)


base_learning_rate = 0.0003
loaded_model = model.sculpture_model()

loaded_model.load_weights("efficientnet_untuned_96.h5")
loaded_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=base_learning_rate),
                loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                metrics=['accuracy'])



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
       pass
    else:
        return render_template("predict.html")
    
@app.route("/result", methods = ["GET", "POST"])
def result():
    if 'image_file' not in request.files:
        return redirect('/')  

    file = request.files['image_file']


    img_stream = file.stream.read()
    img_array = np.frombuffer(img_stream, np.uint8)  
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    retval, buffer = cv2.imencode('.jpg', img) 
    img_as_base64 = base64.b64encode(buffer).decode('utf-8')
    test = 2

    img_array = np.frombuffer(img_stream, np.uint8) 
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  


    img = cv2.resize(img, (256, 256))  


    img = tf.keras.preprocessing.image.img_to_array(img)  
    img = np.expand_dims(img, axis=0) 
    img = tf.keras.applications.efficientnet.preprocess_input(img)
    Class_label, prob = predict(img)
    prob = int(prob * 100)

    pic, desc, desc2, content = info(Class_label)
    return render_template("result.html", Class = Class_label, prob = prob, image=img_as_base64, pic1 = pic, desc = desc, desc2 = desc2, content = content) # Or display the processed image





def predict(img):


    prediction = loaded_model.predict(img)
    prob = max(prediction[0])
    class_names = ['Brahma', 'Buddha', 'Ganesha', 'Hanuman', 'Harihara', 'Jayavarman_VII', 'Lakshmi', 'Lokeshvara', 'Monivong', 'Shiva', 'Vishnu', 'unknown_class']
    Class =  class_names[np.argmax(prediction)]
    return Class, prob

    




if __name__ == '__main__':  
   app.run(debug=True)