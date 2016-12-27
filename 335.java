/*
* @Author: Lich_Amnesia
* @Date:   2016-12-27 12:34:33
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2016-12-27 12:35:01
* 相交情况：http://www.cnblogs.com/grandyang/p/5216856.html
*/

public class Solution {
    public boolean isSelfCrossing(int[] x) {
        for (int i = 3; i < x.length; i ++){
            if (x[i] >= x[i - 2] && x[i - 3] >= x[i - 1]){
                return true;
            }
            if (i >= 4 && x[i - 1] == x[i - 3] && x[i - 4] + x[i] >= x[i - 2]){
                return true;
            }
            if (i >= 5 && x[i - 2] >= x[i - 4] && x[i - 3] >= x[i - 1] && x[i] + x[i - 4] >= x[i - 2] && x[i - 5] + x[i - 1] >= x[i - 3]){
                return true;
            }
            
        }
        return false;
    }
}
