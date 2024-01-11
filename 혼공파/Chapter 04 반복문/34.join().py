# () 를 통해 해결하기 but 파이썬에만 있고, 파이썬 문법 중에서도 좀 마니아하다. 

number = int(input("정수입력"))

if number % 2 == 0:
  print((
    f"입력한 문자열은 {number}입니다. \n"
    f"{number}는 짝수입니다."
  ))

# join으로 해결하기 
  print("".join(["A", "B", "C"]))
  # 앞에 있는 걸로 뒤 배열을 이어주는 함수