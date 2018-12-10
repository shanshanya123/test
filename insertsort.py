def InsertSort(ls):
    n=len(ls)
    if n<=1:
        return ls
    for i in range(1,n):
        j=i
        target=ls[i]           
        while j>0 and target<ls[j-1]:      
            ls[j]=ls[j-1]
            j=j-1
        ls[j]=target            
    return ls
