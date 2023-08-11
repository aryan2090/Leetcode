# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        
        def dfs(node, level):
            if node:
                d[level].append(node.val)
                dfs(node.left, level+1)
                dfs(node.right, level+1) 
        dfs(root, 0)
        return reversed(list(d.values()))