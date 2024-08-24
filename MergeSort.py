testArray=[]
elements=int(input("Array length: "))

def array(array, n):
    for i in range(n):
        if n>0:
            element=int(input(f"Input {i+1}: "))
            array.append(element)
        elif n-1==i:
            return array

array(testArray,elements)
print("Unordered",testArray)

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2  
        left_half = array[:mid]  
        right_half = array[mid:]
        
        mergeSort(left_half)
        mergeSort(right_half)
        
        i=j=k=0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        #Verifies if there are any elements left in the left half
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        #Verifies if there are any elements left in the right half
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
            
mergeSort(testArray)
print("Ordered", testArray)


