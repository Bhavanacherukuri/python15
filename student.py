per=int(input('enter percentage:'))
if per>=90 and per>=100:
    print('A+ grade')
elif per>=80 and per>=90:
    print('A grade')
elif per>=70 and per>=80:
    print('B grade')
elif per>=60 and per>=70:
    print('C grade')
elif per>=35 and per<=60:
    print('justpass')
elif per<35 and per>0:
    print('Fail')
else:
    print('enter valid percentage')
    
