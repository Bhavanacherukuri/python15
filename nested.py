a=int(input('enter first number'))
b=int(input('enter second number'))
c=int(input('enter third number'))
if a>b and a>c:
    if b>c:
        print(b,'is second greatest')
    else:
        print(c,'is second greatest')
elif b>c:
    if a>c:
       print(a,'is second greatest')
    else:
        print(c,'is second greatest')
else:
    if a>b:
         print(a,'is second greatest')
    else:
        print(b,'is second greatest')
