import unittest
from lab3 import BinaryTree, is_tree_balanced

def top_view(root):
    if not root:
        return []
    top_view_map = {}
    queue = [(root, 0)]
    while queue:
        node, position = queue.pop(0)
        if position not in top_view_map:
            top_view_map[position] = node.value
        if node.left:
            queue.append((node.left, position - 1))
        if node.right:
            queue.append((node.right, position + 1))
    return [top_view_map[pos] for pos in sorted(top_view_map.keys())]

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_val = preorder[0]
    root = BinaryTree(root_val)
    mid = inorder.index(root_val)
    root.left = build_tree(preorder[1:mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])
    return root

class TestBinaryTreeBalance(unittest.TestCase):

    def test_tree(self):
        root = BinaryTree(4)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(1)
        root.left.right = BinaryTree(2)
        root.right = BinaryTree(5)
        root.right.right = BinaryTree(6)
        root.right.right.right = BinaryTree(7)
        root.right.right.right.right = BinaryTree(8)
        root.right.right.right.right.left = BinaryTree(9)
        root.right.right.right.right.right = BinaryTree(10)

        result = top_view(root)
        print("\nВигляд дерева зверху:", result)

        self.assertFalse(is_tree_balanced(root))

    def test_build_from_preorder_and_inorder(self):
        preorder = [4, 3, 1, 2, 5, 6, 7, 8, 9, 10]
        inorder = [1, 3, 2, 4, 5, 6, 7, 9, 8, 10]

        restored_root = build_tree(preorder, inorder)

        self.assertEqual(restored_root.value, 4)
        self.assertEqual(restored_root.left.value, 3)
        self.assertEqual(restored_root.left.left.value, 1)
        self.assertEqual(restored_root.left.right.value, 2)
        self.assertEqual(restored_root.right.value, 5)
        self.assertEqual(restored_root.right.right.right.right.value, 8)
        self.assertEqual(restored_root.right.right.right.right.left.value, 9)
        self.assertEqual(restored_root.right.right.right.right.right.value, 10)


if __name__ == '__main__':
    unittest.main()