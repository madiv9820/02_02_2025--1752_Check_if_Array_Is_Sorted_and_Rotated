#include <vector>
using namespace std;

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