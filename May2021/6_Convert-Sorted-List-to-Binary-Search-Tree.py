# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arr, n = [], head
        while n:
            arr.append(n.val)
            n = n.next
            
        return self.createBST(arr)
    
    def createBST(self,arr):
        if arr:
            m = len(arr)//2
            node = TreeNode(arr[m])
            node.left = self.createBST(arr[:m])
            node.right = self.createBST(arr[m+1:])
            
            return node
