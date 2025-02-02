from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        # Step 1: Initialize a counter to count the number of inversions.
        # 'countInversion' keeps track of how many times the order is violated.
        countInversion, n = 0, len(nums)

        # Step 2: Loop through the array to check for inversions.
        for index in range(n):
            # Step 3: Compare the current element with the next one in the array.
            # We use the modulo operation to handle the circular nature of the array.
            # This ensures that we compare the last element with the first element.
            if nums[index] > nums[(index + 1) % n]:
                # If the current element is greater than the next, it counts as an inversion.
                countInversion += 1
        
        # Step 4: If there is at most one inversion, return True (valid rotated sorted array).
        # If there is more than one inversion, return False (not a valid rotated sorted array).
        return countInversion <= 1