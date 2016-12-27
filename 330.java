/*
* @Author: Lich_Amnesia
* @Date:   2016-12-27 12:55:18
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2016-12-27 12:55:39
* http://www.cnblogs.com/grandyang/p/5165821.html
* 注意计算miss的值是什么
*/

public class Solution {
    public int minPatches(int[] nums, int n) {
        long miss = 1;
        int res = 0, i = 0;
        while (miss <= n){
            if (i < nums.length && (long)nums[i] <= miss){
                miss += nums[i++];
            }else{
                miss += miss;
                res ++;
            }
        }
        return res;
    }
}