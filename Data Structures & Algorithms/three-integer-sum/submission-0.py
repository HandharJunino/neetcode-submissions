class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_list = []
        nums.sort()
        n = len(nums)
        
        for i in range(n-2):
            # initialise the pointers
            j = i + 1
            k = n-1
            
            # skip duplicates for the current item
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    # a valid triplet is found
                    nums_list.append([nums[i], nums[j], nums[k]])
                    
                    # skipping duplicates
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                        
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                        
                    # move the pointers
                    j += 1
                    k -+ 1
                    
                elif sum < 0:
                    j += 1
                    
                else:
                    k -= 1
                    
        return nums_list