
print("\nCoded By Kainat Aijaz\n")
choice=int(input("What did you choose in 9th? Enter 1 for Biology and 2 for Computer?"))
if choice==1:
    final="Biology"
elif choice==2:
    final="Computer"
sindhi=int(input("Enter your Sindhi marks out f 75:"))
pst=int(input("Enter your Pakistan Studies marks out of 75:"))
eng=int(input("Enter your English marks out of 75:"))
chem=int(input("Enter your Chemistry marks out of 100:"))
print("Enter your ",final," marks out of 100:")
fin=int(input())
percent=((sindhi+pst+eng+chem+fin)/425)*100
print(" =================================================")
print("                 9th MarkSheet                    ")
print(" =================================================")
print("\n")
print("ENGLISH : ",eng,"                 SINDHI : ",sindhi,"\n")
print("CHEMISTRY : ",chem,"               P.ST : ",pst,"\n")
print(final,":",fin, "\n")
print(" =================================================")
if percent>=80:
    print("Congratulations you got A+ grade with ",percent,"%")
elif percent<=79 & percent>=70:
    print("Good! you got A grade with ",percent,"%")
elif percent<=69 & percent>=60:
    print("Good! you got B grade with ",percent,"%")
elif percent<=59 & percent>=50:
    print("Good! you got C grade with ",percent,"%")
else:
    print("You are fail with  ",percent,"%")
print(" =================================================/n")