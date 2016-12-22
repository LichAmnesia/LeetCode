/*
* @Author: Lich_Amnesia
* @Date:   2016-12-22 15:21:14
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2016-12-22 15:21:18
*/


public class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length, n = 0;
        if (m > 0) n = matrix[0].length;
        if (m * n == 0) return 0;
        
        int M = Math.max(m, n);
        int N = Math.min(m, n);
        int ans = Integer.MIN_VALUE;
        for (int x = 0; x < N; x ++){
            int sum[] = new int[M];
            for (int y = x; y < N; y ++){
                TreeSet<Integer> set = new TreeSet<Integer>();
                int num = 0;
                for (int z = 0; z < M; z ++){
                    sum[z] += m > n? matrix[z][y] : matrix[y][z];
                    num += sum[z];
                    if (num <= k){
                        ans = Math.max(ans, num);
                    }
                    Integer i = set.ceiling(num - k);
                    if (i != null){
                        ans = Math.max(ans, num - i);
                    }
                    set.add(num);
                    
                }
            }
        }
        return ans;
    }
}