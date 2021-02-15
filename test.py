from flask import Flask, render_template
import requests
app = Flask(__name__)

# 1. 사용자가 접속할 경로를 작성
@app.route('/')
def hello_world():
  print('hello word')


#수정위해원래코드
@app.route('/service.html')
def service():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기
  menu_db = [
  'BBQ 황금 올리브치킨', 'BHC 뿌링클', '네네치킨 오리엔탈파닭', '교촌치킨 레드콤보', '페리카나 양념치킨', '굽네치킨 고추바사삭', '호식이두마리치킨 매운간장치킨', 'BHC 맛초킹',
  '파파존스 수퍼파파스', '도미노 베스트콰트로', '피자스쿨 고구마피자', '피자에땅 달피자', ]

  ans = random.choice(menu_db)
    return render_template('service.html', random_menu=ans)