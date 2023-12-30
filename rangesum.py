def add_even(var,i=0):
    if len(var)-1==i:
        if var[i]%2==0:
            return var[i]
        else:
            return 0
    if var[i]%2==0:
        return var[i]+add_even(var,i+1)
    else:
        return add_even(var,i+1)
a=[1,5,2,2]
out=add_even(a)
print(out)