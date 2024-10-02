# i = 0

# while i < 3 :
#   print(i)
#   i = i+1
# print ("이거 끝나면 정리하고 가자")


# for i in range (0,3,1) :
#   print (i)
  
  
# for i in range (0,3) :
#   print (i)
  
# for i in range (3) :
#   print (i)



# print (list(range(0,3,1)))

# a = ['사과', '배', '귤', '샤인머', '망고']
# for i in a: 
#   print (i)
  
#   if i == '귤':
#     print ("귤 찾음")
#     continue
#     print (i)


a = ['사과', '배', '귤', '샤인머', '망고']
for index, value in enumerate(a):
  if value == '배':
    a [index] = 0
  
print (a)
