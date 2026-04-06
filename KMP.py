def kmp(t,p):
    l=[0]*len(p)
    j=0
    for i in range(1,len(p)):
        while j and p[i]!=p[j]:
            j=l[j-1]
        if p[i]==p[j]:
            j+=1
            l[i]=j
    j=0
    for i in range(len(t)):
        while j and t[i]!=p[j]:
            j=l[j-1]
        if t[i]==p[j]:
            j+=1
        if j==len(p):
            print(i-j+1)
            j=l[j-1]

kmp("ababcabcabababd","ababd")