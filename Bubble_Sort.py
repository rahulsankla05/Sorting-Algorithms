# **** "Bubble Sort RS "
#  Move the biggest elem to end of the array by doing pairwise swap
A=[1,5,2,7,87]   # Given Array
n=len(A)   # length of array
for itr in range(n):     # loop to travese in given array
    for j in range(0,n-1-itr):    # inner loop to compare elems of Array
        if A[j]>A[j+1]:       # condition for Swap
            A[j],A[j+1]=A[j+1],A[j]      # Pairwise Swapping
print("Sorted Array:",A)

#  T.C: O(N^2) and S.C: O(1)

