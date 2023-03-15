




def partition(array, low, high):

	pivot = array[high]

	i = low - 1


	for j in range(low, high):
		if array[j] <= pivot:

			i = i + 1


			(array[i], array[j]) = (array[j], array[i])

	(array[i + 1], array[high]) = (array[high], array[i + 1])


	return i + 1



def quickSort(arr, low, high):
     if low<high:
          pi = partition(arr, low, high)
          quickSort(arr, low, pi-1)
          quickSort(arr, pi+1, high)




if __name__ == "__main__":
     
     arr = [4,76,12,86,23,97]
     quickSort(arr, 0, len(arr)-1)
     print(arr)


      

     
