def cal(lis):
    lis=[i for i in str(lis)]
    for i in range(len(lis)):
        if i%2==0:
            i=i+1
            lis[-i]=int(lis[-i])*2
            if len(str(lis[-i]))==2:
            
                lis[-i]=int(str(lis[-i])[0])+int(str(lis[-i])[1])
                
    sum=0
    print(lis)
    for k in lis:
        sum= sum+int(k)
    return 10 -sum%10

print(cal(7992739871))