i = input("입력: ")

if "안녕" in i:
  print("안녕하세요")
elif "몇시" in i:
  from pytz import timezone
  from datetime import datetime
  today = datetime.now(timezone('Asia/Seoul'))
  print(f" 지금은 {today.hour}시 입니다.")
else :
  print(">",i)

# 나누어 떨어지는 숫자
  i = int(input("입력: "))
  if i % 2 == 0 :
    print("2로 나누어 떨어지는 숫자 입니다.")
  else :
    print("2로 나누어 떨어지는 숫자가 아닙니다.")