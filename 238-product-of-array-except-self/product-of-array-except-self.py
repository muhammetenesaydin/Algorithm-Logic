from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # 1. Soldan prefix çarpımı
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # 2. Sağdan suffix çarpımı ile çarp
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
