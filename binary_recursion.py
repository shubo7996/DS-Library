def binary_search(arr,val):
	if (len(arr)==0 or (len(arr)==1 and arr[0]!=val)):
		return False

	mid= len(arr)//2
	mid_val = arr[mid]

	if val==mid_val: return True
	if val<mid_val: return binary_search(arr[:len(arr)//2],val)
	if val>mid_val: return binary_search(arr[len(arr)//2+1:],val)

if __name__ == '__main__':
	arr = [34,46,58,62,71,84,90]
	val=84
	print(binary_search(arr,val))
