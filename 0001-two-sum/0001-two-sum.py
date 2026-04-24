class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}  # 값 -> 인덱스

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in d:
                return [d[complement], idx]
            
            else:
                d[num] = idx