def countchar(a,ch):
    count=0
    for i in a:
        if i==ch:
            count+=1
    return count
count=countchar('happy new year','a')
print(count)
