def sample(a):
    for i in a:
        if type(i) in [list,str,tuple,set,dict]:
            yield len(i)
        else:
            yield i
a=[1,[4,5,6],{7,9},'efg',{'a':1},9.5,12]
out=sample(a)
print(list(out))