class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_hash = {}
        for idx, num in enumerate(nums):
            if target - num in dict_hash:
                idx_1 = idx
                idx_2 = dict_hash[target - num]
                break
            dict_hash[num] = idx
        else:
            idx_1, idx_2 = None, None
        return [idx_1, idx_2]
