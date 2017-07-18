/*
* @Author: Lich Amnesia
* @Date:   2016-10-28 16:34:07
* @Last Modified by:   Lich Amnesia
* @Last Modified time: 2016-10-28 16:42:08
*/

public class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        char[] ws = s.toCharArray();
        char[] wp = p.toCharArray();
        boolean[][] dp = new boolean[m+1][n+1];
        dp[0][0] = true;
        for (int i = 1; i < n + 1; i ++){
            dp[0][i] = dp[0][i - 1] && wp[i - 1] == '*';
        }
        for (int i = 1; i < m + 1; i ++){
            dp[i][0] = false;
        }
        for (int i = 1; i < m + 1; i ++){
            for (int j = 1; j < n + 1; j ++){
                if (wp[j - 1] == '?' || wp[j - 1] == ws[i - 1])
                    dp[i][j] = dp[i - 1][j - 1];
                else if (wp[j - 1] == '*')
                    dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
            }
        }
        return dp[m][n];
    }
}

