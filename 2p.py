try:
    lis = []
    while True:
        a,b,c = str(input()).split()
        lis.append((a,b,c))
        
except:
    count = 0
    # print (len(lis))
    for i in lis:
        a,b,c = i
        l,h = a.split('-')
        if len(c)>=int(l) and len(c)>=int(h):
        	if c[int(l)-1]==b[0] and c[int(h)-1]!=b[0]:
        		count+=1
        	if c[int(h)-1]==b[0] and c[int(l)-1]!=b[0]:
        		count+=1

    print (count)




        
