#반복문

fruits = ["사과" , "배", "딸기"]
for fruit in fruits:
  print(fruit)

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for i,person in enumerate(people):
  name = person["name"]
  age = person["age"]
  #print(i,name,age)
  if i > 2:
    break # 커지는 순간의 값 "까지" 반환 

# 연습문제 1
  num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
  for even in num_list:
    if even % 2 == 0:
      print(even)

# 연습문제 2
  num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
  result = 0
  for num in num_list:
    if(num % 2 == 0):
      result += 1
      # print(result)

# 연습문제 3
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
result2 = 0 
for num in num_list:
    result2 += num
print(result2)

#연습문제 4
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
sort_list = sorted(num_list)
print(sort_list[-1])