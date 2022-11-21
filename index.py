from flask import Flask, render_template
from requests import get, exceptions
import time

app = Flask(__name__)

@app.route("/")
def home():

    while True:
        render_template("ping.html")
        ping()
        time.sleep(10)
        #server_close()
           

    return 

def ping():

    try:
        a = get('http://148.226.212.2', timeout = 5)
        print('UDICA ', a)

    except exceptions.ConnectionError:
        print('UDICA MUERTO: ', 0)

    try:
        b = get('https://8.8.8.8', timeout = 5)
        print('GOOGLE ', b)

    except exceptions.ConnectionError:
        print('GOOGLE MUERTO: ', 0)

    try:
        c = get('http://148.226.129.2', timeout =5)
        print('VETERINARIA ', c)

    except exceptions.ConnectionError:
        print('VETERINARIA MUERTO: ', 0)


if __name__ == '__main__':
    app.run()
    