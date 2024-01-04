# if 조건문 : 조건이 True 일때만 들여쓰기 안쪽의 문장을 실행
if 조건: 복합문장
  # 복합문장 : 문장을 묶어 놓은 것 

아오.. 왜 중괄호 안쓰냐고 파이썬... 
  
if Ture:
  문장
  문장
  문장

# ex 사용자가 입력한 숫자가 양수/ 음수/ 0 인지 판별하는 프로그램
raw_input = input("정수를 입력하세요: ")
raw_input = int(raw_input)

if raw_input > 0 :
  print("양수입니다.")

if raw_input < 0 :
  print("음수입니다.")

if raw_input == 0 :
  print("0입니다.")