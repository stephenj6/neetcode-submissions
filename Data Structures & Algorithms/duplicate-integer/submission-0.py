class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            seen.add(nums[i])
        return len(nums) != len(set(nums))
        


