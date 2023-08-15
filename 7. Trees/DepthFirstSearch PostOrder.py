def dfs_post_order(self):
    results = []
    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
    traverse(self.root)
    return results