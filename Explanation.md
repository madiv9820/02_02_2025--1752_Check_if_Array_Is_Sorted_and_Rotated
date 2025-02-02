- ## Approach 3:- Find Smallest Element
    - ### Intuition:
        The problem asks us to determine whether an array is sorted in non-decreasing order and then rotated. A key observation is that in a rotated sorted array, there can be at most **one inversion**—a point where the order breaks (i.e., when an element is greater than the next). This is because the array, when rotated, should only have one "descent" or point where the order is disrupted. The goal is to count how many such inversions exist in the array and check if there’s at most one.

    - ### Approach:
        1. **Inversion Counting:**
            - We count the number of times an element is greater than the next element in the array. If this happens more than once, the array cannot be a rotated version of a sorted array.
        
        2. **Circular Array Comparison:**
            - The array is treated as circular using the modulo operation. This allows the comparison of the last element with the first element, simulating the rotation.

        3. **Valid Rotated Array:**
            - If there is at most **one inversion** (i.e., one point where the order is broken), then the array is a valid rotated sorted array. Otherwise, it is not.

        4. **Return the Result:**
            - If the number of inversions is less than or equal to 1, return `True` (indicating the array is a valid rotated sorted array). Otherwise, return `False`.

    - ### Code Implementation:
        - **Python Solution**
            ```python3 []
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
            ```
        - **C++ Solution**
            ```cpp []
            class Solution {
            public:
                bool check(vector<int>& nums) {
                    // Step 1: Initialize a counter to count the number of inversions.
                    int countInversion = 0;

                    // Step 2: Iterate through the array to check for inversions.
                    for(int index = 0; index < nums.size(); ++index) {
                        // Step 3: Compare each element with the next one in the array.
                        // We use the modulo operator to handle the circular nature of the array (i.e., checking the last element with the first).
                        if(nums[index] > nums[(index + 1) % nums.size()])
                            ++countInversion; // If the current element is greater than the next, it counts as an inversion.
                    }

                    // Step 4: If there is more than one inversion, return false.
                    // If there is at most one inversion, return true (i.e., the array is sorted and rotated).
                    return countInversion <= 1;
                }
            };
            ```

    - ### Time Complexity:
        - The function loops through the array once, comparing adjacent elements. Since the loop runs $n$ times (where $n$ is the length of the array), the time complexity is **$O(n)$**.

    - ### Space Complexity:
        - The space complexity is **$O(1)$** because the solution only uses a fixed amount of extra space (a few integer variables for counting and indexing). No additional space proportional to the input size is used.