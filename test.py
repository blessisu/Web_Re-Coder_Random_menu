from flask import Flask, render_template
import requests
app = Flask(__name__)

# 1. 사용자가 접속할 경로를 작성
@app.route('/')
def hello_world():
  print('hello word')