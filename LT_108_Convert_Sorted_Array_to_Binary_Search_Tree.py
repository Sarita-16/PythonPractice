# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        # Base case: if the array is empty, return None
        if len(nums) == 0:
            return None

        # Find the middle index
        mid = len(nums) // 2

        # Create the root node with the middle element
        root = TreeNode(nums[mid])

        # Recursively build the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root

# Example usage:
# Create an instance of the Solution class
sol = Solution()

# A sorted array
nums = list(map(int, input("Enter a sorted array : ").split()))


# Convert the sorted array to a BST
bst_root = sol.sortedArrayToBST(nums)

# Function to print the BST in a pre-order traversal (for testing purposes)
def pre_order_traversal(node):
    if not node:
        return
    print(node.val, end=' ')
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

# Print the BST nodes in pre-order traversal
pre_order_traversal("BST nodes in  pre-order traversal : ", bst_root)
