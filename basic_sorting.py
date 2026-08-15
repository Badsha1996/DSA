class sort:
    def __init__(self, arr : list[int]) -> None:
        self.arr = arr
        self.size = len(arr)

    # Time - O(n^2)
    # best time - O(n)
    # SWAP ADJECENT ELEMENT 
    def bubbleSort(self) -> None:
        for i in range(self.size): 
            swap = False 
            for j in range(0, self.size - i - 1 ): 
                if self.arr[j] > self.arr[j+1]: 
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swap = True 
            if not swap : break

    # best, aver, worst -> O(n^2)
    # PICK MINIMUM AND SWAP 
    def selectionSort(self) -> None:
        for i in range(self.size):
            smallest = i 
            for j in range(i+1, self.size):
                if self.arr[j] < self.arr[smallest]:
                    smallest = j 

            self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]

    # Time - O(n^2)
    # best time - O(n)
    def insertionSort(self) -> None:
        for i in range(1, self.size):
            key = self.arr[i]
            j = i - 1

            while j >= 0 and self.arr[j] > key:
                self.arr[j+1] = self.arr[j]
                j-=1 

            self.arr[j + 1] = key # insert into right position  

            


    def printList(self) -> None:
        print(f"Your list is : {self.arr}") 

s = sort([4,3,2,6,1,0])
# s.bubbleSort()
# s.selectionSort()
s.insertionSort()
s.printList()