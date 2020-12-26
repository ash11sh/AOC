try: 
    a = []
    while True:
        a.append(int(input()))
except:
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if a[i]!=a[j]!=a[k] and a[i]+a[j]+a[k]==2020:
                    print (a[i]*a[j]*a[k])
