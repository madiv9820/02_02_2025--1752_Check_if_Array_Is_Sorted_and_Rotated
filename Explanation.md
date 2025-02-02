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