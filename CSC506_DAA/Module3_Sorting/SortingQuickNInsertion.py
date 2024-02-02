def insertion(inputArray):
   '''
   Base insertion sort
   '''
   for i in range(1,len(inputArray)):
      j=i
      while(j>0 and inputArray[j-1] > inputArray[j]):
         temp = inputArray[j]
         inputArray[j] = inputArray[j-1]
         inputArray[j-1]=temp
         j = j-1
   return inputArray

def quickSort(inputArray):
   'Quick Sort'
   if len(inputArray)<=1:
      return inputArray
   
   mid = len(inputArray)//2
   pivot = inputArray[mid]
   left = [x for x in inputArray if x < pivot]
   right = [x for x in inputArray if x> pivot]
   return quickSort(left)+[pivot]+quickSort(right)

def quickSortWithInsertionSort(inputArray,partitionSize = 10): # check for 10 elements and go for insertionSort
   if len(inputArray)<=partitionSize:
      print("doing insertion sort")
      return insertion(inputArray)
   else:
      print("doing quick sort")
      return quickSort(inputArray)

#print(quickSortWithInsertionSort([10, 2, 78, 4, 45, 32,-12,65,14,32,85])) #elements < 10  #12 elemenst

import random

random_list = random.sample(range(1, 1000000000), 1000)  # Generate a random list of 20 integers
print("Unsorted list:", random_list)
sorted_list = insertion(random_list)
print("Sorted list:", sorted_list)
