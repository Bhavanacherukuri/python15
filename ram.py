def hetr(arr):
    count=0
    for i in arr:
        if type(i)==int:
            count+=i
    print(count)
hetr([1,2,3,'hi','j',3])
