# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert(root):
    if root.left or root.right:
        root.left, root.right = root.right, root.left
        if root.left:
            invert(root.left)
        if root.right:
            invert(root.right)


class Solution:
    def invertTree(self, root):
        if root:
            invert(root)
        return root


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
