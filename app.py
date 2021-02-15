from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

@app.route('/')
def home():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기
    return render_template('home.html')

@app.route('/home.html')
def home2():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기
    return render_template('home.html')


@app.route('/service_intro.html')
def service_intro():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기
    return render_template('service_intro.html')

# render_template 사용해보기
# == 사용자에게 보여줄 데이터를 HTML에 담기
# @app.route('/service.html')
# def service():
#     # HTML 반환해주기
#     # 반드시 templates 폴더 안에 위치해야합니다.
#     # render_template 불러와주기
#     menu_db = [
#     'BBQ 황금 올리브치킨', 'BHC 뿌링클', '네네치킨 오리엔탈파닭', '교촌치킨 레드콤보', '페리카나 양념치킨', '굽네치킨 고추바사삭', '호식이두마리치킨 매운간장치킨', 'BHC 맛초킹',
#     '파파존스 수퍼파파스', '도미노 베스트콰트로', '피자스쿨 고구마피자', '피자에땅 달피자', ]

#     ans = random.choice(menu_db)
#     return render_template('service.html', random_menu=ans)
@app.route('/service.html')
def service():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기
    menu_db = ['후라이드치킨', '갈릭파스타']
    menu_photo = {'후라이드치킨' : '../static/images/fried_chicken.png', '갈릭파스타' : '../static/images/garlic_pasta.png',}

    ans = random.choice(menu_db)
    return render_template('service.html', random_menu=ans, random_menu_photo=menu_photo[ans])   



# 파일 수정 시, 자동으로 반영해주는 코드
# 서버 껐다킬 필요 없음.
# 이제부터 python app.py로 서버 실행!
if __name__ == '__main__':
    app.run(debug=True)