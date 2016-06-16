import os
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from jarvis_django.TTSSample import get_speech


def elb_ping(request):
    return HttpResponse("ping")


def index(request):
    return render(request, "index.html")

def demo(request):
    return render(request, "demo.html")

@csrf_exempt
def text_to_speech(request):
    try:
        question = request.POST["question"]
        user_name = request.POST["userName"]
        latitude = request.POST["lat"]
        langitude = request.POST["lang"]

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

        root = os.path.dirname(os.path.dirname(__file__))
        file_name = os.path.join(root, "static")
        file_name = os.path.join(file_name, "temp.wav")

        file = open(file_name, "wb")
        file.write(data)

        return HttpResponse("/static/temp.wav?xyz=" + str(random.randint(1, 10000000)))
    except Exception as e:
        print(str(e))
        return str(e)

