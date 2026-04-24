class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while(l<r):
            start = (l+r)//2
            if nums[start] == target:
                return start
            if nums[start]>nums[r]:
                l = start+1
            else:
                r = start
        start = l
    
        if target<=nums[n-1]:
            l = start
            r = n-1
            return self.search_ele(l, r, nums, target)
        else:
            l = 0
            r = start-1
            return self.search_ele(l, r, nums,target)


    def search_ele(self, l, r, nums, target):
        if l<0 or r >= len(nums):
            return -1
        while(l<=r):
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1 
        return -1   