# Last updated: 9/4/2025, 4:30:32 PM
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0

        l = [0]*(len(nums1)+len(nums2))
        mer = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                l[mer] = nums2[j]
                j+=1
                mer+=1
            else:
                l[mer] = nums1[i]
                i+=1
                mer+=1
        while i< len(nums1):
            l[mer] = nums1[i]
            i+=1
            mer+=1
        while j< len(nums2):
            l[mer] = nums2[j]
            j+=1
            mer+=1
        if len(l) % 2 != 0:
            return float(l[len(l)/2])
        else:
            return(float((l[len(l)/2])+(l[(len(l)/2)-1]))/2)
            