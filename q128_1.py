class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return self.cubicTime(nums)
        # return self.sorting(nums)
        return self.linearTime(nums)
    
    def cubicTime(self, nums):
        if len(nums) == 0: return 0
        res, curr = 1, 1

        for num in nums:
            curr = 1
            
            while num + 1 in nums:
                num += 1
                curr += 1
            res = max(res, curr)
        
        return res

    def sorting(self, nums):
        if len(nums) == 0: return 0
        nums.sort()

        res, curr = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: continue
            if nums[i] == nums[i - 1] + 1: curr += 1
            else: curr = 1

            res = max(res, curr)
        
        return res
    
    def linearTime(self, nums):
        if len(nums) == 0: return 0
        numSet = set(nums)

        res, curr = 1, 1

        for num in nums:
            # only look for start of the consecutive sequence
            if num - 1 not in numSet:
                curr = 1
                currNum = num

                while currNum + 1 in numSet:
                    curr += 1
                    currNum += 1
            res = max(res, curr)

        return res
