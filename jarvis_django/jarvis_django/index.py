import random

import os

from TTSSample import get_speech
from flask import Flask, request, send_from_directory, render_template
from flask.ext.cors import CORS

# set the project root directory as the static folder, you can set others.
app = Flask(__name__)
CORS(app)

@app.route('/ping')
def elb_ping():
    return "hello"

@app.route('/')
def index():
    return render_template("index.htm")

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    try:
        question = request.form["question"]
        user_name = request.form["userName"]
        latitude = request.form["lat"]
        langitude = request.form["lang"]

        if question == '':
            data = get_speech("Hello, Welcome " + user_name)
        elif ("samba" in question) or ("masuri" in question) or ("BPT" in question) or ("seed" in question) or ("where" in question):
            data = get_speech("samba masuri BPT 5204 is susceptible to major pests and diseases like rice blast "
                              "in your location. "
                              "We recommend sugandha samba as a aromatic and high yield variety.")
        elif ("price" in question) or ("rnr" in question) or ("what" in question):
            data = get_speech("The price per bag for sugandha samba last season was rupees 1500")
        elif "weather" in question:
            data = get_speech("Forecast for tomorrow is maximum temperature 40 degree celsius "
                              "and minimum temperature 26 degree celsius")
        else:
            data = get_speech("Hi " + user_name + " " + "We will get back to you soon regarding this query")

        root = os.path.dirname(__file__)
        file_name = os.path.join(root, "static")
        file_name = os.path.join(file_name, "temp.wav")

        file = open(file_name, "wb")
        file.write(data)

        return "/static/temp.wav?xyz=" + str(random.randint(1, 10000000))
    except Exception:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
