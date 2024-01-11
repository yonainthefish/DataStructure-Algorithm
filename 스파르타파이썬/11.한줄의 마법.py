#if문 을 간단하게 

num = 3

if num % 2 == 0:
  result = "짝수"
else:
  result = "홀수"

# 위와 같은 값 () 없이도 된다. 
  #result = ("짝수" if num % 2 == 0 else "홀수")

print(f"{num}은 {result}입니다.")

a_list = [1,2,4,6,7,2]
b_list = []

for a in a_list:
  b_list.append(a*2)

b_list = [a*2 for a in a_list]
print(b_list)