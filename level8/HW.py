#davalebis pirveli etapi

x=int(input('enter number:'))
y=int(input('enter number:'))
z=int(input('enter number:'))
e=int(input('enter number:'))
a=int(input('enter number:'))

if x>0:
    print('positive')
if y>0:
        print('positive')
if z>0:
            print('positive')
if e>0:
                print('positive')
if a>0:
                    print('positive')


#davalebis meore etapi

x=int(input('enter number:'))

total=0

for i in range(0,x+1,2):
        total+=i

print(total)

#davalebis mesame etapi

number=int(input('enter number:'))

act_number=5

while number!=act_number:
        print('try again')
        number=int(input('enter number:'))
print('number found, game over')

#igive if else-it ar vicodi usasrulo gvindoda tu ara

number=int(input('enter number:'))

act_number=5

if number!=act_number:
        print('you lost')
else:
        print('number found, you won')

#davalebis meotxe etapi

x=3
y=4
z=5

avg=(3+4+5)/3

print(avg)

if avg>50:
        print('passed')
else:
        print('failed')

#davalebis mexute etapi

for i in range(1,21):
        print(i)
        if i%3==0:
                print('fizz')

#davalebis meeqvse etapi

number=int(input('enter number:'))

while number<0:
        print('again')
        number=int(input('enter number:'))
print('positive')

#davalebis meshvide etapi

even_count=0
odd_count=0

x=int(input('enter number1:'))
y=int(input('enter number2:'))
q=int(input('enter number3:'))
w=int(input('enter number4:'))
e=int(input('enter number5:'))
z=int(input('enter number6:'))

if x%2==0:
        even_count+=1
        
else:
        odd_count+=1
        
if y%2==0:
        even_count+=1
        
else:
        odd_count+=1
        
if q%2==0:
        even_count+=1
        
else:
        odd_count+=1
        
if w%2==0:
        even_count+=1
        
else:
        odd_count+=1
        
if e%2==0:
        even_count+=1
        
else:
        odd_count+=1
        
if z%2==0:
        even_count+=1
        
else:
        odd_count+=1
        
print('even=',even_count)
print('odd=',odd_count)

#gakvetilis merve etapi

number=float(input('enter max number:'))

for i in range(4):
        num=float(input('enter number:'))
        if num>number:
                number=num

print('max number is',number)
        
        
    
        
        
