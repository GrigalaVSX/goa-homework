#davalebis pirveli etapi

age=int(input('how old are you?')) 

comparison=age>=18  

student=True 

print(comparison and student)

print(type(age))

#davalebis meore etapi

x=5

y=700

compar_x=5>0

compar_y=700>0

compar2_x=5>100

compar2_y=700>100

print(compar_x and compar_y)

print(compar2_x or compar2_y)

# davalebis mesame etapi

number=int(input('choose any number'))

# lets_see=10<number<50 ese ufro martivia

lets_see1=number>10

lets_see2=number<50

print(lets_see1 and lets_see2)

ngt1=number>0

ngt2=number<0

print(ngt1 or ngt2)

#davalebis meotxe etapi

user_age=(input('age:'))

user_password=input('password:')

compar1=int(user_age)>=18

act_password='admin123'

compar2=user_password==act_password

print(compar1 and compar2)

#davalebis 5 etapi

x=7.0
y=-9.0
z=81.0

average=(x+y+z)/3

compar_1=x>0
compar_2=y>0
compar_3=z>0
compar_4=average>60

answer=compar_1 and compar_2 and compar_3 and compar_4

print(answer)

print(type(answer))

#davalebis meeqvse etapi

speed=int(input('speed:'))

compar=speed>120

compar02=speed<0

anss=compar or compar02

print(anss)

#davalebis meshvide etapi

height=float(input('height:'))

weight=float(input('weight'))

height_compar=height>1.7

weight_compar=weight<90

print(height_compar and weight_compar)

height_compar02=height>1.5

weight_compar02=weight>120

print(height_compar02 or weight_compar02)

#davalebis merve etapi

x=-9

ahk=x%2

ahk2=ahk==0

compare=x>0

ahk3=x%2==1

compare2=x<0

print(ahk2 and compare)

print(ahk3 and compare2)

#davalebis mecxre etapi

x=input('number:')

print(type(x))

x=float(x)

answ=0<x<100

print(answ)

#davalebis meate etapi

age=int(input('age:'))

balance=float(input('balance:'))

VIP_status=True

compar1=age>=18

compar2=balance>=100

checking=compar1 and compar2

access=checking or VIP_status

print(access)




















