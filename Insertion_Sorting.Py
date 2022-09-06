# Insertion_Sorting.py
A=[1,5,2,7,87] 
n=len(A)
for i in range(1,n):
    j=i-1
    temp=A[i]
    while(j>=0) and (A[j]>temp):
        A[j+1]=A[j]
        j-=1
    A[j+1]=temp
print(A)
