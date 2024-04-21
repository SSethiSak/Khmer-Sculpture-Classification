import model
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image
from tensorflow.keras.preprocessing import image
import cv2
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date, datetime
import base64

app = Flask(__name__)


base_learning_rate = 0.005
loaded_model = model.sculpture_model()

loaded_model.load_weights('Model_weights_ver2.h5')
loaded_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=base_learning_rate),
                loss=tf.keras.losses.SparseCategoricalCrossentropy (),
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
        return redirect('/')  # Or a suitable error message

    file = request.files['image_file']

    # Load the image using OpenCV (cv2)
    img_stream = file.stream.read()
    img_array = np.frombuffer(img_stream, np.uint8)  # Convert to NumPy array
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    retval, buffer = cv2.imencode('.jpg', img) 
    img_as_base64 = base64.b64encode(buffer).decode('utf-8')
    test = 2
    # Image processing with NumPy
    # ... your image processing code using 'img' ...
    img = Image.open(file.stream)
    img = img.resize((160, 160))  # Resize to the target size
    x = image.img_to_array(img)    # Convert to NumPy array
    x = np.expand_dims(x, axis = 0) 
    Class_label, prob = predict(x)
    prob = int(prob * 100)
    
    pic, desc, desc2, content = info(Class_label)
    e = 12
    return render_template("result.html", Class = Class_label, prob = prob, image=img_as_base64, pic1 = pic, desc = desc, desc2 = desc2, content = content) # Or display the processed image





def predict(img):


    prediction = loaded_model.predict(img)
    prob = max(prediction[0])
    class_names = ['Buddha', 'Lakshmi', 'Monivong', 'Shiva', 'unknown_class', 'Vishnu']
    Class =  class_names[np.argmax(prediction)]

    return Class, prob

    


def info(class_name):
    if class_name == "unknown_class":
        pic = "static/unknown_pic.jpg"
        desc = "Unknown Image. please select or take a valid image.\n the image you provided is either an image of sculpture unlabeled by this application yet or is an image unrelated to this application usage."
        desc2 = "please select or take a valid image.\n the image you provided is either an image of sculpture unlabeled by this application yet or is an image unrelated to this application usage."
        content = "No information"
        return pic, desc, desc2, content
        e = 2
    pic = f"static/{class_name}_pic.jpg"
    if class_name == "Vishnu":
        desc = "Vishnu is one of the principal deities of Hinduism, known as the Preserver within the Trimurti (the Hindu trinity). Vishnu is believed to embody compassion and protection, and he periodically takes on earthly avatars to restore balance to the world."
        desc2 = "Hinduism reached Southeast Asia, including Cambodia (formerly known as Khmer Empire), around the 1st century CE. Vishnu quickly became a prominent deity, alongside Shiva, the Destroyer.Khmer kings associated themselves with Vishnu, claiming divine authority through their connection to the preserver god. This association helped solidify their rule and promote social order."

        
    
    elif class_name == "Lakshmi":
        desc = "Lakshmi is the Hindu goddess of wealth, fortune, and prosperity. She is a symbol of beauty, abundance, and auspiciousness."
        desc2 = "Lakshmi's importance lies in her association with wealth and material prosperity – essential aspects Khmer kings sought for their kingdom.Lakshmi's grace and regal iconography resonated with depictions of powerful queens, highlighting their importance in maintaining social harmony and prosperity within the kingdom."


    elif class_name == "Shiva":
        desc = "Shiva is one of the supreme deities of Hinduism, known as 'The Destroyer' within the Trimurti. Despite his destructive association, Shiva also represents transformation, rejuvenation, and the cycle of life and death."
        desc2 = "Unlike other regions where Vishnu held equal or greater importance, Shiva reigned supreme in the Khmer pantheon. He was seen as the source of all creation and the ultimate force behind change and transformation.Khmer kings identified with Shiva's ascetic aspects, such as self-discipline and yogic practices. This association reflected the ideal of a righteous and dedicated ruler who ensured prosperity for his people."

        
    elif class_name == "Monivong":
        desc = "Sisowath Monivong was the King of Cambodia from 1927 until his death in 1941, ruling during the period of French colonial influence."
        desc2 = "Monivong took a strong interest in preserving and revitalizing Khmer culture. He supported the study of Khmer history, the arts, and the restoration of important historical sites.While politically limited, Monivong supported some social and administrative reforms, aiming to modernize Cambodia within the constraints of the colonial system."

    
    elif class_name == "Buddha":
        desc = "The Buddha, originally named Siddhartha Gautama, was a spiritual teacher who lived in ancient India.His teachings form the foundation of Buddhism, a major world religion emphasizing mindfulness, compassion, and the end of suffering."
        desc2 = "Early depictions of Buddha in Khmer art show the influence of Indian and Southeast Asian styles. Later periods reflect distinct Khmer artistic interpretations of the Buddha's form, often serene and meditative.Khmer depictions of Buddha incorporate traditional Buddhist iconography such as the ushnisha (cranial bump), elongated earlobes, mudras (hand gestures), and the lotus flower representing purity."



    with open(f"text/{class_name}.txt", "r") as file: 
        content = "".join(line for line in file)

        
    return pic, desc, desc2, content