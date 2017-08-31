# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import abort, redirect, url_for,request,make_response as response
from flask import Flask, request, render_template, abort
import json, time, threading
from gen_tagged_img import  gen_tagged_img

class MyFlask(Flask):
    def get_send_file_max_age(self, name):
        if name.lower().endswith('.js'):
            return 1
        return Flask.get_send_file_max_age(self, name)


app = MyFlask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/')
def hello():
    print('hello action')
    return render_template('hello.html')
#上传页面路径
@app.route('/upload_page/')
def page_jump(name=None):
    return render_template('upload.html', name='name')
#上传路径
@app.route("/upload/img", methods=['GET', 'POST'])
def deal_img():
    f = request.files['upload_file']
    img_id = gen_tagged_img(f,f.filename)
    #获取结果
    return  redirect(url_for('hello',name =img_id))
#json测试
@app.route("/test_json", methods=['GET', 'POST'])
def return_json():
    t = {
        'a': 1,
        'b': 222,
        'c': [3, 4, 5]
    }
    return json.dumps(t)
#上传后返回json
@app.route("/upload_json", methods=['GET', 'POST'])
def upload_json():
    result = {
        'result' : 1
    }
    file = request.files['upload_file']
    img_id = gen_tagged_img(file,file.filename)
    result['result'] = img_id
    return json.dumps(result)

@app.route("/show_result/<imgid>")
def show_result(imgid):
    print('result action')
    return render_template('result.html',imgid = imgid)
if __name__ == '__main__':

    app.run()
