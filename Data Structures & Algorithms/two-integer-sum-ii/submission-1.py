class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        
        while l<r:
            n_sum = numbers[l] + numbers[r]

            if n_sum < target:
                l += 1

            elif n_sum > target:
                r -= 1

            else:
                return [l + 1, r + 1]

        return []
