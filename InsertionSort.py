def insertion_sort(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j
        while i>0 and A[i-1]>key:
            A[i]=A[i-1]
            i=i-1
        A[i]=key
    return A

unsorted_array=[]
n=int(input("Enter Length of array"))
for i in range(n):
    value=int(input("Enter Element "+ str(i) + " : " ))
    unsorted_array.append(value)
sorted_array=insertion_sort(unsorted_array)
print(sorted_array)