#/usr/local/bin/python3
# -*- coding: utf-8 -*-

RED = 0
BLACK = 1


class RBTreeNodes:

    def __init__(self, key, left=None, right=None, parent=None, color=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class RedBlackTree:

    def __init__(self, root=None):
        self.nil = RBTreeNodes(None, color=BLACK)
        self.root = root
        self.size = 0

    def insert(self, inode):
        node = RBTreeNodes(inode)
        t = RBTreeNodes(None, color=BLACK)
        t_nil = None
        currentNode = self.root
        while currentNode and currentNode.key:
            t_nil = currentNode
            if currentNode.key < node.key:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
        if not t_nil:
            self.root = node
            node.parent = t
            node.color = BLACK
        elif node.key < t_nil.key:
            t_nil.left = node
            node.parent = t_nil
        else:
            t_nil.right = node
            node.parent = t_nil
        node.color = RED
        node.left = t
        node.right = t
        # print(self.root.parent.color)
        # print(node.color)
        self.insertFixup(node)

        # self.insertFixup(node)

    def insertFixup(self, node):
        while node.parent.color is RED:
            if node.parent is node.parent.parent.left:
                y = node.parent.parent.right
                if y.color is RED:
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                    # print(node.parent.color)
                    continue
                elif node is node.parent.right:
                    node = node.parent
                    self.leftRotate(node)
                node.parent.color = BLACK
                node.parent.parent.color = RED
                self.rightRotate(node.parent.parent)
                return
            else:
                y = node.parent.parent.left
                if y.color is RED:
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                    continue
                elif node is node.parent.left:
                    node = node.parent
                    self.rightRotate(node)
                node.parent.color = BLACK
                node.parent.parent.color = RED
                self.leftRotate(node.parent.parent)
                return
        self.root.color = BLACK
        # print(self.root.color,self.root.key,self.root.parent.color)

    def preorderRBTreeWalk(self, node):
        if node:
            print(node.key, node.color)
            self.preorderRBTreeWalk(node.left)
            self.preorderRBTreeWalk(node.right)

    def inorderRBTreeWalk(self):
        if self.root:
            self._inorderRBTreeWalk(self.root)
        else:
            return None

    def _inorderRBTreeWalk(self, root):
        if not root:
            return
        self._inorderRBTreeWalk(root.left)
        nodes2.append(root.key)
        if root.key:
        	print(root.key, root.color)
        self._inorderRBTreeWalk(root.right)

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

# 测试代码
# nodes = [15, 6]
nodes = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
nodes2 = []
rbt = RedBlackTree()
for node in nodes:
    rbt.insert(node)
# rbt.inorderRBTreeWalk()
# for nodes in nodes2:
# 	print(node)
rbt.preorderRBTreeWalk(rbt.root)
x = rbt.root
# print(x.key)
# print(rbt.root.key)
