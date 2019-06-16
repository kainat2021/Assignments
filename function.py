def greet(): #function definition
  print("Good Morning")
greet() #function calling
print("I am outside the function")
greet()
print("Completed")
a=int(input("Enter number 1 :"))
b=int(input("Enter number 2 :"))
choice=int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Divison"))
def add(num1,num2): #Recieving info/data
     my_sum=num1+num2
     print("Answer of addition of ",num1," and ",num2, " is ",my_sum)
def sub(num1,num2):
     subtract=num1-num2
     print("Answer of subtraction of ",num1," and ",num2, " is ",subtract)
def mul(num1,num2):
     mult=num1*num2
     print("Answer of multiplication of ",num1," and ",num2, " is ",mult)
def div(num1,num2):
     divide=num1/num2
     print("Answer of divsion of ",num1," and ",num2, " is ",divide)
if choice==1:
    add(a,b) #passing  data called arguements
elif choice==2:
    sub(a,b)
elif choice==3:
    mul(a,b)
elif choice==4:
    div(a,b)
# def my_pet(owner,pet,city="Karachi"):
#     print(owner," is an owner of ",pet)
# my_pet(pet="Cat",owner="Sarah")
# def sum():
#     a=2
#     b=3
#     return(a+b)
# result=sum()
# print(result)
# def sum(val1,val2):
#     result=val1+val2
#     return result
# output_of_function=sum(a,b)
# print(output_of_function)
def checkeven(val):
    if val%2==0:
         return True
    else:
         return False
def checkodd(val):
    if val%2!=0:
         return True
    else:
         return False
choice=int(input("Tell whether you want to check even or odd\n1.even\n2.odd\n"))
num=int(input("Enter number to check: "))
if choice==1:
    result_even=checkeven(num)
    print(result_even)
elif choice==2:
    result_odd=checkodd(num)
    print(result_odd)
    

