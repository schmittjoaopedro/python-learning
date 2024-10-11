from typing import Optional, List
from math import floor, ceil


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        rootIdx = len(nums) // 2
        root = TreeNode(val=nums[rootIdx])
        self.buildTree(root, nums, rootIdx, 0, len(nums) - 1)
        return root

    def buildTree(self, root, nums, rootIdx, leftIdx, rightIdx):

        if rootIdx - leftIdx > 0:
            leftChildIdx = floor((rootIdx + leftIdx) / 2)
            leftChild = TreeNode(val=nums[leftChildIdx])
            root.left = leftChild
            self.buildTree(leftChild, nums, leftChildIdx, leftIdx, rootIdx - 1)

        if rightIdx - rootIdx > 0:
            rightChildIdx = ceil((rightIdx + rootIdx) / 2)
            rightChild = TreeNode(val=nums[rightChildIdx])
            root.right = rightChild
            self.buildTree(rightChild, nums, rightChildIdx, rootIdx + 1, rightIdx)
