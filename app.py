import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route('/submit', methods=['POST'])
def submit():

    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text = "The Attack Type is {}".format(prediction))
    
if __name__ == "__main__":
    flask_app.run(debug=True)
    #icmp:0 tcp:1 udp:2
    #SF:9 SO:5 REJ:1 RSTR:4 RSTO:2 SH:10 S1:6 S2:7 RSTOS0:3 S3:8 OTH:0
    