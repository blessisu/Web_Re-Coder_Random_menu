import random
menu_db = [
  'BBQ 황금 올리브치킨', 'BHC 뿌링클', '네네치킨 오리엔탈파닭', '교촌치킨 레드콤보', '페리카나 양념치킨', '굽네치킨 고추바사삭', '호식이두마리치킨 매운간장치킨', 'BHC 맛초킹',
  '파파존스 수퍼파파스', '도미노 베스트콰트로', '피자스쿨 고구마피자', '피자에땅 달피자', ]

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