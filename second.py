def rec_sum(lis):
    if len(lis)==1:
        return lis[0]
    else:
        return lis[-1]+rec_sum(lis[:-1])
    
print(rec_sum([1,2,5]))