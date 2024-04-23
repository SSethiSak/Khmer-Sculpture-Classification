1. Introduction 

This project aims to accurately predict input images of sculptures and return the correct label/name of the input image. The tool used for this task will be a Deep Convolutional Neural Network trained on image data that reflect real world use-case as well as a technique called Transfer Learning. As there is no freely available data of Cambodia’s Historical Sculptures, the data would have to be manually collected, cleaned, and organized for this project.  

2. Data Collection
As there is virtually no available abundance of Cambodian sculpture dataset, this project would require me the collect every data myself and that is no easy task. So, I have decided to limit the scope of this project to just classifying sculpture in the Cambodia National Museum. As a neural network requires a lot of data, taking hundreds of pictures of each sculpture in the museum by myself is not a viable option; so, I have decided to do it differently. By taking video of each sculpture while moving around slightly and moving the camera from many different angles, I can later process that video and capture a certain amount of frame per second as images using python. By doing this and capturing 3 frames per second, I was able to collect over 2000 images of sculptures belonging to 11 different classes. In addition to those 11 classes of data, i have also created 1 additional class called the ‘unknown class’ which contains random images of objects, sculptures, and statues that do not belong to my 11 classes of sculptures. By doing this, the network can also learn which image does not belong to any class instead of blindly guessing that it belongs to a random class.
https://colab.research.google.com/drive/1av7MHdwuVGiK-96lvOAVT8g6ZCh8Tb4D?usp=sharing

3. Model training
train the model on colab and save the models and weight after training is done for implementing into a flask application.
https://colab.research.google.com/drive/1_SmNI6jUGS-uxSDbjfKmJxMV7lcmgxW2?usp=sharing
(model is provided in this repository)

4. flask application
   To run this application:
   -clone this repository
   -install all the neccesary library
   -run app.py or alternatively run "flask run" in terminal on the directory of the cloned repository.
   -click on the ip link in terminal or alternatively navigate to http://127.0.0.1:5000 on any browser
