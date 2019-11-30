import binary_search_tree

class Node(binary_search_tree.Node):
    pass

class AVLTree(binary_search_tree.BinarySearchTree):
    def insert(self, new_node, node = 0):
        super().insert(new_node, node)
        self.check_fix_AVL(new_node.parent)
        return new_node
    
    def update_all_heights_upwards(self, node):
        node.update_height()
        if node is not self.root:
            self.update_all_heights_upwards(node.parent)
    
    def _left_rotate(self, x): 
        # x, y, B notation follows MIT 6.006 Lecture 6.
        y = x.right
        B = y.left
        y.parent = x.parent
        y.left = x
        x.parent = y
        x.right = B
        if B is not None:
            B.parent = x
        if y.parent is None:
            self.root = y
        elif y.parent.left == x:
            y.parent.left = y
        else:
            y.parent.right = y
        self.update_all_heights_upwards(x)

    def _right_rotate(self,x):
        y = x.left
        B = y.right
        y.parent = x.parent
        y.right = x
        x.parent = y
        x.left = B
        if B is not None:
            B.parent = x
        if y.parent is None:
            self.root = y
        elif y.parent.right == x:
            y.parent.right = y
        else:
            y.parent.left = y
        self.update_all_heights_upwards(x)

    def check_fix_AVL(self, node):
        if node is None:
            return
        if abs(node.balance()) < 2:
            self.check_fix_AVL(node.parent)
            return
        if node.balance() == 2: # right too heavy
            if node.right.balance() >= 0:
                self._left_rotate(node)
            else:
                self._right_rotate(node.right)
                self._left_rotate(node)
        else: # node.balance() == -2, left too heavy
            if node.left.balance() <= 0:
                self._right_rotate(node)
            else:
                self._left_rotate(node.left)
                self._right_rotate(node)
        self.check_fix_AVL(node.parent)

def AVL_sort(array):
    my_tree = AVLTree(array)
    return my_tree.sort()

if __name__ == "__main__":

    # tree = AVLTree([0,3,7,5,2,1,9,10,11,12,13,14,15,16,17,-1,-2,-3,-4,-5,-5])
    # print(tree)
    # print(tree.sort())
    # tree = AVLTree(["Zhao", "Qian", "Sun","Li", "Zhou", "Wu", "Zheng", "Wang"])
    # print(tree)
    # print(tree.sort())
    # print(AVL_sort(["Zhao", "Qian", "Sun","Li", "Zhou", "Wu", "Zheng", "Wang"]))

    tree = AVLTree([5.2, 5.6, 8.6, 9.3, 4.2, 57.6, 7.6, 15.9, 29.3, 13.1, 5.0, 6.0])
    print(tree)
    print(tree.sort())
