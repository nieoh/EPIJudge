from test_framework import generic_test
from list_node import ListNode

def add_two_numbers(L1, L2):
    L = ListNode()
    dummy_head = L
    carry = 0

    while L1 and L2:
        summ = L1.data + L2.data + carry
        
        if summ >= 10:
            L.next = ListNode(summ%10)
            carry = 1
        else:
            L.next=ListNode(summ)
            carry = 0
        L = L.next
        L1, L2 = L1.next, L2.next

    while L1:
        if carry == 0:
            L.next = L1
            break
        summ = L1.data + carry
        if summ >= 10:
            L.next = ListNode(summ%10)
            carry = 1
        else:
            L.next = ListNode(summ)
            carry = 0
        L, L1 = L.next, L1.next

    while L2:
        if carry == 0:
            L.next = L2
            break
        summ = L2.data + carry
        if summ >= 10:
            L.next = ListNode(summ%10)
            carry = 1
        else:
            L.next = ListNode(summ)
            carry = 0
        L, L2 = L.next, L2.next

    if carry != 0:
        L.next = ListNode(carry)
    return dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
