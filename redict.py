from flask import Flask
from flask import render_template
from flask import abort, redirect, url_for,request,make_response as response
from flask import Flask, request, render_template, abort
import json, time, threading
from gen_tagged_img import  gen_tagged_img
from websocket import create_connection
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/')
def hello():
    print('hello action')
    return render_template('hello.html')

@app.route('/upload_page/')
def page_jump(name=None):
    return render_template('upload.html', name='name')

@app.route("/upload/img", methods=['GET', 'POST'])
def deal_img():
    f = request.files['upload_file']
    img_id = gen_tagged_img(f,f.filename)
    
    return  redirect(url_for('hello',name =img_id))

@app.route("/test_json", methods=['GET', 'POST'])
def return_json():
    t = {
        'a': 1,
        'b': 222,
        'c': [3, 4, 5]
    }
    t['a'] = 000;
    return json.dumps(t)

if __name__ == '__main__':

    app.run()
