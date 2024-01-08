

# 연습문제 
def check_gender(pin):
  num = pin.split("-")[1][:1]
  if int(num) % 2 == 0:
    print("여성")
  else:
    print("남성")

check_gender("150105-1010203")
check_gender("150105-2010203")  
check_gender("150105-4010203")

