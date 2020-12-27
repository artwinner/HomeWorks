import sys

lessons=("Calculus","Diff","Quantum","Fundementals of Electric Circuit","Music")
students=["SAMET","SATIROGLU"]


while True :
    name=str(input("Name:")).upper()
    surname=str(input("Surname:")).upper()
    if name==students[0] and surname==students[1]:
        print("Welcome %s %s "%(name,surname))
        break
    elif name != students[0] or surname != students[1]:
        name=str(input("Name:")).upper()
        surname=str(input("Surname:")).upper()
        if name==students[0] and surname ==students[1]:
            print("Welcome %s %s "%(name,surname))
            break
        elif name != students[0] or surname != students[1]:
            name=str(input("Name:")).upper()
            surname=str(input("Surname:")).upper()
            if name==students[0] and surname ==students[1]:
                print("Welcome %s %s "%(name,surname))
                break
            else:
                print("Please Try Again Later")
                sys.exit()

print(lessons)
choose=int(input("How many lessons do you want to add? (You must add at least 3 lessons!!)"))
if choose < 3:
    print("You failed!")
    sys.exit()

if choose==3:
    l1=str(input("1. lesson:")).upper()
    l1m=int(input(f"{l1} Midterm:"))
    l1f=int(input(f"{l1} Final:"))
    l1p=int(input(f"{l1} Project:"))
    l1a=int((l1m*0.3)+(l1f*0.5)+(l1p*0.2))
    if l1a>=90 and l1a<=100:
        harf='AA'
    elif l1a>=70 and l1a<90:
        harf='BB'
    elif l1a>=50 and l1a<70:
        harf='CC'
    elif l1a>=30 and l1a<50:
        harf='DD'
    else:
        harf='FF'
    if harf=="FF":
        print(f"{l1} grade:"+harf)
        print(f"You failed {l1}")
    with open("Results.txt","a",encoding="utf-8") as file:
        file.write('='*18+'\n'+str(name)+' '+str(surname)+'\n'+str(l1)+' Midterm:'+str(l1m)+'\n'+str(l1)+' Final:'+str(l1f)+'\n'+str(l1)+' Project:'+str(l1f)+'\n'+str(l1)+' Grade:'+str(harf)+'\n'+'='*18+'\n')
    l2=str(input("2. lesson:")).upper()
    l2m=int(input(f"{l2} Midterm:"))
    l2f=int(input(f"{l2} Final:"))
    l2p=int(input(f"{l2} Project:"))
    l2a=int((l2m*0.3)+(l2f*0.5)+(l2p*0.2))
    if l2a>=90 and l2a<=100:
        harf='AA'
    elif l2a>=70 and l2a<90:
        harf='BB'
    elif l2a>=50 and l2a<70:
        harf='CC'
    elif l2a>=30 and l2a<50:
        harf='DD'
    else:
        harf='FF'
    if harf=="FF":
        print(f"{l2} grade:"+harf)
        print(f"You failed {l2}")
    with open("Results.txt","a",encoding="utf-8") as file:
        file.write(str(l2)+' Midterm:'+str(l2m)+'\n'+str(l2)+' Final:'+str(l2f)+'\n'+str(l2)+' Project:'+str(l2f)+'\n'+str(l2)+' Grade:'+str(harf)+'\n'+'='*18+'\n')
    l3=str(input("3. lesson:")).upper()
    l3m=int(input(f"{l3} Midterm:"))
    l3f=int(input(f"{l3} Final:"))
    l3p=int(input(f"{l3} Project:"))
    l3a=int((l3m*0.3)+(l3f*0.5)+(l3p*0.2))
    if l3a>=90 and l3a<=100:
        harf='AA'
    elif l3a>=70 and l3a<90:
        harf='BB'
    elif l3a>=50 and l3a<70:
        harf='CC'
    elif l3a>=30 and l3a<50:
        harf='DD'
    else:
        harf='FF'
    if harf=="FF":
        print(f"{l3} grade:"+harf)
        print(f"You failed {l3}")
    with open("Results.txt","a",encoding="utf-8") as file:
        file.write(str(l3)+' Midterm:'+str(l3m)+'\n'+str(l3)+' Final:'+str(l3f)+'\n'+str(l3)+' Project:'+str(l3f)+'\n'+str(l3)+' Grade:'+str(harf)+'\n'+'='*18+'\n')
elif choose==4:
    l1=str(input("1. lesson:")).upper()
    l1m=int(input(f"{l1} Midterm:"))
    l1f=int(input(f"{l1} Final:"))
    l1p=int(input(f"{l1} Project:"))
    l1a=int((l1m*0.3)+(l1f*0.5)+(l1p*0.2))
    if l1a>=90 and l1a<=100:
        harf='AA'
    elif l1a>=70 and l1a<90:
        harf='BB'
    elif l1a>=50 and l1a<70:
        harf='CC'
    elif l1a>=30 and l1a<50:
        harf='DD'
    else:
        harf='FF'
    if harf=="FF":
        print(f"{l1} grade:"+harf)
        print(f"You failed {l1}")
    with open("Results.txt","a",encoding="utf-8") as file:
        file.write('='*18+'\n'+str(name)+' '+str(surname)+'\n'+str(l1)+' Midterm:'+str(l1m)+'\n'+str(l1)+' Final:'+str(l1f)+'\n'+str(l1)+' Project:'+str(l1f)+'\n'+str(l1)+' Grade:'+str(harf)+'\n'+'='*18+'\n')
    l2=str(input("2. lesson:")).upper()
    l2m=int(input(f"{l2} Midterm:"))
    l2f=int(input(f"{l2} Final:"))
    l2p=int(input(f"{l2} Project:"))
    l2a=int((l2m*0.3)+(l2f*0.5)+(l2p*0.2))
    if l2a>=90 and l2a<=100:
        harf='AA'
    elif l2a>=70 and l2a<90:
        harf='BB'
    elif l2a>=50 and l2a<70:
        harf='CC'
    elif l2a>=30 and l2a<50:
        harf='DD'
    else:
        harf='FF'
    if harf=="FF":
        print(f"{l2} grade:"+harf)
        print(f"You failed {l2}")
    with open("Results.txt","a",encoding="utf-8") as file:
        file.write(str(l2)+' Midterm:'+str(l2m)+'\n'+str(l2)+' Final:'+str(l2f)+'\n'+str(l2)+' Project:'+str(l2f)+'\n'+str(l2)+' Grade:'+str(harf)+'\n'+'='*18+'\n')
    l3=str(input("3. lesson:")).upper()
    l3m=int(input(f"{l3} Midterm:"))
    l3f=int(input(f"{l3} Final:"))
    l3p=int(input(f"{l3} Project:"))
    l3a=int((l3m*0.3)+(l3f*0.5)+(l3p*0.2))
    if l3a>=90 and l3a<=100:
        harf='AA'
    elif l3a>=70 and l3a<90:
        harf='BB'
    elif l3a>=50 and l3a<70:
        harf='CC'
    elif l3a>=30 and l3a<50:
        harf='DD'
    else:
        harf='FF'
    if harf=="FF":
        print(f"{l3} grade:"+harf)
        print(f"You failed {l3}")
    with open("Results.txt","a",encoding="utf-8") as file:
        file.write(str(l3)+' Midterm:'+str(l3m)+'\n'+str(l3)+' Final:'+str(l3f)+'\n'+str(l3)+' Project:'+str(l3f)+'\n'+str(l3)+' Grade:'+str(harf)+'\n'+'='*18+'\n')
    l4=str(input("4. lesson:")).upper()
    l4m=int(input(f"{l4} Midterm:"))
    l4f=int(input(f"{l4} Final:"))
    l4p=int(input(f"{l4} Project:"))
    l4a=int((l4m*0.3)+(l4f*0.5)+(l4p*0.2))
    if l4a>=90 and l4a<=100:
        harf='AA'
    elif l4a>=70 and l4a<90:
        harf='BB'
    elif l4a>=50 and l4a<70:
        harf='CC'
    elif l4a>=30 and l4a<50:
        harf='DD'
    else:
        harf='FF'
    if harf=="FF":
        print(f"{l4} grade:"+harf)
        print(f"You failed {l4}")
    with open("Results.txt","a",encoding="utf-8") as file:
        file.write(str(l4)+' Midterm:'+str(l4m)+'\n'+str(l4)+' Final:'+str(l4f)+'\n'+str(l4)+' Project:'+str(l4f)+'\n'+str(l4)+' Grade:'+str(harf)+'\n'+'='*18+'\n')
else:
    l1=str(input("1. lesson:")).upper()
    l1m=int(input(f"{l1} Midterm:"))
    l1f=int(input(f"{l1} Final:"))
    l1p=int(input(f"{l1} Project:"))
    l1a=int((l1m*0.3)+(l1f*0.5)+(l1p*0.2))
    if l1a>=90 and l1a<=100:
        harf='AA'
    elif l1a>=70 and l1a<90:
        harf='BB'
    elif l1a>=50 and l1a<70:
        harf='CC'
    elif l1a>=30 and l1a<50:
        harf='DD'
    else:
        harf='FF'
    if harf=="FF":
        print(f"{l1} grade:"+harf)
        print(f"You failed {l1}")
    with open("Results.txt","a",encoding="utf-8") as file:
        file.write('='*18+'\n'+str(name)+' '+str(surname)+'\n'+str(l1)+' Midterm:'+str(l1m)+'\n'+str(l1)+' Final:'+str(l1f)+'\n'+str(l1)+' Project:'+str(l1f)+'\n'+str(l1)+' Grade:'+str(harf)+'\n'+'='*18+'\n')
    l2=str(input("2. lesson:")).upper()
    l2m=int(input(f"{l2} Midterm:"))
    l2f=int(input(f"{l2} Final:"))
    l2p=int(input(f"{l2} Project:"))
    l2a=int((l2m*0.3)+(l2f*0.5)+(l2p*0.2))
    if l2a>=90 and l2a<=100:
        harf='AA'
    elif l2a>=70 and l2a<90:
        harf='BB'
    elif l2a>=50 and l2a<70:
        harf='CC'
    elif l2a>=30 and l2a<50:
        harf='DD'
    else:
        harf='FF'
    if harf=="FF":
        print(f"{l2} grade:"+harf)
        print(f"You failed {l2}")
    with open("Results.txt","a",encoding="utf-8") as file:
        file.write(str(l2)+' Midterm:'+str(l2m)+'\n'+str(l2)+' Final:'+str(l2f)+'\n'+str(l2)+' Project:'+str(l2f)+'\n'+str(l2)+' Grade:'+str(harf)+'\n'+'='*18+'\n')
    l3=str(input("3. lesson:")).upper()
    l3m=int(input(f"{l3} Midterm:"))
    l3f=int(input(f"{l3} Final:"))
    l3p=int(input(f"{l3} Project:"))
    l3a=int((l3m*0.3)+(l3f*0.5)+(l3p*0.2))
    if l3a>=90 and l3a<=100:
        harf='AA'
    elif l3a>=70 and l3a<90:
        harf='BB'
    elif l3a>=50 and l3a<70:
        harf='CC'
    elif l3a>=30 and l3a<50:
        harf='DD'
    else:
        harf='FF'
    if harf=="FF":
        print(f"{l3} grade:"+harf)
        print(f"You failed {l3}")
    with open("Results.txt","a",encoding="utf-8") as file:
        file.write(str(l3)+' Midterm:'+str(l3m)+'\n'+str(l3)+' Final:'+str(l3f)+'\n'+str(l3)+' Project:'+str(l3f)+'\n'+str(l3)+' Grade:'+str(harf)+'\n'+'='*18+'\n')
    l4=str(input("4. lesson:")).upper()
    l4m=int(input(f"{l4} Midterm:"))
    l4f=int(input(f"{l4} Final:"))
    l4p=int(input(f"{l4} Project:"))
    l4a=int((l4m*0.3)+(l4f*0.5)+(l4p*0.2))
    if l4a>=90 and l4a<=100:
        harf='AA'
    elif l4a>=70 and l4a<90:
        harf='BB'
    elif l4a>=50 and l4a<70:
        harf='CC'
    elif l4a>=30 and l4a<50:
        harf='DD'
    else:
        harf='FF'
    if harf=="FF":
        print(f"{l4} grade:"+harf)
        print(f"You failed {l4}")
    with open("Results.txt","a",encoding="utf-8") as file:
        file.write(str(l4)+' Midterm:'+str(l4m)+'\n'+str(l4)+' Final:'+str(l4f)+'\n'+str(l4)+' Project:'+str(l4f)+'\n'+str(l4)+' Grade:'+str(harf)+'\n'+'='*18+'\n')
    l5=str(input("5. lesson:")).upper()
    l5m=int(input(f"{l5} Midterm:"))
    l5f=int(input(f"{l5} Final:"))
    l5p=int(input(f"{l5} Project:"))
    l5a=int((l5m*0.3)+(l5f*0.5)+(l5p*0.2))
    if l5a>=90 and l5a<=100:
        harf='AA'
    elif l5a>=70 and l5a<90:
        harf='BB'
    elif l5a>=50 and l5a<70:
        harf='CC'
    elif l5a>=30 and l5a<50:
        harf='DD'
    else:
        harf='FF'
    if harf=="FF":
        print(f"{l5} grade:"+harf)
        print(f"You failed {l5}")
    with open("Results.txt","a",encoding="utf-8") as file:
        file.write(str(l5)+' Midterm:'+str(l5m)+'\n'+str(l5)+' Final:'+str(l5f)+'\n'+str(l5)+' Project:'+str(l5f)+'\n'+str(l5)+' Grade:'+str(harf)+'\n'+'='*18+'\n')

print("Have a nice day!")