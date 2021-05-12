# Full Binary Tree Implementation
# Implenting below
# 1.Create tree
# 2.Insert Nodes
# 3.traverse(pre-order,in-order,post-order)
# 4.Searching
# 5.Find min & max Node
# 6.Deletion of any node


class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None


class BST():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if self.val == val:
            return

        if val > self.val:
            if self.right:
                self.right.insert(val)
            else:
                new_node = BST(val)
                self.right = new_node

        else:
            if val < self.val:
                if self.left:
                    self.left.insert(val)
                else:
                    new_node = BST(val)
                    self.left = new_node

    def traverse(self, method='pre'):
        if method == 'pre':
            print(self.val)
            if self.left:
                self.left.traverse()

            if self.right:
                self.right.traverse()
        elif method == 'inorder':
            if self.left:
                self.left.traverse(method)
            print(self.val)

            if self.right:
                self.right.traverse(method)
                # print(self.val)
        elif method == 'post':
            if self.left:
                self.left.traverse(method)

            if self.right:
                self.right.traverse(method)
                # print(self.val)
            print(self.val)

        else:
            return 'Invalid Method'

    def min_max(self, e='min'):
        if self.val is not None:
            if e == 'min':
                while(self.left):
                    self = self.left
                return self.val

            elif e == 'max':
                while self.right:
                    self = self.right
                return self.val
            else:
                return 'Invalid'
        return 'Empty Tree'

    def search(self, val):
        if self.val is None:
            return 'Empty Tree'

        if self.val == val:
            return 'Node is present in Tree'

        if val > self.val:
            if self.right:
                return self.right.search(val)
            return 'Node is not present in Tree'
        if val < self.val:
            if self.left:
                return self.left.search(val)
            return 'Node is not present in tree'

    def delete(self, val):

        if self.val is None:
            return 'Empty Tree'

        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            else:
                print('Not Present To Delete')

        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            else:
                print('Not Present To Delete')

        if self.val == val:
            if self.right is None:
                temp = self.left
                self = None
                return temp
            if self.left is None:
                temp = self.right
                self = None
                return temp

            temp = self.right
            while temp.left:
                temp = temp.left
            self.val = temp.val
            self.right = self.right.delete(temp.val)
        return self


root = BST(None)
nodes = [30, 10, 50, 7, 20, 40, 100, 1, 9, 35]
for i in nodes:
    root.insert(i)
root.traverse('inorder')
print('Min,Max :', root.min_max('min'), root.min_max('max'))
print('Searching:', root.search(20))
root.delete(7)
root.traverse('inorder')
