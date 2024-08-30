#점수들 입력받기
Math = float(input ("수학점수를 입력하세요:"))

Kor = float(input ("국어점수를 입력하세요:"))

Inf = float(input ("정보점수를 입력하세요:"))

#총합구하기

print("총합:",Math + Kor + Inf)

#평균구하기

print ("평균 점수:", round((Math + Kor + Inf)/3))