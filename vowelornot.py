def vowelornot(a):
    i=0
    out=[]
    while(i<len(a)):
        if a[i] in 'aeiouAEIOU':
            out=out+[i]
        i=i+1
    return out
out=vowelornot('happy new year')
print(out)
