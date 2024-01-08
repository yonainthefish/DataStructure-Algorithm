# 딕셔너리
변수명 ={
  키:값
  키:깂
  키:값
}

#키 값은 문자열로 문자열이 아니면 변수라고 생각되어 정의하라고 한다.
product = {
  "제품명" : "건망고 슲라이스",
  "가격" : "4000",
  "분류" : "식품"
}

product["제품명"] #건망고 슬라이스
product["가격"] #4000
product["분류"] #식품

for key in product:
  print(key)
  print(product[key])
  print("-" * 20)


  