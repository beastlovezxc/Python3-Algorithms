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
import matplotlib.pyplot as plt
# 二叉树节点类
class TreeNode:
	def __init__(self, key, left=None, right=None, parent=None):
		self.key=key
		self.left=left
		self.right=right
		self.parent=parent

	# 该节点是否有左孩子
	def hasLeftChild(self):
		return self.left

	# 该节点是否有右孩子
	def hasRightChild(self):
		return self.right

	# 该节点是否为左孩子 
	def isLeftChild(self):
		return self.parent and self.parent.left == self

	# 该节点是否为右孩子
	def isRightChild(self):
		return self.parent and self.parent.right == self

# 二叉搜索树类
class BinarySearchTree:
	# 二叉树初始化
	def __init__(self, root=None):
		self.root=root
		self.size=0

	# 二叉搜索树插入
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

	# 二叉搜索树查找
	def find(self, key):
		if not self.root:
			return None 
		return self._find(key,self.root)
	
	def _find(self, key, node):
		if not node:
			return None
		elif node.key == key:
			return node
		elif node.key > key:
			return self._find(key, node.left)
		else:
			return self._find(key, node.right)

	# 二叉搜索树最小值
	def treeMinimum(self):
		if self.root:
			current = self.root
			while current.left:
				current = current.left
			return current
		else:
			return None

	# 二叉搜索树最大值
	def treeMaximum(self):
		if self.root:
			current = self.root
			while current.right:
				current = current.right
			return current
		else:
			return None

	# 中序遍历二叉搜索树
	def inorderTreeWalk(self):
		if self.root:
			return self._inorderTreeWalk(self.root)
		else:
			return None

	def _inorderTreeWalk(self, root):
		if not root:
			return
		self._inorderTreeWalk(root.left)
		# print(root.key)
		nodes2.append(root.key)
		self._inorderTreeWalk(root.right)

	# 
	# 将以znodes为根节点的子树替换为以ynodes为根节点的子树
	# 
	def transPlant(self, znodes, ynodes):
		if not znodes.parent:
			self.root = ynodes
		elif znodes.parent.left == znodes:
			znodes.parent.left = ynodes
		else:
			znodes.parent.right = ynodes
		if ynodes:
			ynodes.parent = znodes.parent
	# 
	# 删除二叉搜索树中的节点
	# 
	def treeDelete(self, zKey):
		znodes = self.find(zKey)
		if znodes.left and znodes.right:
			zTree = BinarySearchTree(znodes.right)
			y = zTree.treeMinimum()
			if y.parent != znodes:
				self.transPlant(y, y.right)
				y.right = z.right
				y.right.parent = y
			self.transPlant(znodes, y)
			y.left = znodes.left
			y.left.parent = y
		elif not znodes.left:
			self.transPlant(znodes, znodes.right)
		else:
			self.transPlant(znodes, znodes.left)
		

bst = BinarySearchTree()
nodes = [15,6,18,3,7,17,20,2,4,13,9]
# 中序遍历将二叉搜索树中元素存入 nodes2 以便输出现实
nodes2 = []

fig = plt.figure()
ax=fig.add_subplot(1, 1, 1)
for node in nodes:
	bst.insert(node)
bst.inorderTreeWalk()
ax.plot(nodes2,'b-.',lw=5)
print("Before delete :%d",len(nodes2))
nodes2 = []
bst.treeDelete(6)
bst.inorderTreeWalk()
print("After delete :%d",len(nodes2))
ax.plot(nodes2,'r-.',lw=5)
plt.show()
















