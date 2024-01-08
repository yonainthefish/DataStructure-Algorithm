number = [123,54,657,8768,53,3]

for number in numbers:
  #홀수짝수
  if number % 2  == 0:
    print(f"{number}는 짝수입니다.")
  else :
    print(f"{number}는 홀수입니다.")

  #자릿수 출력
    print(f"{number}는 {len(str(number))}자리입니다.")
    print()