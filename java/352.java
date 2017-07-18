/*
* @Author: Lich_Amnesia
* @Date:   2016-12-27 11:47:45
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2016-12-27 11:48:35
* 使用TreeSet存储已经有的区间，并且调用floor函数和higher函数找到比Val大或者小的区间，进行比较，然后进行合并
*/

/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class SummaryRanges {

    /** Initialize your data structure here. */
    private TreeSet<Interval> intervalSet;
    public SummaryRanges() {
        intervalSet = new TreeSet<Interval>(new Comparator<Interval>(){
            public int compare(Interval a, Interval b){
                return a.start - b.start;
                
            }
            
        });
    }
    
    public void addNum(int val) {
        Interval intervalVal = new Interval(val, val);
        Interval floor = intervalSet.floor(intervalVal);
        if (floor != null){
            if (floor.end >= intervalVal.start){
                return;
            }else if(floor.end + 1 == intervalVal.start){
                intervalVal.start = floor.start;
                intervalSet.remove(floor);
            }
        }
        Interval higher = intervalSet.higher(intervalVal);
        if (higher != null && higher.start == intervalVal.end + 1){
            intervalVal.end = higher.end;
            intervalSet.remove(higher);
        }
        intervalSet.add(intervalVal);
    }
    
    public List<Interval> getIntervals() {
        return Arrays.asList(intervalSet.toArray(new Interval[0]));
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * List<Interval> param_2 = obj.getIntervals();
 */

