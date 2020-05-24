# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    depth = 0
    tree = root

    def dfs():
        return list(_dfs(0))

    def _dfs(node_ix):
        if node_ix >= 2**(depth-1) - 1:  # leaf node
            yield [node_ix]
        else:
            for path in _dfs(2*node_ix+1):  # left child
                yield [node_ix] + path
            for path in _dfs(2*node_ix+2):  # right child
                yield [node_ix] + path

    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.tree = root
        n = len(root)
        n += 1
        while n != 2:
            n //= 2
            self.depth += 1
        l = dfs()
        for i in range(len(l)):
            dic = {}
            ll = len(l[i])
            if l[-1] == None:
                ll -= 1
            for j in range(len(l[i])):
                if tree[l[i][j]] not in dic.keys():
                    dic[tree[l[i][j]]] = 1
                else:
                    dic[tree[l[i][j]]] += 1
            even = 0
            odd = 0
            for j in dic.keys():
                if dic[j]%2 == 0:
                    even += 1
                else:
                    odd += 1
            flag = True
            if odd >= 2:
                flag = False
            if flag:
                cnt += 1
        return cnt