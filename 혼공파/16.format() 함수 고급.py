#정수를 규격화 하여 출력하기 
"{:d}".format(52)

# 특정 칸만큼 출력
print("{{:5d}".format(52))  =>     52 
print("{{:10d}".format(52)) =>          51

print("{{:05d}".format(52))  => 0000052
print("{{:010d}".format(52)) => 000000000052


#부동소숫점 
print("{{:=+20.1f}".format(52)) =>                   52.0
print("{{:=+20.2f}".format(52)) =>                  52.00
print("{{:=+20.3f}".format(52)) =>                 52.000
!. 자동 반올림 된다. 
print("{:.1f}".format(52.37)) => 52.3