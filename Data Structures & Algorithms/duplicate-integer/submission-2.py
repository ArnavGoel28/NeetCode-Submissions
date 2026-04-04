class Solution:
        def hasDuplicate(self, nums: List[int]) -> bool:
            from collections import Counter
            count_map = Counter(nums)
            for key in count_map:
                if count_map[key] > 1:
                    return True
            return False