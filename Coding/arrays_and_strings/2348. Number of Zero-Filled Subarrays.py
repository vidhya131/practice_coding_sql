class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cur_count = 0
        res = 0
        for i in nums:
            if i == 0:
                cur_count += 1
                res += cur_count
            else:
                # res += cur_count*(cur_count+1)//2
                cur_count = 0
        # res += cur_count*(cur_count+1)//2
        return res

        
            
