# 1752. Check if Array Is Sorted and Rotated (All Approaches)
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
<hr>

- ## Approach 2:- Compare with Sorted Array
    - ### Intuition:
        The problem asks us to determine whether an array is sorted in non-decreasing order and then rotated. The key observation is that if an array is sorted and rotated, there should be at most **one descent** where an element is greater than the next (i.e., the array should "break" its sorted order only once). The array may have duplicate elements, but it should still follow this rule. If we can find such a rotation, the array is valid; otherwise, it isn't.

    - ### Approach:
        1. **Sorting the Array:**
            - We first create a sorted version of the original array to compare against. This allows us to identify the correct order of elements in a valid rotated array.

        2. **Rotation Simulation:**
            - We simulate each possible rotation of the array (by shifting the array to the right `n` times), and compare the rotated version of the array to the sorted version.
            - For each rotation, check if all the elements in the rotated array match the sorted version.

        3. **Checking Each Rotation:**
            - For each rotation, we use the modulo operation to correctly simulate the circular nature of the rotation and compare each element of the rotated array with the sorted array.
            - If any rotation matches the sorted array, return `True` (indicating the array is a rotated version of a sorted array).
            - If no rotation matches, return `False`.

    - ### Code Implementation
        - **Python Solution**
            ```python3 []
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
            ```
        - **C++ Solution**
            ```cpp []
            class Solution {
            public:
                bool check(vector<int>& nums) {
                    // Step 1: Create a copy of the original array 'nums' called 'sorted_nums'
                    // and sort it in non-decreasing order.
                    vector<int> sorted_nums = nums;
                    sort(nums.begin(), nums.end());

                    // Step 2: Loop through every possible rotation from 0 to nums.size() - 1.
                    for(int rotationCount = 0; rotationCount < nums.size(); ++rotationCount) {
                        // Step 3: Assume that the current rotation matches the sorted array.
                        bool is_Match = true;
                        
                        // Step 4: For each rotation, compare the rotated version of 'nums'
                        // with the sorted array ('sorted_nums') element by element.
                        for(int index = 0; index < nums.size(); ++index) {
                            // The (rotationCount + index) % nums.size() gives the rotated position.
                            if(nums[(rotationCount + index) % nums.size()] != sorted_nums[index]) {
                                // If any element doesn't match, mark the match as false and break out of the loop.
                                is_Match = false;
                                break;
                            }
                        }

                        // Step 5: If the current rotation matches the sorted array, return true.
                        if(is_Match) return true;
                    }

                    // Step 6: If no valid rotation matches the sorted array, return false.
                    return false;
                }
            };
            ```

    - ### Time Complexity:
        - Sorting the array takes **$O(n \times log(n))$** time.
        - The outer loop runs for $n$ rotations, and for each rotation, we compare all $n$ elements of the array, resulting in **$O(n)$** time for each rotation.
        - Therefore, the overall time complexity is **$O(n^2)$** due to the combination of sorting and comparing rotations.

    - ### Space Complexity:
        - We use an additional array `sorted_nums` of size $n$ to store the sorted version of the input array.
        - Therefore, the space complexity is **$O(n)$** because of the extra storage required for the sorted array.
<hr>

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