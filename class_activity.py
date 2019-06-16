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