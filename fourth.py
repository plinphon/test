import string


def check(word):
    lower= [i for i in string.ascii_lowercase]
    upper= [i for i in string.ascii_uppercase]
    num=[0,1,2,3,4,5,6,7,8,9]
    alphabet=upper+lower
    collect={}
    for i in word:
        if i in alphabet:
            if i in lower:
                if upper[lower.index(i)] in collect.keys():
                    collect[i]=collect[upper[lower.index(i)]]+1
                    del collect[upper[lower.index(i)]]
                elif i not in collect.keys():
                    collect[i]=1
                else:
                    collect[i]+=1
            else:
                if lower[upper.index(i)] in collect.keys():
                    i = i.lower()
                if i not in collect.keys():
                    collect[i]=1
                else:
                    collect[i]+=1
        else:
            if i not in collect.keys():
                collect[i]=1
            else:
                collect[i]+=1

    count=0
    toprint=''
    for i in list(collect.items()):
        if i[1]>1:
            count+=1
            toprint=toprint+'"'+str(i[0])+'"'+" occurs "+str(i[1])+" times "
    toprint = str(count) + " # "+toprint   
    return toprint

print(check('fre444Aaefefe'))

