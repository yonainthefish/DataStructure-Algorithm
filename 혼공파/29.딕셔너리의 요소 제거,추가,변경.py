product = {
  "name" : "건강한 망고",
  "type" : "당절임",
}

# 요소의 값을 변경하는 방법
product["name"] = "건강한 레몬"
# 요소를 추가하는 방법
product["price"] = "4000"
# 요소를 제거하는 방법
del product["type"]

# 키의 존재를 확인하는 방법
# True or False
if "price" in product:
  print(product["price"])
  
# get()
print(product.get("price"))
=> 딕셔너리에 없는 값은 NONE으로 출력된다. 오류 없이 출력되기 때문에 키의 존재 여부를 찾을 때 쓰기도 한다. 