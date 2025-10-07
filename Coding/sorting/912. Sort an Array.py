class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(nums):
            n = len(nums)
            if n<=1:
                return nums
            mid = n//2
            left = divide(nums[:mid])
            right = divide(nums[mid:])
            return sort_and_merge(left, right)


        def sort_and_merge(left, right):
            temp = []
            while(left and right):
                if left[0]<=right[0]:
                    temp.append(left[0])
                    left.pop(0)
                else:
                    temp.append(right[0])
                    right.pop(0)
            return temp+left+right
        return divide(nums)


