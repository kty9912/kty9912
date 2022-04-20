from audioop import add
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

#url을 추가해서 def를 실행하는 법
@app.route('/second/')
def  second():
    return "Second Page"

app.run