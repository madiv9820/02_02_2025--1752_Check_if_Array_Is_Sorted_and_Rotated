from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        # Step 1: Determine the size of the array.
        size = len(nums)
        
        # Step 2: Create a sorted version of the input array to compare against.
        sorted_nums = sorted(nums)

        # Step 3: Loop through all possible rotations of the original array.
        for rotationCount in range(size):
            # Assume that the current rotation matches the sorted array.
            is_Match = True

            # Step 4: Compare the rotated version of 'nums' with 'sorted_nums'.
            for index in range(size):
                # (rotationCount + index) % size gives the rotated index of 'nums'.
                if nums[(rotationCount + index) % size] != sorted_nums[index]:
                    # If any element does not match, set 'is_Match' to False and break out of the loop.
                    is_Match = False
                    break
            
            # Step 5: If a rotation matches the sorted array, return True.
            if is_Match:
                return True
        
        # Step 6: If no rotation matches the sorted array, return False.
        return False