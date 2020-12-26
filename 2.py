try:
    lis = []
    while True:
        a,b,c = str(input()).split()
        lis.append((a,b,c))
        
except:
    count = 0
    print (len(lis))
    for i in lis:
        a,b,c = i
        l,h = a.split('-')
        if c.count(b[0])>=int(l) and c.count(b[0])<=int(h):
            count+=1
    print (count)



        
