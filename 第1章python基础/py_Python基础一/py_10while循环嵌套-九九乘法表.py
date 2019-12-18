line=9
row=9
i=1
j=1
while i<=line:
    j=1
    while j<=i:
        n=i*j
        print('%d*%d=%d'% (j,i,n),end='\t')
        j=j+1
    print()
    i=i+1
