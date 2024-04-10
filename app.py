import numpy as np


from flask import Flask, request, jsonify, render_template
import pickle
#fcntl()
# Create flask app
flask_app = Flask(__name__,template_folder='template')
model = pickle.load(open("boost_pkl", "rb"))

@flask_app.route("/")
def home():
    return render_template("index.html")
@flask_app.route("/predict", methods = ["POST"])
def predict():
    
    float_features = [float(x)  for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    #predictionfinal1=int()
    predictionfinal=int(prediction[0])
  
         
    #return render_template('index.html',prediction=prediction[0])
    return render_template('index.html', prediction = "The time required for food Delivery is  {} Minutes".format(predictionfinal))   
if __name__ == "__main__":
    flask_app.run(debug="True",port=8080)
    