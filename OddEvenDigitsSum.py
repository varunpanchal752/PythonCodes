def oddEvenSum(n):
  num=[]
  oddSum=0
  evenSum=0
  while n>0:
    num.append(int(n%10))
    n=int(n/10)
  for i in num:
    if i % 2 == 0:
      evenSum=evenSum+i
    else:
      oddSum=oddSum+i
  print(evenSum,oddSum)

n = int(input("Enter an integer : "))
oddEvenSum(n)
