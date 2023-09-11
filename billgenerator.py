s=input('What size pizza want to you:')
bill=0
if s=='S' or s=='s':
    bill+=100
    print('Small pizza')
elif s=='M' or s=='m':
    bill+=200
    print('Medium pizza')
else:
    bill+=300
    print('Large pizza')
            
perper=input("Do you want Extra perper (y/n)?")

if perper=='Y' or perper=='y':
    if s=="S" or s=='s':
        bill+=30
    elif s=='M' or s=='m':
        bill+=30    
    else:
        bill+=30

cheese=input("Add Extra Cheese (Y/N)?")

if cheese=='Y' or cheese=='y':
    if s=='S'or s=="s":
        bill+=20
    else:
        bill+=20

print(f"Your Final bill is {bill}/-")            
