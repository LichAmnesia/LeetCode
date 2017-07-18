/*
* @Author: Lich_Amnesia
* @Date:   2016-12-22 14:36:19
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2016-12-22 14:36:43
* 注意Java的一些用法，hashset和queue
*/


public class SnakeGame {
    Set<Integer> set; // this copy is good for fast loop-up for eating body case
    Deque<Integer> body; // this copy is good for updating tail
    int score;
    int[][] food;
    int foodIndex;
    int width;
    int height;
    /** Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
    public SnakeGame(int width, int height, int[][] food) {
        this.width = width;
        this.height = height;
        this.food = food;
        set = new HashSet<>();
        set.add(0);
        body = new LinkedList<>();
        body.offerLast(0);
        
    }
    
    /** Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body. */
    public int move(String direction) {
        if (score == -1){
            return -1;
        }
        int col = body.peekFirst() % width;
        int row = body.peekFirst() / width;
        switch(direction){
            case "U": row -= 1; break;
            case "D": row += 1; break;
            case "L": col -= 1; break;
            default: col += 1; break;
        }
        int head = row * width + col;
        // case 1. if can not move
        set.remove(body.peekLast());
        if (row < 0 || row == height || col < 0 || col == width || set.contains(head)){
            return score = -1;
        }
        
        // case 2. eat food.
        set.add(head);
        body.offerFirst(head);
        
        if (foodIndex < food.length && row == food[foodIndex][0] && col == food[foodIndex][1]){
            foodIndex ++;
            return ++ score;
        }
        
        body.pollLast();
        return score;
        
    }
}

/**
 * Your SnakeGame object will be instantiated and called as such:
 * SnakeGame obj = new SnakeGame(width, height, food);
 * int param_1 = obj.move(direction);
 */