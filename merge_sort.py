#### python program to illustrate the merge sort algorithm
def mergesort(list1):
    n=len(list1)
    if(n>1):
        mid=n//2
        l=list1[:mid]
        r=list1[mid:]

        mergesort(l)
        mergesort(r)

        i=j=k=0
        while(i<len(l) and j<len(r)):
            if(l[i]<r[j]):
                list1[k]=l[i]
                i+=1
            else:
                list1[k]=r[j]
                j+=1
            k+=1

        while(i<len(l)):
            list1[k]=l[i]
            i+=1
            k+=1
        while(j<len(r)):
            list1[k]=r[j]
            j+=1
            k+=1
    return list1
list1=[int(x) for x in input().split()]
print(mergesort(list1))
