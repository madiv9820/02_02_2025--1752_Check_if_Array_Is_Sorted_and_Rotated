#include <vector>
#include <algorithm>
using namespace std;

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