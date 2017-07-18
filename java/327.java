/*
* @Author: Lich_Amnesia
* @Date:   2017-01-02 13:41:19
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2017-01-02 13:42:22
* 二分求解，但是复杂度仍然是N^2
*/

public class Solution {
    long[] counts;
    int lower, upper;
    public int countRangeSum(int[] nums, int lower, int upper) {
        int length = nums.length;
        if (length < 1){
            return 0;
        }
        counts = new long[length];
        this.lower = lower;
        this.upper = upper;
        counts[0] = nums[0];
        for (int i = 1; i < length;i ++){
            counts[i] = counts[i - 1] + nums[i];  
        }
        return Count(nums, 0, length - 1);
    }
    
    public int Count(int[] nums, int left, int right){
        if (left == right){
            if (nums[left] <= upper && nums[left] >= lower){
                return 1;
            }
            return 0;
        }
        int mid = (left + right) / 2;
        int total = 0;
        for (int i = left; i <= mid; i ++){
            for (int j = mid + 1; j <= right; j ++){
                long tmpNum = counts[j] - counts[i] + nums[i];
                if(tmpNum >= lower && tmpNum <= upper){
                    ++total;
                }
            }
        }
        return total + Count(nums, left, mid) + Count(nums, mid + 1, right);
    }
}