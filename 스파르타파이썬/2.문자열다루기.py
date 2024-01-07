# 숫자를 문자열로 바꾸고 싶을 때 쓰는 함수 str()
a = "2"
b = str(2)

#print(a+b)


text = "abcdefghijk"

# 문자열 길이세기 => len(변수명)
result = len(text)
print(result)

# 문자열 자르기 => [:자르고싶은 문자의길이]
# 처음부터 3까지
result = text[:3]
# 3부터 끝까지 
result = text[3:]
print(result)
# 3 부터 8 까지 
result = text[3:8]
print(result)

# split()
myEmail = "abe@sparta.co"
result = myEmail.split('@')[1].split('.')[0]
print(result)

#퀴즈
text = "sparta"
result = text[:3]
print(result)

phone = '02-123-1234'
result = phone.split("-")[0]
print(result)