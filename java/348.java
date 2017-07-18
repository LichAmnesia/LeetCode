/*
* @Author: Lich_Amnesia
* @Date:   2016-12-27 12:24:15
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2016-12-27 12:24:37
* 每行每列，对角线都设定一下共有多少个连续相同的
*/

public class TicTacToe {


    private int[] rows;
    private int[] cols;
    private int diag;
    private int anti_diag;
    
    private int n;
    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        rows = new int[n];
        cols = new int[n];
        diag = 0;
        anti_diag = 0;
        
        this.n = n;
        
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    public int move(int row, int col, int player) {
        int add = player == 1 ? 1 : -1;
        rows[row] += add; cols[col] += add;
        diag += (row == col ? add : 0);
        anti_diag += (row == n - col - 1 ? add : 0);
        return (Math.abs(rows[row]) == n || Math.abs(cols[col]) == n || Math.abs(diag) == n || Math.abs(anti_diag) == n ) ? player : 0;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */