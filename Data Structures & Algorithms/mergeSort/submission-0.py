# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)

        return self.merge_sort(pairs, 0, n-1)
    
    
    def merge(self, arr, start, mid, end):
        left = arr[start:mid+1]
        right = arr[mid+1: end+1]
        m, n = len(left), len(right)
        i, j, k = 0, 0, start
        while i < m and j < n:
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < m:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n:
            arr[k] = right[j]
            j += 1
            k += 1
        
        return arr
        

    def merge_sort(self, arr, start, end):
        if end - start + 1 <= 1:
            return arr
        
        mid = (end + start) // 2
        self.merge_sort(arr, start, mid)
        self.merge_sort(arr, mid+1, end)

        return self.merge(arr, start, mid, end)
