/*
* @Author: Lich_Amnesia
* @Date:   2017-01-02 13:20:08
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2017-01-02 13:20:09
*/

public class java {
    public static void main(String[] args) {

    }
}public class Solution {
    public int countComponents(int n, int[][] edges) {
        int count = n;
        int[] root = new int[n];
        /* initialize */
        for (int i = 0; i < n; i ++){
            root[i] = i;
        }
        
        for (int i = 0; i < edges.length; i ++){
            int x = edges[i][0];
            int y = edges[i][1];
            
            int xRoot = getRoot(root, x);
            int yRoot = getRoot(root, y);
            
            if (yRoot != xRoot){
                root[yRoot] = xRoot;
                count --;
            }
        }
        return count;
    }
    
    public int getRoot(int[] root, int x){
        while (root[x] != x){
            root[x] = root[root[x]];
            x = root[x];
            
        }
        return x;
    }
    
}