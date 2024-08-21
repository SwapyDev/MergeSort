testArray=[]
elements=int(input("Array length: "))

def array(array, n):
    for i in range(n):
        if n>0:
            element=input(f"Element {i+1}: ")
            array.append(element)
        elif n-1==i:
            return array

array(testArray,elements)
print(testArray)

def mergeSort(array):
    middle = len(array) // 2
    leftArray = array[:middle]
    rightArray = array[middle:]
    print(leftArray, rightArray)
    
mergeSort(testArray)


