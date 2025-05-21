# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # 더미 노드를 만들어서 head가 삭제될 경우도 처리
        dummy = ListNode(0)
        dummy.next = head

        # 두 포인터 설정
        fast = slow = dummy

        # fast를 n+1칸 먼저 이동 (slow가 삭제 노드의 전 노드에 위치하게 하기 위함)
        for _ in range(n+1):
            fast = fast.next

        # fast와 slow를 함게 이동
        while fast:
            fast = fast.next
            slow = slow.next

        #삭제
        slow.next = slow.next.next

        return dummy.next

        