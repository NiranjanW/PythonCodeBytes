
from typing import List

class Node :
    def __init__(self,value, ptr =None):
        self.value = value
        self.next = 

def selectionSort( arry:List[int]) ->List[int]:

    min_idx:int 

    for i in range(len(arry)):
        min_idx = i

        for j in range (i +1 , len(arry)):
            if arry[min_idx] > arry[j]:
                min_idx = j
        arry[i] , arry[min_idx] = arry[min_idx] , arry[i]
    return arry       

def quickSort(arry:List[int]) ->List[int]:
    pivot = 
def bubbleSort(arry:List[int]) ->List[int]:

    swapped = False
    for i in range(len(arry)-1):
        for j in range( 0, len(arry)-i-1 ):
             if arry[j] > arry[j + 1]:
                swapped = True
                arry[j], arry[j + 1] = arry[j + 1], arry[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return 

def main ():
    A = [64, 25, 12, 22, 11]
    selectionSort(A)
    for i in range(len(A)):
           print("%d" %A[i],end=" ")
        


if __name__ == "__main__":
    main()
