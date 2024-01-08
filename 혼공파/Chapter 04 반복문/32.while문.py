# while 반복문
while True:
  #복합구문
  #조건이 참이라면 반복


  i = 0
  while i < 10:
    print(f"{i}번째 반복입니다.")
    i += 1  


a = [1,2,1,2]
value = 2

while value in a:
  a.remove(value)
print(a) # [1,1]

#break 키워드 / continue 키워드 
