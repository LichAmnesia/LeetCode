/*
* @Author: Lich_Amnesia
* @Date:   2016-08-30 23:05:19
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2016-08-31 00:03:56
* @3. Longest Substring Without Repeating Characters
*/

#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int next[1000];
        if (s.length() == 1){
            return 1;
        } 
        int maxLen = 0;
        int j = -1;
        for (int i = 0; i < 1000;i ++){
            next[i] = -1;
        }
        for (int i = 0; i < s.length(); i ++){
            j = max(next[s[i]], j);
            maxLen = max(maxLen, i - j);
            // for (int k = 0; k < 10; k ++){
            //     printf("%d ", next[k]);
            // }cout << endl;
            // printf("%d\n", j);
            next[s[i]] = i;
        }
        return maxLen;
    }
};

int main(){
    string s = "abcabcd";
    Solution ans;
    cout << ans.lengthOfLongestSubstring(s);
    return 0;
}