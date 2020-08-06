import math 

# MaxSubsetSum - 
#   Input - Array of Numbers
#   Result- maximum sum of continuous elements in array
def maxSubsetSum(A):
    max_start, max_stop = 0, 1 
    curr = 0                  
    max_sum = A[0]        
    current_sum = 0           

    for i, elem in enumerate(A):
        current_sum +=  elem

        if max_sum < current_sum:
            max_sum = current_sum 
            max_start = curr
            max_stop = i  + 1
        if current_sum < 0:
            current_sum = 0
            curr = i + 1

    return  max_sum

# Merge two Sorted Arrays
#   Input - Two Sorted Arrays
#   Output- One Sorted Array containing elements from both input arrays
def merge_sorted_array(a,b):
    i=0
    j=0
    c=[]
    while (i<len(a) and j<len(b)):
        if(a[i]<b[j]):
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while(i<len(a)):
        c.append(a[i])
        i+=1
    while(j<len(b)):
        c.append(b[j])
        j+=1
    return(c)

#Missing Element in an Array
#   Input - Array with continuous elements of numbers with one missing number , and size
#   Output - Missing element from the array
def missing_element_in_array(arr, n):
    return int((n*(n+1))/2 - sum(arr))

#Sub-Array Sum
#   Input - Size of Array, Sum to be found, Array 
#   Output - 1 if found, -1 if not found 
def SubArraySum(size,final,array):
        first=0
        total=0
        i=0
        for i in range(0,size+1):
            while (total>final and first<i-1):
                total=total-array[first]
                first+=1
            if total==final:
                print (first+1,i)
                return(1)
            if i<size:
                total=total+array[i]
        print(-1)

#Rearrange array alternately
#Input - Array of numbers
#Output- Array in the format containing higesht number then lowest number and so on.
def rearrange_alternate_array(arr):
    c=[]
    for i in range(0,len(arr)):
        if(i%2==0):
            c.append(max(arr))
            arr.remove(max(arr))
        else:
            c.append(min(arr))
            arr.remove(min(arr))
    return(c)

#Merge Sort
#Input - Array of Numbers
#Output- Sorted Array 
def merge_sort(A):
    n=len(A)
    if n == 1 :
        return A
    mid = n // 2
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    return merge(L,R)

def merge(L,R):
    i=0
    j=0
    answer=[]
    while (i<len(L) and j<len(R)):
        if L[i]<R[j]:
            answer.append(L[i])
            i+=1
        else:
            answer.append(R[j])
            j+=1
    if  (i<len(L)):
        answer.extend(L[i:])
    if (j<len(R)):
        answer.extend(R[j:])
    return answer

#Equilibrium- Equilibrium position in an array is a position such that the sum of elements before it is equal to the sum of elements after it.
#Input - Array of Numbers
#Output- Pointer value or -1 if not found
def equilibrium(array):
    left=0
    right=sum(array)
    pointer=1
    for i in range(0,len(array)):
        if(i==0):
            left=left
        else:
            left=left+array[i-1]
        right=right-array[i]
        if(left==right):
            return pointer
        pointer+=1
        if(right<left):
            return(-1)