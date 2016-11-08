#/usr/bin/env python3
# -*- coding: utf-8 -*-
# def InorderTreeWalk(tree):
# 	pass

# def TreeSearch(tree, key):
# 	pass

# def InterativeTreeSearch(tree, key):
# 	pass

# def TreeMinimum(tree):
# 	pass

# def TreeMaximum(tree):
# 	pass

# def TreeSuccessor(tree):
# 	pass
class TreeNode:
	def __init__(self, key, left=None, right=None, parent=None):
		self.key=key
		self.left=left
		self.right=right
		self.parent=parent

	def hasLeftChild(self):
		return self.left

	def hasRightChild(self):
		return self.right
	def isLeftChild(self):
		return self.parent and self.parent.left == self

	def isRightChild(self):
		return self.parent and self.parent.right == self

class BinarySearchTree:
	def __init__(self):
		self.root=None
		self.size=0

	def insert(self, node):
		node = TreeNode(node)
		if not self.root:
			self.root = node
		else:
			currentNode = self.root
			while True:
				if currentNode.key >= node.key:
					if currentNode.left:
						currentNode = currentNode.left
					else:
						node.parent = currentNode
						currentNode.left = node
						self.size += 1
						break
				else:
					if currentNode.right:
						currentNode = currentNode.right
					else:
						node.parent = currentNode
						currentNode.right = node
						self.size += 1
						break

	def find(self, key):
		if not self.root:
			# print("二叉树不存在，查找失败！")
			return None 
		return self._find(key,self.root)
	
	def __find(self, key, node):
		if not node:
			return None
		elif node.key == key:
			return node
		elif node.key > key:
			return self._find(key, node.left)
		else:
			return self._find(key, node.right)

	def treeMinimum(self):
		if self.root:
			current = self.root
			while current.left:
				current = current.left
			return current
		else:
			return None

	def treeMaximum(self):
		if self.root:
			current = self.root
			while current.right:
				current = current.right
			return current
		else:
			return None

	def inorderTreeWalk(self):
		if self.root:
			return self._inorderTreeWalk(self.root)
		else:
			return None

	def _inorderTreeWalk(self, root):
		if not root:
			return
		self._inorderTreeWalk(root.left)
		print(root.key)
		self._inorderTreeWalk(root.right)


bst = BinarySearchTree()
nodes = [15,6,18,3,7,17,20,2,4,13,9]
for node in nodes:
	bst.insert(node)
bst.inorderTreeWalk()


















