package hasPathSum;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

// 113
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null)
            return false;

       if (root.left == null && root.right == null) return sum == root.val;

       return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum- root.val);
    }

}