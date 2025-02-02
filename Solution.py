from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        # Step 1: Determine the length of the array.
        n = len(nums)
        
        # Step 2: Create a cache array of the same size as nums to store the rotated version.
        cache = [0] * n

        # Step 3: Try every possible rotation of the array (from 0 to n-1).
        for rotationCount in range(n):
            # Step 4: Initialize a variable to keep track of the current index in the 'cache' array.
            currentIndex = 0

            # Step 5: Copy the elements from the array starting from 'rotationCount' to the end of the array
            # into the 'cache' array, effectively rotating the array.
            for index in range(rotationCount, n):
                cache[currentIndex] = nums[index]
                currentIndex += 1

            # Step 6: Copy the elements from the beginning of the array up to 'rotationCount' into the 'cache'.
            for index in range(rotationCount):
                cache[currentIndex] = nums[index]
                currentIndex += 1
            
            # Step 7: Now, check if the rotated array (stored in 'cache') is sorted in non-decreasing order.
            is_Sorted = True
            for index in range(n-1):
                if cache[index] > cache[index+1]:
                    # If any element is greater than the next, it's not sorted.
                    is_Sorted = False
                    break
            
            # Step 8: If the rotated array is sorted, return True.
            if is_Sorted:
                return True
        
        # Step 9: If none of the rotations resulted in a sorted array, return False.
        return False