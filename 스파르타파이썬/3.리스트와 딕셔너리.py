# 리스트와 딕셔너리는 값을 담는 방법

#1. 리스트의 끝에 원소 담기
a_list = [1,2,34,6]
a_list.append(99)
print(a_list)

#2. 리스트의 [-1] => 무조건 마지막 값 반환

#3. 리스트 정렬 
b_list = [1,5,2,75,12]
b_list.sort()
#내림차순 => .sort(reverse.True)
print(b_list)

#4. 원하는 값이 있는지 확인하기 (확인하고싶은 값 in 리스트)

# 딕셔너리
a_dict = {"name" : 'bob' , "age" : "21"}
result = a_dict["name"] # a_dict이라는 딕셔너리의 name이라는 키의 값을 가져와라 


#1. 딕셔너리에 특정 값 넣기 

a_dict["height"] = 180
print(a_dict)

#2. 딕셔너리에 값 있는지 확인하고 싶을 때
result = ("height" in a_dict) 
print(result)

#3. 퀴즈
people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

print(people[2]["score"]["science"])