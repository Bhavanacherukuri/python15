def squa(a,b):
    for i in range(a,b):
        yield i**2
        yield i*2
out=squa(5,15)
print(list(out))

