/*
* @Author: Lich_Amnesia
* @Date:   2016-12-27 12:06:12
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2016-12-27 12:07:45
* 先用hashmap统计数字出现次数，然后使用priorityqueue存储最大出现次数的字符，然后一个个add进去。
* 如果要放得时候队列为空，那么就return 空
*/


public class Solution {
    public String rearrangeString(String str, int k) {
        if (k == 0){
            return str;
        }
        
        // initial the hashmap counter
        final HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 0; i < str.length(); i ++){
            char c = str.charAt(i);
            if (map.containsKey(c)){
                map.put(c, map.get(c) + 1);
                
            }else{
                map.put(c, 1);
            }
        }
        
        // priority queue
        PriorityQueue<Character> queue = new PriorityQueue<Character>(new Comparator<Character>(){
            public int compare(Character a, Character b){
                if (map.get(a).intValue() != map.get(b).intValue()){
                    return map.get(b).intValue() - map.get(a).intValue();
                }else{
                    return a.compareTo(b);
                }
            }
        });
        
        for (char c: map.keySet()){
            queue.offer(c);
        }
        StringBuilder sb = new StringBuilder();
 
        int len = str.length();
        
        while(!queue.isEmpty()){
            int cnt = Math.min(len, k);
            ArrayList<Character> arr = new ArrayList<Character>();
            
            for (int i = 0; i < cnt; i ++){
                if (queue.isEmpty()){
                    return "";
                }
                char c = queue.poll();
                sb.append(String.valueOf(c));
                map.put(c, map.get(c) - 1);
                
                if (map.get(c) > 0){
                    arr.add(c);
                }
                len --;
            }
            for (char c: arr){
                queue.offer(c);
            }
        }
        return sb.toString();
    }
    
}