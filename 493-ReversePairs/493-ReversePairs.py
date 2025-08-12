# Last updated: 8/13/2025, 1:10:54 AM
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        def mergeSort(nums):
            if len(nums) < 2:
                return nums
            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] > 2 * right[j]:
                    self.count += len(left) - i
                    j += 1
                else:
                    i += 1
            return merge(left, right)

        def merge(left, right):
            merged = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i+=1
                else:
                    merged.append(right[j])
                    j+=1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
        
        mergeSort(nums)
        return self.count