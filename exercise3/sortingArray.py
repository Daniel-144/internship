"""
3. Sort the numbers in an array (ascending or descending). Write a function that finds the largest number in an array.
"""
def ascending(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if (array[j]<array[i]):
                array[j],array[i]=array[i],array[j]
    return(array)

def descending(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if (array[j]>array[i]):
                array[j],array[i]=array[i],array[j]
    return(array)

def FindMaximum(arraySorted):
    return(max(arraySorted))

       

array=[2,18,7,90,5,33]
choice=int(input("enter 1-to sort in ascending 2-to sort inn descending order:"))
if (choice==1):
    arraySorted=ascending(array)
    print(arraySorted)
elif(choice==2):
    arraySorted=descending(array)
max=FindMaximum(arraySorted)
print("the maximum number of the array is:",max)