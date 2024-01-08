# for 반복문
# for 반복변수 in 리스트 :


# 복합구문
a = [1,2,3,4,5]

# 반복변수 : a의 요소가 하나하나
for a_i in a:
  print(a_i)

#예제 
a = [1,2,3,4,5]

# 1) 총합 
sum = 0 
for a_i in a :
  sum = sum + a_i
  print(sum)

# 2) 총곱
prod = 1
for a_i in a :
  prod = prod * a_i
  print(prod)
