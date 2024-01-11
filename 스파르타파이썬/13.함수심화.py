#특정 매개변수에 디폴트 값을 지정해 줄 수 있음
#인자 개수를 무제한으로 받을 수 있음 
def cal(*args):
  for name in args:
    print(f"{name} 빕막아리")

cal("영수","영희","철수")
# 객체로 받기 **

