class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l % 2:  # the length is odd
            return self.findKthSmallest(nums1, nums2, l//2+1)
        else:
            return (self.findKthSmallest(nums1, nums2, l//2) +
            self.findKthSmallest(nums1, nums2, l//2+1))*0.5
    
    def findKthSmallest(self, nums1, nums2, k):
    # force nums1 is not longer than nums2
        if len(nums1) > len(nums2):
            return self.findKthSmallest(nums2, nums1, k)
        if not nums1:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        pa = min(k/2, len(nums1)); pb = k-pa  # take care here
        if nums1[pa-1] <= nums2[pb-1]:
            return self.findKthSmallest(nums1[pa:], nums2, k-pa)
        else:
            return self.findKthSmallest(nums1, nums2[pb:], k-pb)
        