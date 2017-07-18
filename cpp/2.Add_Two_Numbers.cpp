/*
* @Author: Lich_Amnesia
* @Date:   2016-08-30 22:14:22
* @Last Modified by:   Lich_Amnesia
* @Last Modified time: 2016-08-30 23:03:03
*/

#include <bits/stdc++.h>
using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode ans = ListNode(0);
        ListNode* p = &ans;
        int val = 0;
        int ten = 0;
        while (l1 || l2){
            // printf("%d %d\n", val, ten);
            val += (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
            ten = val / 10;
            val = val % 10;
            p->next = new ListNode(val);
            p = p->next;
            val = ten;
            if (l1->next) l1 = l1->next;
            if (l2->next) l2 = l2->next;
        }
        if (val){
            p->next = new ListNode(val);
            p = p->next;
        }
        return ans.next;
    }
};



int main(){
    ListNode A = ListNode(2);
    ListNode *pA = &A;
    pA->next = new ListNode(4);
    pA->next->next = new ListNode(3);

    ListNode B = ListNode(5);
    ListNode *pB = &B;
    pB->next = new ListNode(6);
    pB->next->next = new ListNode(7);
    Solution ans;
    ListNode* Node = ans.addTwoNumbers(pA, pB);
    while (Node){
        printf("%d -> ", Node->val);
        Node = Node->next;
    }
    return 0;
}