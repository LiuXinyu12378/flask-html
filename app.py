from flask import Flask, render_template, request

import os
import pickle


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/getNER', methods=['POST'])
def getNER():
    source = request.form.get('source')

    return source

@app.route('/get_data', methods=["POST"])
def getPer():
    title = request.form.get('title')
    nums = request.form.get('nums')
    max_len = request.form.get('max_len')

    return title+nums+max_len


@app.route('/getOrg', methods=["POST"])
def getOrg():
    source = request.form.get('org')

    return "asdfas"


if __name__ == '__main__':
    app.run( port='5000', host='127.0.0.1')
