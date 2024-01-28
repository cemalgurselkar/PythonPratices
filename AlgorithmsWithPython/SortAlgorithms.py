import sys

class SortAlgorithm:
    def __init__(self,array):
        self.array = array
    
    def selection(self):
        liste = self.array
        for i in range(len(liste)):
            min_indx = i
            for j in range(i+1,len(liste)):
                if liste[min_indx] > liste[j]:
                    min_indx = j
            liste[i],liste[min_indx] = liste[min_indx],liste[i]
        return liste
    
    def bubbleSort(self):
        arr = self.array
        n = len(arr)
        for i in range(len(arr)):
            swapped = False
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    swapped = True
            if swapped == False:
                break
        return arr
    
    def insertSort(self):
        arr = self.array
        for i in range(1,len(arr)):
            key = arr[i]
            j = i-1
            while j>=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
    
    def partition(self,low,high):
        arr = self.array
        pivot = arr[high]
        i = low-1
        for j in range(low,high):
            if arr[j]<=pivot:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1
    
    def quickSort(self,low,high):
        if low<high:
            pi = self.partition(low,high)
            self.quickSort(low,pi-1)
            self.quickSort(pi+1,high)
        return self.array
    
    def heapify(self,size,i):
        arr = self.array
        largest = i
        l = 2*i+1
        r = 2*i+2
        if l<size and arr[largest]<arr[l]:
            largest = l
        if r<size and arr[largest]<arr[r]:
            largest = r
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            self.heapify(size,largest)
        return arr
        
    def heapSort(self):
        arr = self.array
        size = len(arr)
        for i in range((size//2)-1,-1,-1):
            self.heapify(size,i)
        for i in range(size-1 ,0,-1):
            arr[i],arr[0] = arr[0],arr[i]
            self.heapify(i,0)
        return arr
    
    def count_sort(self):
        arr = self.array
        m = max(arr)
        count_arr = [0] * (m+1)
        for num in arr:
            count_arr[num] += 1
        for i in range(1,m+1):
            count_arr[i] += count_arr[i-1]
        output_arr = [0]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            output_arr[count_arr[arr[i]]-1] = arr[i]
            count_arr[arr[i]] -= 1
        return output_arr


#DRİVER FUNCTİON WİTH EXAMPLE ARRAY
def main():
    array = [34,22,18,97,57,45,39,706,1,3,5,2,7]
    alg = SortAlgorithm(array)
    sorted_list = alg.bubbleSort()
    return sorted_list

print(main())        