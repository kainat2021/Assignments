import random
array=[]
for i in range(101):
    array.append(random.randint(1,10000))
print("\nEnter your operation you want to perform on the list:\n")
print("1) Find the Minimum number.")
print("2) Find the Maximum number.")
print("3) Find the Average of numbers.\n")
choice=int(input())
print("\n")
if choice==1:
    min=array[0]
    for i in range(len(array)):
       if min>array[i]:
          min=array[i]
    print("Minimum number in the list is ",min,"at the index",array.index(min),"\n")
elif choice==2:
    max=array[0]
    for i in range(len(array)):
       if max<array[i]:
          max=array[i]
    print("Maximum number in the list is ",max,"at the index",array.index(max),"\n")
elif choice==3:
    avg=0
    sum=0
    for i in range(len(array)):
        sum+=array[i]
    avg=sum/len(array)
    print("Average of numbers in list is",avg,"\n")
else:
    print("Invalid option")
