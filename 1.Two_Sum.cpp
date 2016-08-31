/*
* @Author: Lich_Amnesia
* @Date:   2016-06-27 09:56:27
* @Last Modified by:   Alwa
* @Last Modified time: 2016-06-27 10:47:50
*/

#include <iostream>
#include <vector>
#include <cstdio>
#include <map>
using namespace std;

class Solution{
public:
    vector<int> ans;
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> int_hash;
        for (int i = 0; i < nums.size(); i++){
            int com = target - nums[i];
            if (int_hash.find(com) != int_hash.end()){
                ans.push_back(i);
                ans.push_back(int_hash[com]);
                return ans;
            }
            int_hash[nums[i]] = i;
        }     
        return ans;
    }
};


int main(){
    Solution ans;
    vector<int> nums;
    nums.push_back(3);
    nums.push_back(2);
    nums.push_back(4);
    int target = 6;
    vector<int> a = ans.twoSum(nums, target);
    for (int i = 0; i < a.size(); i ++){
        printf("%d ", a[i]);
    }
    return 0;
}