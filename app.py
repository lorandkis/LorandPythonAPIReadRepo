"""
-------------------------------------------------------
[Program Discription]
-------------------------------------------------------
Author: Lorand Kis
ID: 210629580
Email: kisx9580@mylaurier.ca
__updated__ = "2023-01-12"
-------------------------------------------------------
"""
# Imports
import requests
# from flask import Flask, render_template


from flask import Flask, render_template, url_for, request


def readAPI():
    api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(api_url)
    if (response.status_code < 300):
        jRes = response.json()
        print(jRes)
    else:
        jRes = 'Error: ' + str(response.status_code)
    return jRes

# --------Python HTML Interaction-------


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    # buttonTrack = 1  # tracks the number of times the button has been pressed
    return render_template("index.html", name=None)


@app.route('/result', methods=['POST', 'GET'])
def result():

    # output = request.form.to_dict()
    # print(output)
    #buttonTrack = buttonTrack + 1
    print("Result Page")
    # if(buttonTrack % 2 == 0):
    name = str(readAPI())  # output["name"]
    # else:
    # return render_template("index.html")

    return render_template('index.html', name=name)


@app.route('/home', methods=['POST', 'GET'])
def home2():

    return render_template('index.html', name=None)


if __name__ == "__main__":
    app.run(debug=True)

# -----------------End of test----------------
