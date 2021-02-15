
#이미지를 겹치지 않게 하려면 어떻게해야할까?
#실제서버랑연결시키는법?
#로딩화면은 html을 따로 만드는걸까..? type error 로 거르는 것..?

@app.route('/service.html')
def service():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기
    menu_db = ['후라이드치킨', '갈릭파스타']
    menu_photo = {'후라이드치킨' : '../static/images/fried_chicken.png', '갈릭파스타' : '../static/images/garlic_pasta.png',}

    ans = random.choice(menu_db)
    return render_template('service.html', random_menu=ans, random_menu_photo=menu_photo[ans])



def random():
  random.shuffle(menu_db)
  index = 0
  while index < len(menu_db):
    ans = False
    print(menu_db[index])
    if ans:
      return menu_db
    index += 1
    # 사용자가 ans를 True라고 답할 때까지 shuffle된 메뉴 계속해서 show해주기