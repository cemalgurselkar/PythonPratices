import sys

class SearchAlgorithms:
    def __init__(self,array):
        self.array = array
    
    def linearSearch(self,target):
        arr = self.array
        size = len(arr)
        for i in range(0,size):
            if arr[i] == target:
                return i
        return -1
    
    def binarySearch(self,left,right,target):
        arr = self.array
        while left<=right:
            mid = (left+right)//2
            if arr[mid] == target:
                return mid
            elif arr[mid]<target:
                left == mid+1
            else:
                right = mid-1
        return -1


array = [2,3,7,12,16,19,20,24]
size = len(array)
target = int(input("Enter the number you wanna find: "))
alg = SearchAlgorithms(array)
found = alg.binarySearch(0,size-1,target)
if found == -1:
    print(f'Your target number {target} is not found!!!')
else:
    print(f'Your target number {target} is found!!!')