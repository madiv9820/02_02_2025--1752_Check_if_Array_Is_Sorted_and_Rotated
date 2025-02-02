#include <iostream>
#include "Solution.hpp"

class UnitTest {
private:
    Solution sol;
    vector<pair<vector<int>, bool>> testcases;
public:
    UnitTest() {
        testcases = {{{3,4,5,1,2}, true}, {{2,1,3,4}, false}, {{1,2,3}, true}};
    }

    void test() {
        for(int i = 0; i < testcases.size(); ++i) {
            vector<int>& nums = testcases[i].first;
            bool output = testcases[i].second;
            bool result = sol.check(nums);
            cout << "TestCase " << i+1 << ": " << ((result == output) ? "passed":"result") << endl;
        }
    }
};

int main() {
    UnitTest test;
    test.test();
}