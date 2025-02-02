#include <vector>
using namespace std;

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