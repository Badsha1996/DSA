class Searching:
    def __init__(self, target: int, arr : list[int]) -> None:
        self.target = target
        self.arr    = arr 

    def binarySearch(self) -> int | None:
        # 1. mid 
        # 2. arr[mid] == target 
        # 3. is it bigger or shorter 
        # 4. do an update of mid depending on situation 

        low  = 0
        high = len(self.arr) - 1

        while low <= high:
            mid = low + high // 2
            # FOUND THE TARGET 
            if self.arr[mid] == self.target: return mid 

            # OTHERWISE 
            if self.arr[mid] > self.target: high = mid - 1
    
            else:                           low = mid + 1

        return None

    def recursiveBinarySearch(self, low : int, high : int) -> int | None: 
        if low > high : return None 

        mid = low + high // 2

        if self.arr[mid] == self.target: return mid
        if self.arr[mid] > self.target: return self.recursiveBinarySearch(low, mid - 1)
        else :                          return self.recursiveBinarySearch(mid + 1, high)

    def printTargetIndex(self) -> None:
        # index = self.binarySearch()
        index = self.recursiveBinarySearch(low=0, high=len(self.arr) - 1)
        print(f"The index of {self.target} in {self.arr} is {index}")


S = Searching(4, [1,2,3,4])   # Have created an Object 
S.printTargetIndex()
