num=[]
def findMiss(num):
    distinct = {*num}
    index = 1
    while True:
        if index not in distinct:
            return index
        index += 1
 

n=int(input("enter the count of total values: "))
print("enter the",n,"values")
for i in range(n):
  k=int(input("Enter one value at a time :"))
  num.append(k)
print(num)111
if __name__ == '__main__':
    print('The smallest positive natural number missing from the list is : ',
        findMiss(num))
