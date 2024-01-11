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

def check_adult(person):
  return "성인" if person["age"] > 20 else "청소년"

result = map(check_adult, people)
# 2. filter => True인 것만 뽑아오는 애들 
  # result = filter(lamda x:x["age"] > 20. people)
# 3. lamda => result = map(lamda person:("성인" if person["age"] > 20 else "청소년"),people)
print (list(result))