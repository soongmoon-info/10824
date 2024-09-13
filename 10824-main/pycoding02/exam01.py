#라이브러리 불러오기
import math

#점수들 입력받기
Math = float(input ("수학점수를 입력하세요:"))

Kor = float(input ("국어점수를 입력하세요:"))

Inf = float(input ("정보점수를 입력하세요:"))

#총합구하기

Sum = Math+ Kor + Inf

print("총합:",Math + Kor + Inf)

#평균구하기

Avr = (Math + Kor + Inf)/3

print ("평균 점수:", math.floor((Math + Kor + Inf)/3))

#등급구하기
if Avr >= 90:
  print ("등급 : ","A")
elif Avr >= 80 :
  print ("등급 : ","B")
else :
  print ("등급 : ","C")
