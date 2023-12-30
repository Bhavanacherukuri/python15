a='MCA SECTION A 123455GB&$#'
V=0
C=0
for i in a:
    if 'A'<=i<='Z' or 'a'<=i<='z':
        if i in 'aeiouAEIOU':
            V+=1
        else:
            C+=1
print(V)
print(C)