# Selection_Sorting
A=[1,5,2,7,87] 
n=len(A)
# Linear Search for min elem of Array
for i in range(n):
    small_idx=i
    for j in range(i+1,n):
        if A[j]<A[small_idx]:
            small_idx=j
        A[i],A[small_idx]=A[small_idx],A[i]
print(A)
# T.C.-O(N^2)  and S.C.: O(1)