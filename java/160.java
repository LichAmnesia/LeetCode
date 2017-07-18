/*
* @Author: Lich_Amnesia
* @Date:   2016-09-20 14:52:14
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2016-09-20 14:52:23
*/

public class java {
    public static void main(String[] args) {

    }
}


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode pa, pb, ta, tb;
        for(ta=headA, tb=headB; ta != null && tb != null; ta=ta.next, tb=tb.next);
        for(pa=headA; ta!=null; ta=ta.next, pa=pa.next);
        for(pb=headB; tb!=null; tb=tb.next, pb=pb.next);
        for(; pa!=pb; pa=pa.next, pb=pb.next);
        return pa;
    }
}