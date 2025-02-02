- ## Approach 1:- Brute Force 
    - ### Intuition:
        The problem asks us to determine whether an array is sorted in non-decreasing order and then rotated. The key observation is that if an array is sorted and rotated, there should be at most **one descent** where an element is greater than the next (i.e., the array should "break" its sorted order only once). The array may have duplicate elements, but it should still follow this rule. If we can find such a rotation, the array is valid; otherwise, it isn't.

    - ### Approach:
        1. **Rotation Simulation:**
            - The problem requires checking if the array is sorted after it has been rotated. This can be done by simulating each possible rotation.
            - For each rotation, we "rotate" the array by shifting elements and checking if the resulting array is sorted.

        2. **Sorted Check:**
            - For each rotated version of the array, we check if it is sorted in non-decreasing order.
            - If we find any rotation that results in a sorted array, we return `True`.
            - If no rotation produces a sorted array, we return `False`.

        3. **Brute Force:**
            - For each possible rotation (from 0 to `n-1`), we create a new rotated array and check if it is sorted. This is repeated for every possible rotation.
    
    - ### Code Implementation
        - **Python Solution**
            ```python3 []
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
            ```
        - **C++ Solution**
            ```cpp []
            class Solution {
            public:
                bool check(vector<int>& nums) {
                    // Create a vector 'cache' to store a rotated version of the input array 'nums'.
                    vector<int> cache(nums.size());
                    
                    // Loop through each possible rotation from 0 to nums.size() - 1.
                    for(int rotationCount = 0; rotationCount < nums.size(); ++rotationCount) {
                        // Start the rotation process by filling up the 'cache' array.
                        int currentIndex = 0;
                        
                        // First, copy the part of the array starting from 'rotationCount' to the end into 'cache'.
                        for(int index = rotationCount; index < nums.size(); ++index)
                            cache[currentIndex++] = nums[index];
                        
                        // Then, copy the part of the array from the start up to 'rotationCount' into 'cache' after the first part.
                        for(int index = 0; index < rotationCount; ++index)
                            cache[currentIndex++] = nums[index];

                        // Now, check if the 'cache' array is sorted in non-decreasing order.
                        bool is_Sorted = true;
                        for(int index = 0; index < nums.size() - 1; ++index) {
                            if(cache[index] > cache[index + 1]) {
                                // If any element is greater than the next, the array is not sorted.
                                is_Sorted = false;
                                break;
                            }
                        }

                        // If the array is sorted in this rotation, return true.
                        if(is_Sorted) return true;
                    }

                    // If no valid sorted rotation is found, return false.
                    return false;
                }
            };
            ```

    - ### Time Complexity:
        - The time complexity is **$O(n^2)$**.
            - For each rotation (up to $n$ times), we are copying the array and checking if it is sorted, which takes **$O(n)$** time.
            - This results in a total time complexity of **$O(n^2)$** for the entire solution.

    - ### Space Complexity:
        - The space complexity is **$O(n)$**.
            - We use an additional array (`cache`) of size $n$ to store each rotated version of the input array.
            - Therefore, the space complexity is proportional to the size of the input array.