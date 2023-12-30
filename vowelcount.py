a=input('enter any string:')
vowel=a
count=0
while(vowel<len(a)):
    if a[vowel] in 'aeiouAEIOU':
        count=count+1
    i=i+1
print(count)